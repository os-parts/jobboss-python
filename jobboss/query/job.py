"""
Database field helpers
"""
from string import ascii_lowercase, digits
from jobboss.models import WorkCenter, Job

MAX_JOB_RETRIES = 20


def shipping_option_summary(shipping_option_dict: dict) -> str:
    acct_number = shipping_option_dict.get('customers_account_number')
    carrier = shipping_option_dict.get('customers_carrier')
    shipping_method = shipping_option_dict.get('shipping_method')
    if acct_number:
        return '{} {}'.format(carrier, acct_number)
    else:
        return shipping_method


def terms_summary(payment_details_dict: dict) -> str:
    if payment_details_dict.get('payment_type') == 'credit_card':
        return 'Credit Card'
    else:
        return payment_details_dict.get('purchase_order_number')


def get_work_center(op_name: str) -> WorkCenter:
    return WorkCenter.objects.filter(work_center__iexact=op_name).first()


def increment_job(job_number):
    """Increment job number to find a unique value"""
    last_char = job_number[-1].lower()
    if last_char in ascii_lowercase and last_char != 'z':
        return job_number[0:-1] + \
               ascii_lowercase[ascii_lowercase.find(last_char) + 1]
    else:
        return job_number + 'a'


def get_available_job(order_number: int, sequence_number: int) -> str:
    """Returns an available job number given order number and job sequence
    number."""
    job_number = '{}-{}'.format(order_number, sequence_number)
    tries = 0
    while tries < MAX_JOB_RETRIES:
        if Job.objects.filter(job=job_number).count() == 0:
            return job_number
        job_number = increment_job(job_number)
        tries += 1
    raise ValueError("Can't find an unused job number for {}-{}".format(
        order_number, sequence_number))
