import datetime
import uuid
from django.test import TransactionTestCase
from jobboss.query.job import shipping_option_summary, increment_job, \
    get_default_vendor, get_default_work_center, DEFAULT_VENDOR_NAME, \
    DEFAULT_WORK_CENTER_NAME, get_material
from jobboss.models import WorkCenter, Vendor, Material

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

    def test_get_material(self):
        Material.objects.create(
            material='123',
            rev='A',
            location_id='',
            type='F',
            status='Active',
            pick_buy_indicator='P',
            stocked_uofm='ea',
            purchase_uofm='ea',
            cost_uofm='ea',
            price_uofm='ea',
            standard_cost=0,
            reorder_qty=0,
            lead_days=0,
            uofm_conv_factor=1,
            lot_trace=False,
            rd_whole_unit=False,
            make_buy='M',
            use_price_breaks=True,
            last_updated=datetime.datetime.utcnow(),
            taxable=False,
            affects_schedule=True,
            tooling=False,
            isserialized=False,
            objectid=uuid.uuid4()
        )
        self.assertIsNotNone(get_material('123'))
        self.assertIsNotNone(get_material('123 '))
        self.assertIsNone(get_material('456'))
