#coding=utf-8
from selenium import webdriver
import time,unittest

class collectKB(unittest.TestCase):
	def test_collect(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://passport.kuaibo.com/login/?referrer=http%3A%2F%2Fwebcloud.kuaibo.com%2F")
		self.driver.maximize_window() #浏览器最大化
		#登陆快播私有云
		self.driver.find_element_by_id("user_name").send_keys("testing360")
		self.driver.find_element_by_id("user_pwd").send_keys("198876")
		self.driver.find_element_by_id("dl_an_submit").click()
		time.sleep(3)
		#self.driver.find_element_by_xpath('//*[@class="guide-ok-btn"]').click()
		time.sleep(3)
		inputs=self.driver.find_elements_by_tag_name('input')
		n=0
		for i in inputs:
			if i.get_attribute('type')=="checkbox":
				n=n+1
		print "before number is %d" %n
		time.sleep(3)
		#收藏用户分享文件
		self.driver.find_element_by_class_name("collect").click()
		time.sleep(3)
		#再次获取当前文件的个数
		inputs=self.driver.find_elements_by_tag_name('input')
		ns=0
		for ii in inputs:
			if ii.get_attribute('type')=="checkbox":
				ns=ns+1
		print "after number is %d" %ns
		#判断执行收藏文件之后比收藏之间文件加1 ，否则抛异常
		try:
			self.assertEqual(ns,n+1,msg="add file failure!")
		except AssertionError,msg:
			print msg
		#退出
		self.driver.find_element_by_class_name("Usertool").click()
		time.sleep(2)
		self.driver.find_element_by_link_text("退出").click()
		time.sleep(2)
		self.driver.close()

if __name__ == "__main__":
	unittest.main()