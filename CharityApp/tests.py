from django.urls import resolve
from django.test import TestCase
from CharityApp.views import DonationForm

class DonationFormTest(TestCase):

	def test_root_url_resolves_to_donationfrom_views(self):
		found = resolve ('/')
		self.assertEqual(found.func, DonationForm)

# Create your tests here.
