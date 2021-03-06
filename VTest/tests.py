from selenium import webdriver
#import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException


ANTAY = 3
class VolunteerForm(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def antay_rows_in_info_list_table(self, row_text):
		start_time = time.time()
		while time.time()-start_time < ANTAY:
			time.sleep(0.5)
		try:
			table = self.browser.find_element_by_id('v_info_list_table')
			rows = table.find_elements_by_tag_name('tr')	
			self.assertIn(row_text, [row.text for row in rows])
			return
		except(AssertionError,WebDriverException) as e:
			if time.time()-start_time > ANTAY:
		 		raise e
	
		# table = self.browser.find_element_by_id('v_info_list_table')
		# rows = table.find_elements_by_tag_name('tr')	
		# self.assertIn(row_text, [row.text for row in rows])

	def test_start_user_one(self):
		#self.browser.get('http://localhost:8000')
		self.browser.get(self.live_server_url)
		self.assertIn('VOLUNTEER', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Project Malasakit', headerText)
		headerText_2 = self.browser.find_element_by_tag_name('h3').text
		self.assertIn('Be One of Us !', headerText_2)
		#infor
		inputFName = self.browser.find_element_by_id('Fname')
		inputLName = self.browser.find_element_by_id('Lname')
		inputFAddress = self.browser.find_element_by_id('Faddress')
		inputAage = self.browser.find_element_by_id('Age')
		inputCNumber = self.browser.find_element_by_id('Cnumber')
		self.assertEqual(inputFName.get_attribute('placeholder'),'Your first name')
		self.assertEqual(inputLName.get_attribute('placeholder'),'Your last name')
		self.assertEqual(inputFAddress.get_attribute('placeholder'),'Your Municipality and Province')
		self.assertEqual(inputAage.get_attribute('placeholder'),'Your age')
		self.assertEqual(inputCNumber.get_attribute('placeholder'),'09xx-xxx-xxx')
		inputFName.click()
		inputFName.send_keys('danene')
		time.sleep(1)
		inputLName.click()
		inputLName.send_keys('kyuti')
		time.sleep(1)
		inputFAddress.click()
		inputFAddress.send_keys('Dasma, Cavite')
		time.sleep(1)
		inputAage.click()
		inputAage.send_keys('22')
		time.sleep(1)
		inputCNumber.click()
		inputCNumber.send_keys('0912-123-4567')
		time.sleep(1)
		#Vinfo
		inputInterest = self.browser.find_element_by_id('Vinterest')
		inputschedD = self.browser.find_element_by_id('Dsched')
		inputschedT = self.browser.find_element_by_id('Tsched')
		self.assertEqual(inputInterest.get_attribute('placeholder'),'(Ex. Event Organizer, Repacking Team, Researcher)')
		self.assertEqual(inputschedD.get_attribute('placeholder'),'(Monday, Wednesday, Friday, Sunday ONLY)')
		self.assertEqual(inputschedT.get_attribute('placeholder'),'First Shift(7:00 am - 11:00 pm)/ Second Shift(1:00 pm- 5:00 pm)')
		btnReg = self.browser.find_element_by_id('btnRegister')
		inputInterest.click()
		inputInterest.send_keys('Event Organizer')
		time.sleep(1)
		inputschedD.click()
		inputschedD.send_keys('Monday')
		time.sleep(1)
		inputschedT.click()
		inputschedT.send_keys('First Shift')
		time.sleep(1)
		btnReg.click()
		self.antay_rows_in_info_list_table('1: Event Organizer Monday First Shift')


		#This page should update and show name on the list
		#Vinfo2
		inputInterest = self.browser.find_element_by_id('Vinterest')
		inputschedD = self.browser.find_element_by_id('Dsched')
		inputschedT = self.browser.find_element_by_id('Tsched')
		self.assertEqual(inputInterest.get_attribute('placeholder'),'(Ex. Event Organizer, Repacking Team, Researcher)')
		self.assertEqual(inputschedD.get_attribute('placeholder'),'(Monday, Wednesday, Friday, Sunday ONLY)')
		self.assertEqual(inputschedT.get_attribute('placeholder'),'First Shift(7:00 am - 11:00 pm)/ Second Shift(1:00 pm- 5:00 pm)')
		btnReg = self.browser.find_element_by_id('btnRegister')
		inputInterest.click()
		inputInterest.send_keys('Repacking Team')
		time.sleep(1)
		inputschedD.click()
		inputschedD.send_keys('Friday')
		time.sleep(1)
		inputschedT.click()
		inputschedT.send_keys('Second Shift')
		time.sleep(1)
		btnReg.click()
		self.antay_rows_in_info_list_table('2: Repacking Team Friday Second Shift')

	def test_multiple_users_with_different_urls(self):
		self.browser.get(self.live_server_url)
		#Vinfo
		inputInterest = self.browser.find_element_by_id('Vinterest')
		inputschedD = self.browser.find_element_by_id('Dsched')
		inputschedT = self.browser.find_element_by_id('Tsched')
		self.assertEqual(inputInterest.get_attribute('placeholder'),'(Ex. Event Organizer, Repacking Team, Researcher)')
		self.assertEqual(inputschedD.get_attribute('placeholder'),'(Monday, Wednesday, Friday, Sunday ONLY)')
		self.assertEqual(inputschedT.get_attribute('placeholder'),'First Shift(7:00 am - 11:00 pm)/ Second Shift(1:00 pm- 5:00 pm)')
		btnReg = self.browser.find_element_by_id('btnRegister')
		inputInterest.click()
		inputInterest.send_keys('Documentation Team')
		time.sleep(1)
		inputschedD.click()
		inputschedD.send_keys('Sunday')
		time.sleep(1)
		inputschedT.click()
		inputschedT.send_keys('Second Shift')
		time.sleep(1)
		btnReg.click()
		self.antay_rows_in_info_list_table('1: Documentation Team Sunday Second Shift')
		viewList_url = self.browser.current_url
		self.assertRegex(viewList_url, '/VApp/.+')

		self.browser.quit()
		self.browser = webdriver.Firefox()
		self.browser.get(self.live_server_url)
		htmlBody = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Documentation Team Sunday Second Shift',htmlBody)
		time.sleep(1)
		#Vinfo
		inputInterest = self.browser.find_element_by_id('Vinterest')
		inputInterest.click()
		inputInterest.send_keys('Event Organizer Team')
		time.sleep(1)
		inputschedD = self.browser.find_element_by_id('Dsched')
		time.sleep(1)
		inputschedD.click()
		inputschedD.send_keys('Sunday')
		inputschedT = self.browser.find_element_by_id('Tsched')
		time.sleep(1)
		inputschedT.click()
		inputschedT.send_keys('Second Shift')
		time.sleep(1)
		btnReg = self.browser.find_element_by_id('btnRegister')
		btnReg.click()
		self.antay_rows_in_info_list_table('1: Event Organizer Team Sunday Second Shift')
		user2_url = self.browser.current_url
		self.assertRegex(user2_url, 'VApp/.+')
		self.assertNotEqual(viewList_url, user2_url)
		htmlBody = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Documentation Team Sunday Second Shift',htmlBody)
		self.assertIn('1: Event Organizer Team Sunday Second Shift',htmlBody)




		
# if __name__ == '__main__':
# 	unittest.main(warnings='ignore')


# browser = webdriver.Firefox()
# browser.get('http://127.0.0.1:8000')
	# table = self.browser.find_element_by_id('v_info_list_table')
		# rows = table.find_elements_by_tag_name('tr')
		# self.assertIn('Event organizer Monday First Shift', [row.text for row in rows])
		# self.assertIn('Repacking Team Sunday Second Shift', [row.text for row in rows])


	# def check_rows_in_info_list_table(self, row_text):
	# 	table = self.browser.find_element_by_id('v_info_list_table')
	# 	rows = table.find_elements_by_tag_name('tr')
	# 	self.assertIn('1: danene kyuti lives at Dasma Cavite', [row.text for row in rows])	
	# 	self.assertIn(row_text, [row.test for row in rows])


	# def tearDown(self):
	# 	self.browser.quit()

	# def test_browser_title(self):
	# 	self.browser.get('http://localhost:8000')
	# 	self.assertIn('VOLUNTEER', self.browser.title)
	# 	self.fail('Finish the test noww')
