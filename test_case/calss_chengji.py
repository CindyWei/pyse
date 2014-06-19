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
        self.driver.find_element_by_link_text('班级管理').click()
        time.sleep(3)
        self.driver.switch_to_frame("main_iframe")
        self.driver.find_element_by_link_text('中农考试').click()
        close = self.driver.find_element_by_class_name('closeDialog')
        print close.text
        time.sleep(3)
        close.click()
        time.sleep(1)
        print "AddPost: success"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()