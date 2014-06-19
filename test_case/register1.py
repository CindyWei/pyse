#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner

class Register(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://117.79.146.119:9100"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_register(self):
        u"""注册功能"""
        driver = self.driver
        #百度搜索
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("立即注册").click()
        time.sleep(3)
        driver.find_element_by_name("mobile").send_keys("13683600001")
        driver.find_element_by_name("realName").send_keys(u"魏安安")
        driver.find_element_by_xpath("//input[@value='0']").click()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("confirmPass").send_keys("123456")
        driver.find_element_by_name("email").send_keys("wei@126.com")
        driver.find_element_by_id("province")
        driver.find_element_by_xpath("//option[@value='51']").click()
        driver.find_element_by_id("city")
        driver.find_element_by_xpath("//option[@value='52']").click()
        driver.find_element_by_id("area")
        driver.find_element_by_xpath("//option[@value='54']").click()
        driver.find_element_by_id("school")
        driver.find_element_by_xpath("//option[@value='256']").click()
        driver.find_element_by_id("stage")
        driver.find_element_by_xpath("//option[@value='111767']").click()
        driver.find_element_by_id("grade_sel")
        driver.find_element_by_xpath("//option[@value='23']").click()
        driver.find_element_by_id("userClassId")
        driver.find_element_by_xpath("//option[@value='456']").click()
        driver.find_element_by_xpath("//input[@value='提交']").click()
        time.sleep(3)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()