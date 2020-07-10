from django.test import TestCase
from django.contrib.auth.models import Group


class TestAdminGroup(TestCase):
    """
    Test to see if the admin group is available.
    """
    fixtures = ["groups.json"]

    def test_should_create_group(self):
        group = Group.objects.get(pk=1)
        self.assertEqual(group.name, "admin")


class TestCustomerGroup(TestCase):
    """
    Test to see if the customer group is available.
    """
    fixtures = ["groups.json"]

    def test_should_create_group(self):
        group = Group.objects.get(pk=2)
        self.assertEqual(group.name, "customer")
