from django.test import TestCase
from accounts.forms import CustomerForm


class TestCustomerForm(TestCase):
    """
    Tests the customer form if the required fields
    are actually required.
    """

    def test_required_fields(self):
        form = CustomerForm({
            'first_name': '',
            'last_name': '',
            'street_address': '',
            'country': '',
            'city': '',
            'postal': '',
            'email': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertIn('last_name', form.errors.keys())
        self.assertIn('street_address', form.errors.keys())
        self.assertIn('country', form.errors.keys())
        self.assertIn('city', form.errors.keys())
        self.assertIn('postal', form.errors.keys())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['first_name']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['last_name']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['street_address']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['country']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['city']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['postal']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['email']
                         [0], 'This field is required.')
