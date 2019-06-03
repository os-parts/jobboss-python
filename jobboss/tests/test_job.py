import uuid
import datetime
from django.test import TransactionTestCase
from jobboss.query.job import shipping_option_summary, increment_job, \
    get_default_vendor, get_default_work_center, DEFAULT_VENDOR_NAME, \
    DEFAULT_WORK_CENTER_NAME, create_delivery, create_material_req
from jobboss.models import WorkCenter, Vendor, Job, MaterialReq

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

    def test_mat_req(self):
        job = Job(
            job='1',
            type='A', order_date=datetime.datetime.utcnow(), status='A',
            status_date=datetime.datetime.utcnow(), build_to_stock=0,
            order_quantity=0, make_quantity=0, in_production_quantity=0,
            certs_required=False, time_and_materials=False, scrap_pct=0,
            currency_conv_rate=0, fixed_rate=False, labor_markup_pct=0,
            mat_markup_pct=0, serv_markup_pct=0, labor_burden_markup_pct=0,
            machine_burden_markup_pct=0, ga_burden_markup_pct=0,
            split_to_job=False, last_updated=datetime.datetime.utcnow(),
            objectid=uuid.uuid4(), commissionincluded=False
        )
        job.save()
        now = datetime.datetime.now()
        m1 = create_material_req(
            job=job,
            material='ALUMINUM_SHEET',
            pick_buy_indicator='B',
            type='M',
            uofm='lb',
            deferred_qty=0,
            currency_conv_rate=0,
            fixed_rate=True,
            certs_required=False,
            manual_link=False,
            last_updated=now,
            partial_res=False,
            objectid=uuid.uuid4(),
            job_oid=job.objectid,
            rounded=False)
        self.assertEqual(1, m1.material_req)
