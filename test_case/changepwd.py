#coding=utf-8
from public import login
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time

class classManage1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://student.test.cuotiben.net.cn"


    def test_gonggao(self):
        self.driver.get(self.base_url+'/')
        login.login(self.driver)
        username = self.driver.find_element_by_link_text('魏亚欣')
        ActionChains(self.driver).move_to_element(username).perform()
        time.sleep(2)
        self.driver.find_element_by_link_text('修改密码').click()
        time.sleep(2)
        self.driver.switch_to_frame('main_iframe')
        self.driver.find_element_by_id('oldpd').send_keys('123456')
        self.driver.find_element_by_id('pwd').send_keys('1234567')
        self.driver.find_element_by_name('repassword').send_keys('1234567')
        self.driver.find_element_by_link_text('提交').click()
        time.sleep(3)



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()