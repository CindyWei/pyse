#coding=utf-8

from selenium import webdriver

dr = webdriver.Chrome()
base_url = "http://www.baidu.com"
dr.get(base_url)
title = "新 闻"
dr.find_element_by_link_text(title).click()


print self.driver.current_url
            allhandles = self.driver.window_handles
            for handle in allhandles:
                if handle != handle1:
                    self.driver.switch_to_window(handle)
                    print "content"
                    body = self.driver.find_element_by_id('Wrap')
                    print body.text
                    self.driver.close()
                else: 
                    #定位窗口到主窗口
                    #handle2 = self.driver.current_window_handle
                    #if handle2 != handle1:
                    self.driver.switch_to_window(handle1)