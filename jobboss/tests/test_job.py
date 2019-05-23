import uuid
import datetime
from django.test import TransactionTestCase
from jobboss.query.job import shipping_option_summary, increment_job, \
    get_default_vendor, get_default_work_center, DEFAULT_VENDOR_NAME, \
    DEFAULT_WORK_CENTER_NAME, create_delivery
from jobboss.models import WorkCenter, Vendor

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

    def test_increment_job(self):
        self.assertEqual('123-1a', increment_job('123-1'))
        self.assertEqual('123-1b', increment_job('123-1a'))

    def test_default_wc(self):
        c = WorkCenter.objects.count()
        wc = get_default_work_center()
        self.assertEqual(DEFAULT_WORK_CENTER_NAME, wc.work_center)
        self.assertEqual(c + 1, WorkCenter.objects.count())
        wc = get_default_work_center()
        self.assertEqual(DEFAULT_WORK_CENTER_NAME, wc.work_center)
        self.assertEqual(c + 1, WorkCenter.objects.count())

    def test_default_vendor(self):
        c = Vendor.objects.count()
        v = get_default_vendor()
        self.assertEqual(DEFAULT_VENDOR_NAME, v.vendor)
        self.assertEqual(c + 1, Vendor.objects.count())
        v = get_default_vendor()
        self.assertEqual(DEFAULT_VENDOR_NAME, v.vendor)
        self.assertEqual(c + 1, Vendor.objects.count())

    def test_delivery(self):
        now = datetime.datetime.now()
        d1 = create_delivery(objectid=uuid.uuid4(),
                             promised_date=now,
                             promised_quantity=1,
                             last_updated=now)
        self.assertEqual(1, d1.delivery)
        d2 = create_delivery(objectid=uuid.uuid4(),
                             promised_date=now,
                             promised_quantity=1,
                             last_updated=now)
        self.assertEqual(2, d2.delivery)
