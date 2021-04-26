#from django.urls import resolve
from django.test import TestCase
#from VApp.views import VolunteerForm

#from django.http import HttpRequest
#from django.template.loader import render_to_string


class VolunteerFormTest(TestCase):

	def test_VolunteerForm_returns_correct_view(self):
		response = self.client.get ('/')
		self.assertTemplateUsed(response,'volunteerform.html')

	# def test_root_url_resolves_to_volunteerfrom_views(self):
	# 	found = resolve ('/')
	# 	self.assertEqual(found.func, VolunteerForm)

	# def test_VolunteerForm_returns_correct_view(self):
	# 	request = HttpRequest()
	# 	response = VolunteerForm(request)
	# 	html = response.content.decode('utf8')
	# 	self.assertTrue(html.startswith('<html>'))
	# 	self.assertIn('<title>VOLUNTEER/title>', html)
	# 	self.assertTrue(html.endswith('</html>'))

	# def test_VolunteerForm_returns_correct_view(self):
	# 	request = HttpRequest()
	# 	response = VolunteerForm(request)
	# 	html = response.content.decode('utf8')
	# 	string_html = render_to_string('volunteerform.html')
	# 	self.assertEqual(html, string_html)

	# def test_VolunteerForm_returns_correct_view(self):
	# 	response = self.client.get ('/')
	# 	html = response.content.decode('utf8')
	# 	string_html = render_to_string('volunteerform.html')
	# 	self.assertEqual(html, string_html)
	# 	self.assertTemplateUsed(response,'volunteerform.html')

	# def test_VolunteerForm_returns_correct_view(self):
	# 	request = HttpRequest()
	# 	response = VolunteerForm(request)
	# 	html = response.content.decode('utf8')
	# 	string_html = render_to_string('volunteerform.html')
	# 	self.assertEqual(html, string_html)



# Create your tests here.
