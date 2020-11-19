import datetime
import re
from typing import Optional
from django.template.defaultfilters import slugify
from jobboss.models import Customer, Contact, Address
from .suffixes import STREET_SUFFIX_ABBREVS

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


def get_or_create_customer(
        name: str,
        code: Optional[str] = None,
        set_active: bool = True,
        **kwargs,
) -> Customer:
    """
    Find existing Customer record using fuzzy name matching or create a new
    Customer. Additional kwargs can be provided to overwrite default values
    in columns for customer.

    :param name: business name
    :param code: optional customer code
    :param set_active: change a matched customer's status to active
    :return: matched or newly created JobBOSS Customer record
    """
    if code:
        customer = Customer.objects.filter(customer=code).first()
        if customer is not None:
            return customer
    customer = filter_exact_customer_name(name)
    if customer is None:
        customer = filter_fuzzy_customer_name(name)
    if customer is not None:
        if set_active and customer.status != 'Active':
            customer.status = 'Active'
            customer.save()
        return customer
    customer = Customer(
        customer=get_available_customer_code(name),
        name=name,
        last_updated=datetime.datetime.utcnow(),
        print_statement=False,
        accept_bo=False,
        send_report_by_email=False,
        status='Active'
    )
    if len(kwargs) > 0:
        for k, v in kwargs.items():
            setattr(customer, k, v)
    customer.save()
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
    has_main, has_bill, has_ship = get_address_types_by_customer(customer)
    address = match_address(customer, addr_dict)
    if address is not None:
        is_main = int(address.type[0])
        is_def_bill = int(address.type[1])
        is_def_ship = int(address.type[2])
        needs_save = False
        if is_shipping and not address.shippable:
            address.shippable = True
            needs_save = True
        if is_shipping and not has_ship:
            address.type = '{}{}{}'.format(is_main, is_def_bill, 1)
            needs_save = True
        if not is_shipping and not address.billable:
            address.billable = True
            needs_save = True
        if not is_shipping and not has_bill:
            address.type = '{}{}{}'.format(is_main, 1, is_def_ship)
            needs_save = True
        if needs_save:
            address.save()
        return address
    if addr_dict.get('country') == 'USA':
        country_code = 'US'
    else:
        country_code = addr_dict.get('country')
    phone = addr_dict.get('phone')
    if phone and addr_dict.get('phone_ext'):
        phone += ' x{}'.format(addr_dict.get('phone_ext'))
    is_main = int(not has_main)
    is_def_bill = int(not is_shipping and not has_bill)
    is_def_ship = int(is_shipping and not has_ship)
    type_str = '{}{}{}'.format(is_main, is_def_bill, is_def_ship)
    address = Address(
        customer=customer,
        status='Active',
        type=type_str,
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
    address.save_with_autonumber()
    return address


"""
Helper methods for get_or_create queries
"""
STOP_WORDS = ['and', 'assn', 'assoc', 'co', 'comp', 'corp', 'company',
              'corporation', 'dba', 'gmbh', 'group', 'inc', 'incorporated',
              'intl', 'llc', 'llp', 'lp', 'ltd', 'manufacturing', 'mfg']


def tokenize(name):
    """Tokenization for business names"""
    tokens = slugify(name).split('-')
    if len(tokens) > 1:
        return [t for t in tokens if t not in STOP_WORDS]
    else:
        return tokens


def address_tokenize(street_address):
    """Tokenize street address lines"""
    tokens = slugify(street_address).split('-')
    if len(tokens) > 1:
        return [
            STREET_SUFFIX_ABBREVS[t] if t in STREET_SUFFIX_ABBREVS else t
            for t in tokens
        ]
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
    concatenated phone number. For address line 1 and 2, street suffix
    abbreviations are intuitively matched and punctuation is ignored. Zip code
    intuitively handles plus-4 extensions.

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
    # first get the set of candidate addresses for this customer
    qs = Address.objects.filter(
        customer=customer,
        city__iexact=addr_dict.get('city'),
        state__iexact=addr_dict.get('state'),
        country=country_code,
    ).order_by('-last_updated')
    # next iterate through candidate address and return the first fuzzy match
    # we assume there will never be a very large number of addresses for a
    # single customer
    for candidate_address in qs.all():
        # address line 2
        if address_tokenize(candidate_address.line1) != address_tokenize(
                addr_dict.get('address1')):
            continue
        # address line 2
        if addr_dict.get('address2') and address_tokenize(
                candidate_address.line2) != address_tokenize(
                addr_dict.get('address2')
        ):
            continue
        # zip code
        if len(addr_dict.get('postal_code', '')) == 5:
            if addr_dict.get('postal_code') != candidate_address.zip[0:5]:
                continue
        elif len(addr_dict.get('postal_code', '')) == 10:
            if len(candidate_address.zip) == 5:
                if candidate_address.zip != addr_dict.get('postal_code')[0:5]:
                    continue
            else:
                if candidate_address.zip != addr_dict.get('postal_code'):
                    continue
        elif addr_dict.get('postal_code') != candidate_address.zip:
            continue
        # phone
        if phone and candidate_address.phone:
            if re.sub("[^0-9]", "", phone) != re.sub("[^0-9]", "",
                                                     candidate_address.phone):
                continue
        return candidate_address
    return None


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


def get_address_types_by_customer(customer: Customer):
    types = [d['type'] for d in
             Address.objects.filter(customer=customer).values('type').all()]
    try:
        has_main = any(int(t[0]) for t in types)
    except ValueError:
        has_main = False
    try:
        has_bill = any(int(t[1]) for t in types)
    except ValueError:
        has_bill = False
    try:
        has_ship = any(int(t[2]) for t in types)
    except ValueError:
        has_ship = False
    return has_main, has_bill, has_ship

def get_default_billing_address(customer: Customer) -> Address:
    for addr in Address.objects.filter(customer=customer).order_by('-last_updated'):
        if int(addr.type[1]):
            return addr


def get_default_shipping_address(customer: Customer) -> Address:
    for addr in Address.objects.filter(customer=customer).order_by('-last_updated'):
        if int(addr.type[2]):
            return addr
