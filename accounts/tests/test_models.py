from django.test import TestCase
from accounts.models import Customer


class TestModels(TestCase):

    def test_customer_create(self):
        customer = Customer.objects.create(company_name='Test company')
        self.assertTrue(customer.company_name)
