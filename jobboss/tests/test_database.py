import datetime
import os
from tempfile import NamedTemporaryFile
import uuid
from django.test import TransactionTestCase
from jobboss.models import Contact, AutoNumber, Job, Account
from jobboss.export import export_table


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

    def test_autoincrement(self):
        Contact.objects.create(
            contact=10,
            last_updated=datetime.datetime.utcnow()
        )
        contact = Contact(
            last_updated=datetime.datetime.utcnow()
        )
        contact.save_with_autonumber()
        self.assertEqual(11, contact.contact)

    def test_export_table(self):
        Account.objects.create(
            account='TEST',
            type='Asset',
            last_updated=datetime.datetime.now()
        )
        f = NamedTemporaryFile()
        path = f.name
        f.close()
        export_table(Account, path)
        with open(path, 'r') as f:
            lines = f.readlines()
        os.remove(path)
        self.assertEqual(2, len(lines))
