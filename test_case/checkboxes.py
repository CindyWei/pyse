#coding=utf-8
from selenium import webdriver
import os,time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('checkboxes.html')
driver.get(file_path)
# 选择所有的type 为checkbox 的元素并单击勾选
checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
	checkbox.click()
# 打印当前页面上type 为checkbox 的个数
print len(checkboxes)
# 把页面上最后1个checkbox 的勾给去掉
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
time.sleep(3)
driver.quit()