#coding=utf-8
from selenium import webdriver
import unittest, time

class News(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://sports.qq.com/seriea"

"""
备注：此代码因为网速原因，没法运行，只能按自己的想法把代码写了出来，没调试运行，不确定能不能顺利运行
""" 
    def test_print_news(self):
        self.driver.get(self.base_url+'/')
        handle1 = self.driver.current_window_handle
        #获取“国米”下的<li>标签元素
        tag_lis = self.driver.find_elements_by_xpath("//div[@id='inter']/div[2]/div/ul") #网速原因，没法运行，不确定xpath写的对不对
        for tag_li in tag_lis:
            title = tag_li.text #不知道这样用行不行，还是要获取li下的a标签后才能.text
            print title
            self.driver.find_element_by_link_text(title).click()
            #print self.driver.current_url
            body = self.driver.find_element_by_id('Wrap')
            print body.text   #不知道这样行不行，要不要加.text
            #print body
            #定位窗口到主窗口
            handle2 = self.driver.current_window_handle
            if handle2 != handle1:
                self.driver.switch_to_window(handle1)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()