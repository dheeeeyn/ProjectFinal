from selenium import webdriver
import unittest

class DonationForm(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()


	def tearDown(self):
		self.browser.quit()

	def test_browser_title(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Donation Form', self.browser.title)
		self.fail('Finish the test noww')

if __name__ == '__main__':
	unittest.main(warnings='ignore')


# browser = webdriver.Firefox()
# browser.get('http://127.0.0.1:8000')
