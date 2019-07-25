import datetime
from django.test import TransactionTestCase
from jobboss.query.customer import tokenize, filter_exact_customer_name, \
    filter_fuzzy_customer_name, increment_code, get_available_customer_code, \
    get_or_create_customer, get_or_create_contact, match_address, \
    get_available_address_code, get_or_create_address, \
    get_address_types_by_customer, address_tokenize
from jobboss.models import Customer, Contact, Address

CUST_CODE = 'CUST01'
JB_NAME = 'CUSTOMER 1'
PP_NAME = 'Customer 1 '
JB_CONTACT_NAME = 'JOHN SMITH'
PP_CONTACT_NAME = 'John Smith'
ADDR_DICT = {
    'business_name': 'Customer 1',
    'city': 'Washington',
    'country': 'USA',
    'first_name': 'John',
    'last_name': 'Smith',
    'address1': '1600 Penn Ave',
    'address2': None,
    'phone': None,
    'phone_ext': None,
    'postal_code': '20500',
    'state': 'DC'
}


class TestCustomer(TransactionTestCase):
    def setUp(self):
        customer = Customer.objects.create(
            customer=CUST_CODE,
            name=JB_NAME,
            last_updated=datetime.datetime.utcnow(),
            print_statement=False,
            accept_bo=False,
            send_report_by_email=False
        )
        Contact.objects.create(
            customer=CUST_CODE,
            contact_name=JB_CONTACT_NAME,
            last_updated=datetime.datetime.utcnow()
        )
        Address.objects.create(
            customer=customer,
            status='Active',
            type='000',
            ship_to_id='SHIP',
            line1=ADDR_DICT['address1'].upper(),
            line2=ADDR_DICT['address2'],
            city=ADDR_DICT['city'].upper(),
            state=ADDR_DICT['state'].upper(),
            zip=ADDR_DICT['postal_code'],
            name='{} {}'.format(ADDR_DICT['first_name'],
                                ADDR_DICT['last_name']).upper(),
            country='US',
            phone=ADDR_DICT['phone'],
            lead_days=0,
            last_updated=datetime.datetime.utcnow(),
            billable=False,
            shippable=True
        )

    def test_tokenize(self):
        self.assertEqual(['one', 'two', 'three'],
                         tokenize('One, Two, & Three'))
        self.assertEqual(['one', 'two', 'three', 'four'],
                         tokenize('One, Two, & Three, Inc. d/b/a Four'))
        self.assertEqual(['inc'], tokenize('Inc.'))

    def test_exact_name_match(self):
        self.assertIsNone(filter_exact_customer_name('bad name'))
        self.assertEqual(JB_NAME, filter_exact_customer_name(JB_NAME).name)

    def test_fuzzy_name_match(self):
        self.assertIsNone(filter_fuzzy_customer_name('bad name'))
        self.assertEqual(JB_NAME, filter_fuzzy_customer_name(PP_NAME).name)
        self.assertEqual(JB_NAME, filter_fuzzy_customer_name(
            PP_NAME + ', Inc.').name)
        self.assertIsNone(filter_fuzzy_customer_name('1 customer'))

    def test_code_mutation(self):
        self.assertEquals('CUST1', increment_code('CUST'))
        self.assertEquals('CUST2', increment_code('CUST1'))
        self.assertEquals('CUSTOMERA1', increment_code('CUSTOMERAB'))
        self.assertEquals('CUSTOMER10', increment_code('CUSTOMERA9'))
        self.assertEquals('Strange c1', increment_code('Strange case 13 '))
        self.assertEquals('ABCDE1', increment_code('ABCDEF', 6))
        self.assertEquals('ABCDE2', increment_code('ABCDE1', 6))

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

    def test_contact_get_or_create(self):
        customer = Customer.objects.first()
        c = Contact.objects.count()
        contact = get_or_create_contact(customer, PP_CONTACT_NAME)
        self.assertEqual(c, Contact.objects.count())
        self.assertEqual(contact.contact_name, JB_CONTACT_NAME)
        contact = get_or_create_contact(customer, 'Jane Smith')
        self.assertEqual(c+1, Contact.objects.count())
        self.assertEqual(contact.contact_name, 'Jane Smith')
        self.assertEqual(CUST_CODE, contact.customer)
        self.assertGreater(contact.contact, 0)

    def test_match_address(self):
        customer = Customer.objects.first()
        address = match_address(customer, ADDR_DICT)
        self.assertEqual(ADDR_DICT['address1'].upper(), address.line1)
        d = ADDR_DICT.copy()
        d['address1'] = '1600 Pennsylvania Ave NW'  # not a match
        self.assertIsNone(match_address(customer, d))

        # try some fuzzier cases
        d = ADDR_DICT.copy()
        d['address1'] = '1600 Penn Avenue'
        d['phone'] = '123-456-7890'
        d['postal_code'] = '20500-1234'
        address = match_address(customer, d)
        self.assertIsNotNone(address)
        d = ADDR_DICT.copy()
        d['postal_code'] = '20501-1234'
        address = match_address(customer, d)
        self.assertIsNone(address)
        d = ADDR_DICT.copy()
        d['postal_code'] = '20501'
        address = match_address(customer, d)
        self.assertIsNone(address)

    def test_address_code(self):
        customer = Customer.objects.first()
        self.assertEqual('BILL',
                         get_available_address_code(customer, ship=False))
        self.assertEqual('SHIP1',
                         get_available_address_code(customer, ship=True))

    def test_address_get_or_create(self):
        customer = Customer.objects.first()
        c = Address.objects.count()
        address = get_or_create_address(customer, ADDR_DICT, True)
        self.assertEqual(c, Address.objects.count())
        self.assertEqual(ADDR_DICT['address1'].upper(), address.line1)
        self.assertFalse(address.billable)
        self.assertEqual('001', address.type)  # set to default shipping
        address = get_or_create_address(customer, ADDR_DICT, False)
        self.assertTrue(address.billable)
        self.assertEqual('011', address.type)  # set to default billing
        d = ADDR_DICT.copy()
        d['address1'] = '1600 Pennsylvania Ave NW'  # not a match
        address = get_or_create_address(customer, d, True)
        self.assertEqual(c+1, Address.objects.count())
        self.assertTrue(address.shippable)
        self.assertFalse(address.billable)
        self.assertTrue(address.ship_to_id.startswith('SHIP'))
        self.assertEqual('100', address.type)

    def test_address_types(self):
        customer = Customer.objects.first()
        m, b, s = get_address_types_by_customer(customer)
        self.assertFalse(m)
        self.assertFalse(b)
        self.assertFalse(s)

        customer = Customer.objects.create(
            customer='CUST02',
            name='CUSTOMER 2',
            last_updated=datetime.datetime.utcnow(),
            print_statement=False,
            accept_bo=False,
            send_report_by_email=False
        )
        # add addresses to this customer until they have all address types
        for type_str, type_tuple in [
            ('000', (False, False, False)),
            ('100', (True, False, False)),
            ('010', (True, True, False)),
            ('001', (True, True, True)),
        ]:
            Address.objects.create(
                customer=customer,
                status='Active',
                type=type_str,
                ship_to_id='SHIP',
                line1=ADDR_DICT['address1'].upper(),
                line2=ADDR_DICT['address2'],
                city=ADDR_DICT['city'].upper(),
                state=ADDR_DICT['state'].upper(),
                zip=ADDR_DICT['postal_code'],
                name='{} {}'.format(ADDR_DICT['first_name'],
                                    ADDR_DICT['last_name']).upper(),
                country='US',
                phone=ADDR_DICT['phone'],
                lead_days=0,
                last_updated=datetime.datetime.utcnow(),
                billable=False,
                shippable=True
            )
            self.assertEqual(type_tuple,
                             get_address_types_by_customer(customer))

    def test_address_tokenize(self):
        self.assertEqual(['123', 'main', 'st'],
                         address_tokenize('123 Main Street'))
        self.assertEqual(['123', 'main', 'st'],
                         address_tokenize('123 Main St.'))
