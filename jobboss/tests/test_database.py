import datetime
import unittest
from jobboss.models import Contact


class TestDatabase(unittest.TestCase):
    def test_database(self):
        # test we can create and connect to an empty test database
        self.assertEqual(0, Contact.objects.count())
        contact = Contact(last_updated=datetime.datetime.utcnow())
        contact.save()
        self.assertEqual(1, Contact.objects.count())
