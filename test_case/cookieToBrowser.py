#coding=utf-8
from selenium import webdriver
import os,time

driver = webdriver.Chrome()
driver.get("http://student.cuotiben.net.cn/")
cookie= driver.get_cookies()
#将获得cookie 的信息打印
print cookie
#访问xxxx 网站
#driver.get("http://student.cuotiben.net.cn/")
#将用户名密码写入浏览器cookie
driver.add_cookie({'name':'SESS_732100_705', 'value':'13683607947'})
driver.add_cookie({'name':'s%3AxiV%2BtNhxisqxsWLld8E2oRap.xtZ0Pb1%2BoZMcOp0blKrP8GOqOwvkflWGfzdTgcxgSTg', 'value':'123456'})
#再次访问xxxx 网站，将会自动登录
driver.get("http://student.cuotiben.net.cn")
time.sleep(3)
driver.quit()