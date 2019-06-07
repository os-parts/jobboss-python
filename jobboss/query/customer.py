import datetime
import re
from django.template.defaultfilters import slugify
from django.db import transaction
from django.db.models import Max
from jobboss.models import Customer, Contact, Address

MAX_CODE_LENGTH = 10  # max length of Customer PK
MAX_CODE_RETRIES = 20
MAX_ADDR_CODE_LENGTH = 6  # max length of Ship_To_ID

"""
Queries for finding and creating Customer, Contact, and Address records using
fuzzy record matching to help avoid duplicate records.

* get_or_create_customer
* get_or_create_contact
* get_or_create_address
"""


def get_or_create_customer(name: str) -> Customer:
    """
    Find existing Customer record using fuzzy name matching or create a new
    Customer.

    :param name: business name
    :return: matched or newly created JobBOSS Customer record
    """
    customer = filter_exact_customer_name(name)
    if customer is not None:
        return customer
    customer = filter_fuzzy_customer_name(name)
    if customer is not None:
        return customer
    customer = Customer.objects.create(
        customer=get_available_customer_code(name),
        name=name,
        last_updated=datetime.datetime.utcnow(),
        print_statement=False,
        accept_bo=False,
        send_report_by_email=False,
        status='Active'
    )
    return customer


def get_or_create_contact(customer: Customer, contact_name: str) -> Contact:
    """
    Find existing Contact record for this Customer or create a new Contact.

    :param customer: Customer record
    :param contact_name: Contact.Contact_Name to be fuzzy-matched
    :return: matched or newly created JobBOSS Contact record
    """
    contact = filter_exact_contact_name(customer, contact_name)
    if contact is not None:
        return contact
    contact = Contact(
        customer=customer.customer,
        contact_name=contact_name,
        last_updated=datetime.datetime.utcnow()
    )
    contact.save_with_autonumber()
    return contact


def get_or_create_address(
        customer: Customer, addr_dict: dict, is_shipping: bool = True
) -> Address:
    """
    Find existing Address record for this Customer or a create a new Address.

    :param customer: Customer record
    :param addr_dict: Dictionary containing address fields. Generate using
    ``paperless.objects.Address.to_dict()``.
    :param is_shipping: Set to True if shipping address; otherwise False
    :return: matched or newly created JobBOSS Address record
    """
    address = match_address(customer, addr_dict)
    if address is not None:
        if is_shipping and not address.shippable:
            address.shippable = True
            address.save()
        if not is_shipping and not address.billable:
            address.billable = True
            address.save()
        return address
    if addr_dict.get('country') == 'USA':
        country_code = 'US'
    else:
        country_code = addr_dict.get('country')
    phone = addr_dict.get('phone')
    if phone and addr_dict.get('phone_ext'):
        phone += ' x{}'.format(addr_dict.get('phone_ext'))
    address = Address.objects.create(
        customer=customer,
        status='Active',
        type='000',
        ship_to_id=get_available_address_code(customer, ship=is_shipping),
        line1=addr_dict.get('address1'),
        line2=addr_dict.get('address2'),
        city=addr_dict.get('city'),
        state=addr_dict.get('state'),
        zip=addr_dict.get('postal_code'),
        country=country_code,
        name=customer.name,
        phone=phone,
        lead_days=0,
        last_updated=datetime.datetime.utcnow(),
        billable=not is_shipping,
        shippable=is_shipping
    )
    return address


"""
Helper methods for get_or_create queries
"""
STOP_WORDS = ['and', 'assn', 'assoc', 'co', 'comp', 'corp', 'company',
              'corporation', 'dba', 'gmbh', 'group', 'inc', 'incorporated',
              'intl', 'llc', 'llp', 'lp', 'ltd']


def tokenize(name):
    tokens = slugify(name).split('-')
    if len(tokens) > 1:
        return [t for t in tokens if t not in STOP_WORDS]
    else:
        return tokens


def filter_exact_customer_name(name):
    return Customer.objects.filter(name__iexact=name).order_by(
        '-last_updated').first()


def filter_exact_contact_name(customer: Customer, contact_name):
    return Contact.objects.filter(
        customer=customer.customer,
        contact_name__iexact=contact_name).order_by('-last_updated').first()


def filter_fuzzy_customer_name(name):
    qs = Customer.objects
    for token in tokenize(name):
        qs = qs.filter(name__icontains=token)
    qs.order_by('-last_updated')
    for customer in qs.all():
        if '-'.join(tokenize(customer.name)) == '-'.join(tokenize(name)):
            return customer
    return None


def increment_code(code, max_code_length=MAX_CODE_LENGTH):
    search = re.search('(\d+)$', code)
    if search is None:
        if len(code) < max_code_length:
            return code + '1'
        else:
            return code[0:max_code_length-1] + '1'
    else:
        suffix = search.group(0)
        base_code = code[0:-len(suffix)]
        new_suffix = str(int(search.group(0)) + 1)
        remove = len(base_code) + len(new_suffix) - max_code_length
        if remove > 0:
            base_code = base_code[0:-remove]
        return base_code + new_suffix


def get_available_customer_code(name):
    code = name.upper()[0:MAX_CODE_LENGTH]
    tries = 0
    while tries < MAX_CODE_RETRIES:
        if Customer.objects.filter(customer=code).count() == 0:
            return code
        code = increment_code(code)
        tries += 1
    raise ValueError("Can't find an unused customer code for {}".format(name))


def match_address(customer: Customer, addr_dict: dict) -> Address:
    """
    Find a matching address (case insensitive) for a given customer looking at
    concatenated name, address line 1 and 2, city, state, zip, country, and
    concatenated phone number.

    :param customer: Customer record
    :param addr_dict: Dictionary containing address fields. Generate using
    ``paperless.objects.Address.to_dict()``.
    :return: Address if found; otherwise None
    """
    if addr_dict.get('country') == 'USA':
        country_code = 'US'
    else:
        country_code = addr_dict.get('country')
    phone = addr_dict.get('phone')
    if phone and addr_dict.get('phone_ext'):
        phone += ' x{}'.format(addr_dict.get('phone_ext'))
    qs = Address.objects.filter(
        customer=customer,
        line1__iexact=addr_dict.get('address1'),
        line2__iexact=addr_dict.get('address2'),
        city__iexact=addr_dict.get('city'),
        state__iexact=addr_dict.get('state'),
        zip=addr_dict.get('postal_code'),
        country=country_code,
        phone=phone
    ).order_by('-last_updated')
    return qs.first()


def get_available_address_code(customer: Customer, ship=True):
    if ship:
        code = 'SHIP'
    else:
        code = 'BILL'
    tries = 0
    while tries < MAX_CODE_RETRIES:
        if Address.objects.filter(customer=customer,
                                  ship_to_id=code).count() == 0:
            return code
        code = increment_code(code, MAX_ADDR_CODE_LENGTH)
        tries += 1
    raise ValueError("Can't find an unused address code for {}".format(
        customer.customer))
