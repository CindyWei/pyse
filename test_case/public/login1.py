#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time
import fun
import csv  #导入csv包

#CSV读取文件
'''
#读取本地CSV文件
my_file='E:\\automation\\Selenium Script\\pyse\\data\\info.csv'
data=csv.reader(file(my_file,'rb'))

#循环输出每一行信息
for user in data:
    print user[0]
    print user[1]
    print user[2]
    print user[3]

'''

#字典读取文件
'''
info = fun.zidian()

for us,pw in info.items():
    print us
    print pw

'''
#txt文件读取文件
'''
source = open("E:\\automation\\Selenium Script\\pyse\\data\username.txt", "r") #用户名文件
un = source.read() #读取用户名
source.close()

source2 = open("E:\\automation\\Selenium Script\\pyse\\data\password.txt", "r") #密码文件
pw = source2.read()  #读取密码
source2.close()
''' 
#通过函数方式读取
un,pw = fun.fun()

def login(self):
    driver = self.driver
    driver.maximize_window()
    driver.find_element_by_id("user_name").clear()
    driver.find_element_by_id("user_name").send_keys(un)
    driver.find_element_by_id("user_pwd").clear()
    driver.find_element_by_id("user_pwd").send_keys(pw)
    driver.find_element_by_id("dl_an_submit").click()
    time.sleep(3)

def loginout(self):
    driver = self.driver
    driver.find_element_by_class_name("Usertool").click()
    time.sleep(2)
    driver.find_element_by_link_text("退出").click()
    time.sleep(2)


