from django.test import TestCase
from VApp.models import Item, Volunteer
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
		newVolunteer = Volunteer()
		newVolunteer.save()
		first_item = Item()
		first_item.VolId = newVolunteer
		first_item.text = 'Item one'
		first_item.Sched = 'Sched1'
		first_item.schedT = 'TSched1'
		first_item.save()

		second_item = Item()
		second_item.VolId = newVolunteer
		second_item.text = 'Item two'
		second_item.Sched = 'Sched2'
		second_item.schedT = 'TSched2'
		second_item.save()

		saved_items = Item.objects.all()
		savedVolunteer = Volunteer.objects.first()
		self.assertEqual(saved_items.count(), 2)
		#self.assertEqual(savedVolunteer,newVolunteer)
		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'Item one')
		self.assertEqual(second_saved_item.text, 'Item two')
		self.assertEqual(first_saved_item.Sched, 'Sched1')
		self.assertEqual(second_saved_item.Sched, 'Sched2')
		self.assertEqual(first_saved_item.schedT, 'TSched1')
		self.assertEqual(second_saved_item.schedT, 'TSched2')
		self.assertEqual(first_saved_item.VolId, newVolunteer)
		self.assertEqual(second_saved_item.VolId, newVolunteer)
		

class ListViewTest(TestCase):

	def test_displays_all_items(self):
		newVolunteer = Volunteer.objects.create()
		Item.objects.create(VolId=newVolunteer, text ='milleth kulet')
		Item.objects.create(VolId=newVolunteer,text='maggie sungit')
		response = self.client.get(f'/VApp/{newVolunteer.id}/')
		self.assertContains(response, 'milleth kulet')
		self.assertContains(response, 'maggie sungit')
		self.assertNotContains(response, 'Rica Pretty')
		self.assertNotContains(response, 'Danielle Kyuti')

		newVolunteer_2 = Volunteer.objects.create()
		Item.objects.create(VolId=newVolunteer_2, text ='Rica Pretty')
		Item.objects.create(VolId=newVolunteer_2, text='Danielle Kyuti')
		response = self.client.get(f'/VApp/{newVolunteer_2.id}/')
		self.assertContains(response, 'Rica Pretty')
		self.assertContains(response, 'Danielle Kyuti')
		self.assertNotContains(response, 'milleth kulet')
		self.assertNotContains(response, 'maggie sungit')
		
	def test_uses_list_v_info_template(self):
		newVolunteer = Volunteer.objects.create()
		response = self.client.get(f'/VApp/{newVolunteer.id}/')
		self.assertTemplateUsed(response,'volunteerinfo.html')

	def test_pass_v_info_to_template(self):
	 	VolDummy1 = Volunteer.objects.create()
	 	VolDummy2 = Volunteer.objects.create()
	 	passVinfo = Volunteer.objects.create()
	 	response = self.client.get(f'/VApp/{passVinfo.id}/')
	 	self.assertEqual(response.context['vId'], passVinfo) 


class New_List_Test(TestCase):
	def test_save_a_POST_request(self):
		response = self.client.post('/VApp/newList_url', data={'Vinterest': 'vInterest', 'Dsched':'Sched', 'Tsched':'schedT'})
		# self.assertIn('vInterest', response.content.decode())
		# self.assertTemplateUsed(response, 'volunteerform.html')

		self.assertEqual(Item.objects.count(), 1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'vInterest')
		self.assertEqual(newItem.Sched, 'Sched')
		self.assertEqual(newItem.schedT, 'schedT')
	
	def test_redirects_POST(self):
		response = self.client.post('/VApp/newList_url', data={'Vinterest': 'vInterest','Dsched':'Sched', 'Tsched':'schedT'})
		newList = Volunteer.objects.first()
		self.assertRedirects(response,f'/VApp/{newList.id}/')

		# self.assertEqual(response.status_code, 302)
		# #self.assertEqual(response['location'], '/')
		# self.assertEqual(response['location'], '/VApp/viewList_url/')


class Add_New_Volunteer_Test(TestCase):


	def test_another_post_existing(self):
		VolDummy1 = Volunteer.objects.create()
		VolDummy2 = Volunteer.objects.create()
		existingVol = Volunteer.objects.create()
		self.client.post(f'/VApp/{existingVol.id}/addItem', data={'Vinterest': 'vInterest', 'Dsched':'Sched', 'Tsched':'schedT'})
		self.assertEqual(Item.objects.count(),1)
		newItem =Item.objects.first()
		self.assertEqual(newItem.text,'vInterest')
		self.assertEqual(newItem.Sched,'Sched')
		self.assertEqual(newItem.schedT, 'schedT')
		self.assertEqual(newItem.VolId, existingVol)
		

	def test_redirects_to_vol_view(self):
		VolDummy1 = Volunteer.objects.create()
		VolDummy2 = Volunteer.objects.create()
		VolDummy3 = Volunteer.objects.create()
		existingVol = Volunteer.objects.create()
		response = self.client.post(f'/VApp/{existingVol.id}/addItem', data={'Vinterest': 'vInterest', 'Dsched':'Sched','Tsched':'schedT'})
		self.assertRedirects(response, f'/VApp/{existingVol.id}/')









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
