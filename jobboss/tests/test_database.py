import datetime
import uuid
from django.test import TransactionTestCase
from jobboss.models import Contact, AutoNumber, Job


class TestDatabase(TransactionTestCase):
    def test_database(self):
        # test we can create and connect to an empty test database
        self.assertEqual(0, Contact.objects.count())
        contact = Contact(last_updated=datetime.datetime.utcnow())
        contact.save()
        self.assertEqual(1, Contact.objects.count())

    def test_autonumber(self):
        AutoNumber.objects.create(type='Job', last_nbr='100',
                                  system_generated=True)
        job = Job(
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
        job.save_with_autonumber()
        self.assertEqual('101', job.job)
        job.type = 'B'
        job.save_with_autonumber()
        self.assertEqual('101', job.job)
        self.assertEqual('101', AutoNumber.objects.get(type='Job').last_nbr)
