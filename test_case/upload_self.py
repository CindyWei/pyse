#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time
from public import login,upload_self

class Upload1(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.base_url = "http://student.test.cuotiben.net.cn"


	def test_upload1(self):
		#打开首页
		self.driver.get(self.base_url + "/")
		#登录
		login.login(self.driver)
		print self.driver.current_url
		self.assertTrue('student' in self.driver.current_url)
		print 'Login success'
		#点击上传错题导航按钮
		self.driver.find_element_by_id('mi_tab_uploadpage').click()
		#定位到当前元素所在iframe
		self.driver.switch_to_frame("main_iframe")
		time.sleep(3)
		upload_self.upload_self(self.driver)
		#检查是否回到列表页
		self.driver.find_element_by_id('u2')
		print 'upload self success'


   	def tearDown(self):
   		self.driver.quit()

if __name__ == "__main__":
    unittest.main()