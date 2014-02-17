#coding=utf-8
from selenium import webdriver
import unittest

class PrintNews(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
        self.base_url = "http://sports.qq.com/seriea/"

	def test_printnews(self):
		self.driver.get(self.base_url)
    	tag_lis = self.driver.find_elements_by_xpath("//div[@id='inter']/div[2]/div/ul")
    	print tag_lis
    	for tag_li in lis:
    		tag_li.click()

	def tearDown(self):
		self.driver.quit()



if __name__ == "__main__":
    unittest.main()
