#coding=utf-8
from selenium import webdriver
import os,time

source = open("E:\\automation\\Selenium Script\\pyse\\data\\aa.txt", "r") 
values = source.readlines() 
source.close()

# 执行循环
for serch in values:
    browser = webdriver.Firefox()
    browser.get("http://www.baidu.com")
    browser.find_element_by_id("kw").send_keys(serch)
    browser.find_element_by_id("su").click()
    browser.quit()
