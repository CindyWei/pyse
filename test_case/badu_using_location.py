#coding=utf-8
from selenium import webdriver
import time
import sys
from package import location

sys.path.append("\package")
#调用location.py 文件的定位方法
we = location
dr = webdriver.Chrome()
dr.get('http://www.baidu.com')
#调用封装的方法
we.findId(dr,"kw1").send_keys('selenium')
time.sleep(2)
we.findId(dr,"su1").click()
time.sleep(2)
dr.quit()