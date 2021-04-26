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

	def test_start_list_and_retrive_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('VOLUNTEER', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Be one of Us!', headerText)
		#info
		inputFName = self.browser.find_element_by_id('Fname')
		inputLName = self.browser.find_element_by_id('Lname')
		inputMAddress = self.browser.find_element_by_id('Maddress')
		inputCAddress = self.browser.find_element_by_id('Caddress')
		btnReg = self.browser.find_element_by_id('btnRegister')
		self.assertEqual(inputFName.get_attribute('placeholder'),'Your first name')
		self.assertEqual(inputLName.get_attribute('placeholder'),'Your last name')
		self.assertEqual(inputMAddress.get_attribute('placeholder'),'Municipality')
		self.assertEqual(inputCAddress.get_attribute('placeholder'),'City')
		btnReg.click() # to check if the required attribute in html is working
		time.sleep(2)
		inputFName.send_keys('danene')
		time.sleep(2)
		inputLName.send_keys('kyuti')
		time.sleep(2)
		inputMAddress.send_keys('Dasma')
		time.sleep(2)
		inputCAddress.send_keys('Cavite')
		time.sleep(2)
		btnReg.click()
		time.sleep(4)

		table = self.browser.find_element_by_id('info_list_table')

if __name__ == '__main__':
	unittest.main(warnings='ignore')


# browser = webdriver.Firefox()
# browser.get('http://127.0.0.1:8000')
