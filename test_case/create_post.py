#coding=utf-8
import unittest
from selenium import webdriver
import time
from public import login #从public文件夹中引人login文件
from public import createpost

class WordPress_Add(unittest.TestCase):
	dr = None
	post_list_url = "http://127.0.0.1:8080/wordpress/wp-admin/edit.php"
	
	
	def setUp(self):
		self.dr = webdriver.Chrome()


	def test_login(self):
		"""登录用例"""
		login.login(self.dr) #调用login公用方法
		print self.dr.current_url
		self.assertTrue('wp-admin' in self.dr.current_url)
		print 'Login: success'

	def test_create_post(self):
		"""添加一个文章用例"""
		#调用login公用方法
		login.login(self.dr) #调用login公用方法
		title = createpost.create_post(self.dr)
		self.dr.get(self.post_list_url)
		post_list_table = self.dr.find_element_by_class_name('wp-list-table')
		self.assertTrue(title in post_list_table.text)
		print "AddPost: success"

	
	def tearDown(self):
		time.sleep(3)
		self.dr.quit()

if __name__ == '__main__':
	unittest.main()