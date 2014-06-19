#coding=utf-8
from selenium import webdriver
import time,unittest

class loginKB(unittest.TestCase):
	def test_login(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://passport.kuaibo.com/login/?referrer=http%3A%2F%2Fwebcloud.kuaibo.com%2F")
		self.driver.maximize_window() #浏览器最大化
		#登陆快播私有云
		self.driver.find_element_by_id("user_name").send_keys("testing360")
		self.driver.find_element_by_id("user_pwd").send_keys("198876")
		self.driver.find_element_by_id("dl_an_submit").click()
		time.sleep(3)
		self.driver.find_element_by_xpath('//div[@class="wdg"]').find_element_by_class_name('guide-ok-btn').click()
		time.sleep(3)
		#获取用户名
		now_user=self.driver.find_element_by_xpath("//div[@id='Nav']/ul/li[4]/a[1]/span").text
		#用户名是否等于虫师，不等于将抛出异常
		try:
			self.assertEqual(u"小二账号", now_user, msg='assert failed')
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