"""
Database field helpers
"""
from jobboss.models import WorkCenter

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
