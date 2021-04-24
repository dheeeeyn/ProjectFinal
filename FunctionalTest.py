from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time

class DonationForm(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	# def tearDown(self):
	# 	self.browser.quit()

	# def test_browser_title(self):
	# 	self.browser.get('http://localhost:8000')
	# 	self.assertIn('Donation Form', self.browser.title)
	# 	#self.fail('Finish the test noww')

	def test_start_list_and_retrive_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Donation Form', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		headerText2 = self.browser.find_element_by_tag_name('h3').text
		paragraph = self.browser.find_element_by_id("p1").text
		paragraph2 = self.browser.find_element_by_id("p2").text
		headerText3 = self.browser.find_element_by_tag_name('h2').text
		headerText4 = self.browser.find_element_by_id("hA").text
		self.assertIn('Project Malasakit', headerText)
		self.assertIn('Make Donations Now', headerText2) 
		self.assertIn('Raised', paragraph)
		self.assertIn('Goal', paragraph2) 
		self.assertIn('Donation Form', headerText3)
		self.assertIn('Amount', headerText4)
		#Amount
		btnAmount = self.browser.find_element_by_id('1000')
		#Contact
		inputName = self.browser.find_element_by_id('name')
		inputEmail = self.browser.find_element_by_id('email')
		inputMessage = self.browser.find_element_by_id('message')
		btnSubmit = self.browser.find_element_by_id('btnDonate')
		self.assertEqual(inputName.get_attribute('placeholder'),'Your name..')
		self.assertEqual(inputEmail.get_attribute('placeholder'),'input valid email..')
		self.assertEqual(inputMessage.get_attribute('placeholder'),'Write something... (optional)')
		btnSubmit.click() # to check if the required attribute in html is working
		self.assertEqual(btnAmount.get_attribute('value'),'1000')
		time.sleep(3)
		btnAmount.click()
		time.sleep(3)
		inputName.send_keys('danene')
		time.sleep(2)
		inputEmail.send_keys('danene@gmail.com')
		time.sleep(2)
		inputMessage.send_keys('PAPASA AKO SA WEBDEV2')
		time.sleep(2)
		btnSubmit.click()
		time.sleep(2)

if __name__ == '__main__':
	unittest.main(warnings='ignore')


# browser = webdriver.Firefox()
# browser.get('http://127.0.0.1:8000')
