#coding=utf-8
from selenium import webdriver
import unittest,time
from public import login

class Search(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.base_url = "http://student.test.cuotiben.net.cn"
	def test_search(self):
		self.driver.get(self.base_url+'/')
		login.login(self.driver)
		#定位到当前元素所在iframe
		self.driver.switch_to_frame("main_iframe")
		self.driver.find_element_by_id('subject').find_element_by_xpath("//option[@value='42']").click()
		self.driver.find_element_by_id('request').find_element_by_xpath("//option[@value='1']").click()
		time.sleep(3)
		self.driver.find_element_by_id('u2').click()
		time.sleep(5)
		print 'upload self success'



	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()