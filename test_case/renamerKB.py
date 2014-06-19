#coding=utf-8
from selenium import webdriver
import time,unittest

class renameKB(unittest.TestCase):
	def test_rename(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://passport.kuaibo.com/login/?referrer=http%3A%2F%2Fwebcloud.kuaibo.com%2F")
		self.driver.maximize_window() #浏览器最大化
		#登陆快播私有云
		self.driver.find_element_by_id("user_name").send_keys("testing360")
		self.driver.find_element_by_id("user_pwd").send_keys("198876")
		self.driver.find_element_by_id("dl_an_submit").click()
		self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[4]/table/tbody[8]/tr/td/input').click()
		
if __name__=='__main__':
	unittest.main()