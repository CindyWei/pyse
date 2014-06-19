#coding=utf-8
from public import login
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time

class Info(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://student.test.cuotiben.net.cn"


    def test_information(self):
        self.driver.get(self.base_url+'/')
        login.login(self.driver)
        self.driver.find_element_by_link_text('个人信息').click()
        time.sleep(3)
        self.driver.switch_to_frame("main_iframe")
        self.driver.find_element_by_link_text('编辑').click()
        self.driver.find_element_by_id('email').send_keys('weiyaxin@cuotiben.net.cn')
        self.driver.find_element_by_id('editAva').click()
        self.driver.find_element_by_id('topic_img').send_keys('E:\\automation\\GitHub\\pyse\\image\\00.jpg')
        time.sleep(3)
        self.driver.find_element_by_class_name('baseinf_but btn_ok').click()
        time.sleep(3)
        self.driver.find_element_by_link_text('保存').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()