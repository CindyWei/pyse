#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_baidu(self):
        u"""百度搜索selenium"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw1").clear()
        driver.find_element_by_id("kw1").send_keys("selenium")
        time.sleep(2)
        driver.find_element_by_id("su1").click()
        time.sleep(3)
    
    def test_baidu1(self):
        u"""百度搜索webdriver"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw1").clear()
        driver.find_element_by_id("kw1").send_keys("webdriver")
        time.sleep(2)
        driver.find_element_by_id("su1").click()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()