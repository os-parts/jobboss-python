from django.test import TransactionTestCase
from jobboss.query.job import shipping_option_summary

SHIPPING_OPTION_1 = {
    'customers_account_number': '12345',
    'customers_carrier': 'UPS',
    'shipping_method': 'ground'
}

SHIPPING_OPTION_2 = {
    'customers_account_number': None,
    'customers_carrier': None,
    'shipping_method': 'next day'
}


class TestJob(TransactionTestCase):
    def test_ship_via(self):
        self.assertEqual('UPS 12345',
                         shipping_option_summary(SHIPPING_OPTION_1))
        self.assertEqual('next day',
                         shipping_option_summary(SHIPPING_OPTION_2))
