from django.test import TestCase
from VApp.models import Item
#from django.urls import resolve
#from VApp.views import VolunteerForm

#from django.http import HttpRequest
#from django.template.loader import render_to_string


class VolunteerFormTest(TestCase):

	def test_VolunteerForm_returns_correct_view(self):
		response = self.client.get ('/')
		self.assertTemplateUsed(response,'volunteerform.html')


	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'Vinterest': 'vInterest'})
		self.assertIn('vInterest', response.content.decode())
		self.assertTemplateUsed(response, 'volunteerform.html')

 
	# def test_can_save_a_POST_request(self):
	# 	response = self.client.post('/', data={'Fname': 'firstName'})
	# 	self.assertIn('firstName', response.content.decode())
	# 	self.assertTemplateUsed(response, 'volunteerform.html')

class ORMTest(TestCase):
	def test_saving_and_retrieving_items(self):
		first_item = Item()
		first_item.text = 'Item one'
		first_item.save()
		second_item = Item()
		second_item.text = 'Item two'
		second_item.save()
		third_item = Item()
		third_item.text = 'Item three'
		third_item.save()
		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 3)
		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		third_saved_item = saved_items[2]
		self.assertEqual(first_saved_item.text, 'Item one')
		self.assertEqual(second_saved_item.text, 'Item two')
		self.assertEqual(third_saved_item.text, 'Item three')

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
