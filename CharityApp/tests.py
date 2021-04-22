from django.urls import resolve
from django.test import TestCase
from CharityApp.views import DonationForm

from django.http import HttpRequest

class DonationFormTest(TestCase):

	def test_root_url_resolves_to_donationfrom_views(self):
		found = resolve ('/')
		self.assertEqual(found.func, DonationForm)

	def test_donationform_returns_correct_view(self):
		request = HttpRequest()
		response = DonationForm(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>Donation Form</title>', html)
		self.assertTrue(html.endswith('</html>'))


# Create your tests here.
