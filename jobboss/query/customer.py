import datetime
import re
from django.template.defaultfilters import slugify
from jobboss.models import Customer

MAX_CODE_LENGTH = 10  # max length of Customer PK
MAX_CODE_RETRIES = 20


def tokenize(name):
    return slugify(name).split('-')


def filter_exact_customer_name(name):
    return Customer.objects.filter(name__iexact=name).order_by(
        '-last_updated').first()


def filter_fuzzy_customer_name(name):
    qs = Customer.objects
    for token in tokenize(name):
        qs = qs.filter(name__icontains=token)
    qs.order_by('-last_updated')
    return qs.first()


def increment_code(code):
    search = re.search('(\d+)$', code)
    if search is None:
        if len(code) < MAX_CODE_LENGTH:
            return code + '1'
        else:
            return code[0:MAX_CODE_LENGTH-1] + '1'
    else:
        suffix = search.group(0)
        base_code = code[0:-len(suffix)]
        new_suffix = str(int(search.group(0)) + 1)
        remove = len(base_code) + len(new_suffix) - MAX_CODE_LENGTH
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
        send_report_by_email=False
    )
    return customer
