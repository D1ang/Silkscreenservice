from django.test import TestCase
from accounts.forms import CustomerForm


class TestItemForm(TestCase):
    """
    Test to see if the company name is indeed required.
    """
    def test_company_name_is_required(self):
        form = CustomerForm({'company_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('company_name', form.errors.keys())
        self.assertEqual(form.errors['company_name']
                         [0], 'This field is required.')
