#coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time



class Baidu_Menu(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.base_url = "http://www.baidu.com"
		self.verificationErrors = []
		self.accept_next_alert = True

	#def high_light(self, ele):
		#self.driver.execute_script("arguments[0].style.border = '2px solid red'", ele)

	def test_baidumenu(self):
		driver = self.driver
		driver.get(self.base_url+"/")
		driver.find_element_by_id('lb').click()
		time.sleep(3)
		driver.find_element_by_id('TANGRAM__PSP_8__userName').send_keys('13683607947')
		driver.find_element_by_id('TANGRAM__PSP_8__password').send_keys('123!vanceinfo')
		driver.find_element_by_name('memberPass').click()
		time.sleep(3)
		driver.find_element_by_id('TANGRAM__PSP_8__submit').submit()
		time.sleep(3)
		account = driver.find_element_by_partial_link_text("136")
		ActionChains(driver).move_to_element(account).perform()
		time.sleep(3)
		driver.find_element_by_class_name('sep').click()



	def tearDown(self):
		self.driver.quit()
		self.assertEqual(self.verificationErrors,[])

if __name__ == '__main__':
	unittest.main()
