import datetime
from django.test import TransactionTestCase
from jobboss.query.customer import tokenize, filter_exact_customer_name, \
    filter_fuzzy_customer_name, increment_code, get_available_customer_code, \
    get_or_create_customer
from jobboss.models import Customer

CUST_CODE = 'CUST01'
JB_NAME = 'CUSTOMER 1'
PP_NAME = 'Customer 1 '


class TestCustomer(TransactionTestCase):
    def setUp(self):
        Customer.objects.create(
            customer=CUST_CODE,
            name=JB_NAME,
            last_updated=datetime.datetime.utcnow(),
            print_statement=False,
            accept_bo=False,
            send_report_by_email=False
        )

    def test_tokenize(self):
        self.assertEqual(['one', 'two', 'three'],
                         tokenize('One, Two, & Three'))

    def test_exact_name_match(self):
        self.assertIsNone(filter_exact_customer_name('bad name'))
        self.assertEqual(JB_NAME, filter_exact_customer_name(JB_NAME).name)

    def test_fuzzy_name_match(self):
        self.assertIsNone(filter_fuzzy_customer_name('bad name'))
        self.assertEqual(JB_NAME, filter_fuzzy_customer_name(PP_NAME).name)

    def test_code_mutation(self):
        self.assertEquals('CUST1', increment_code('CUST'))
        self.assertEquals('CUST2', increment_code('CUST1'))
        self.assertEquals('CUSTOMERA1', increment_code('CUSTOMERAB'))
        self.assertEquals('CUSTOMER10', increment_code('CUSTOMERA9'))
        self.assertEquals('Strange c1', increment_code('Strange case 13 '))

    def test_available_code(self):
        self.assertEqual('TEST', get_available_customer_code('test'))
        self.assertEqual('CUST2', get_available_customer_code(CUST_CODE))

    def test_customer_get_or_create(self):
        c = Customer.objects.count()
        customer = get_or_create_customer(PP_NAME)
        self.assertEqual(c, Customer.objects.count())
        self.assertEqual(JB_NAME, customer.name)
        customer = get_or_create_customer('Paperless')
        self.assertEqual(c+1, Customer.objects.count())
        self.assertEqual('PAPERLESS', customer.customer)
        self.assertEqual('Paperless', customer.name)
