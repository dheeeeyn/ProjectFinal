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


	# def test_only_saves_items_kapag_kailangan(self):
	# 	self.client.get('/')
	# 	self.assertEqual(Item.objects.count(), 0)

	# def test_save_a_POST_request(self):
	# 	response = self.client.post('/', data={'Vinterest': 'vInterest'})
	# 	# self.assertIn('vInterest', response.content.decode())
	# 	# self.assertTemplateUsed(response, 'volunteerform.html')

	# 	self.assertEqual(Item.objects.count(), 1)
	# 	newItem = Item.objects.first()
	# 	self.assertEqual(newItem.text, 'vInterest')
	
	# def test_redirects_POST(self):
	# 	response = self.client.post('/', data={'Vinterest': 'vInterest'})
	# 	self.assertEqual(response.status_code, 302)
	# 	#self.assertEqual(response['location'], '/')
	# 	self.assertEqual(response['location'], '/VApp/viewList_url/')

	# def test_template_display_input_item(self):
	# 	Item.objects.create(text='input item 1')
	# 	Item.objects.create(text='input item 2')
	# 	response = self.client.get('/')
	# 	self.assertIn('input item 1', response.content.decode())
	# 	self.assertIn('input item 2', response.content.decode())

class ORMTest(TestCase):
	def test_saving_and_retrieving_input_item(self):
		first_item = Item()
		first_item.text = 'Item one'
		first_item.save()
		second_item = Item()
		second_item.text = 'Item two'
		second_item.save()
		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)
		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'Item one')
		self.assertEqual(second_saved_item.text, 'Item two')

class ListViewTest(TestCase):
	def test_uses_list_template_template(self):
		response = self.client.get('/VApp/viewList_url/')
		self.assertTemplateUsed(response,'volunteerinfo.html')

	def test_displays_all_items(self):
		Item.objects.create(text ='milleth kulet')
		Item.objects.create(text='maggie sungit')
		response = self.client.get('/VApp/viewList_url/')
		self.assertContains(response, 'milleth kulet')
		self.assertContains(response, 'maggie sungit')


class New_List_Test(TestCase):
	def test_save_a_POST_request(self):
		response = self.client.post('/VApp/newList_url', data={'Vinterest': 'vInterest'})
		# self.assertIn('vInterest', response.content.decode())
		# self.assertTemplateUsed(response, 'volunteerform.html')

		self.assertEqual(Item.objects.count(), 1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'vInterest')
	
	def test_redirects_POST(self):
		response = self.client.post('/VApp/newList_url', data={'Vinterest': 'vInterest'})
		self.assertRedirects(response, '/VApp/viewList_url/')

		# self.assertEqual(response.status_code, 302)
		# #self.assertEqual(response['location'], '/')
		# self.assertEqual(response['location'], '/VApp/viewList_url/')



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
