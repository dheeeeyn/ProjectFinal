from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time

class VolunteerForm(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	# def tearDown(self):
	# 	self.browser.quit()

	# def test_browser_title(self):
	# 	self.browser.get('http://localhost:8000')
	# 	self.assertIn('VOLUNTEER', self.browser.title)
	# 	#self.fail('Finish the test noww')


	def check_rows_in_info_list_table(self, row_text):
		table = self.browser.find_element_by_id('v_info_list_table')
		rows = table.find_elements_by_tag_name('tr')	
		self.assertIn(row_text, [row.text for row in rows])

	# def check_rows_in_info_list_table(self, row_text):
	# 	table = self.browser.find_element_by_id('v_info_list_table')
	# 	rows = table.find_elements_by_tag_name('tr')
	# 	self.assertIn('1: danene kyuti lives at Dasma Cavite', [row.text for row in rows])	
	# 	self.assertIn(row_text, [row.test for row in rows])


	def test_start_list_and_retrive_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('VOLUNTEER', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Be one of Us!', headerText)
		#infor
		inputFName = self.browser.find_element_by_id('Fname')
		inputLName = self.browser.find_element_by_id('Lname')
		inputMAddress = self.browser.find_element_by_id('Maddress')
		inputCAddress = self.browser.find_element_by_id('Caddress')
		self.assertEqual(inputFName.get_attribute('placeholder'),'Your first name')
		self.assertEqual(inputLName.get_attribute('placeholder'),'Your last name')
		self.assertEqual(inputMAddress.get_attribute('placeholder'),'Municipality')
		self.assertEqual(inputCAddress.get_attribute('placeholder'),'City')
		inputFName.click()
		time.sleep(1)
		inputFName.send_keys('danene')
		time.sleep(1)
		inputLName.click()
		time.sleep(1)
		inputLName.send_keys('kyuti')
		time.sleep(1)
		inputMAddress.click()
		time.sleep(1)
		inputMAddress.send_keys('Dasma')
		time.sleep(1)
		inputCAddress.click()
		time.sleep(1)
		inputCAddress.send_keys('Cavite')
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
		time.sleep(1)
		inputInterest.send_keys('Event Organizer')
		time.sleep(1)
		inputschedD.click()
		time.sleep(1)
		inputschedD.send_keys('Monday')
		time.sleep(1)
		inputschedT.click()
		time.sleep(1)
		inputschedT.send_keys('First Shift')
		time.sleep(1)
		btnReg.click()
		time.sleep(2)
		#This page should update and show name on the list
		self.check_rows_in_info_list_table('1: Event Organizer Monday First Shift')
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
		inputschedD.send_keys('Wednesday')
		time.sleep(1)
		inputschedT.click()
		inputschedT.send_keys('Second Shift')
		btnReg.click()
		self.check_rows_in_info_list_table('2: Repacking Team Wednesday Second Shift')

		# table = self.browser.find_element_by_id('v_info_list_table')
		# rows = table.find_elements_by_tag_name('tr')
		# self.assertIn('Event organizer Monday First Shift', [row.text for row in rows])
		# self.assertIn('Repacking Team Sunday Second Shift', [row.text for row in rows])

		
if __name__ == '__main__':
	unittest.main(warnings='ignore')


# browser = webdriver.Firefox()
# browser.get('http://127.0.0.1:8000')
