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
        driver = self.driver
        #百度搜索
        driver.get(self.base_url + "/")
        driver.find_element_by_name("wd").clear()
        driver.find_element_by_name("wd").send_keys("selenium")
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(3)
    
    def test_baidu1(self):
        driver = self.driver
        #百度搜索
        driver.get(self.base_url + "/")
        driver.find_element_by_name("wd").clear()
        driver.find_element_by_name("wd").send_keys("webdriver")
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":

    #定义一个单元测试容器
    testunit=unittest.TestSuite()

    #将测试用例加入到测试容器中
    testunit.addTest(Baidu("test_baidu"))  
    testunit.addTest(Baidu("test_baidu1"))

    #定义个报告存放路径，支持相对路径。
    filename = 'E:\\automation\\Selenium Script\\pyse\\report\\result2.html'
    fp = file(filename, 'wb')
    #定义测试报告
    runner =HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'百度搜索测试报告',
        description=u'用例执行情况：')

    #运行测试用例
    runner.run(testunit)
