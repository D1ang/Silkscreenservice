from django.test import TestCase


class TestIndex(TestCase):
    """
    Test to see if the main index page is working.
    """
    def test_get_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
