from selenium import webdriver
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import random

file_path='file:///'+os.path.abspath('locate_advance.html')

def high_light(dr,ele):
	dr.execute_script("arguments[0].style.border='2px solid red'",ele)

def rand_select(sel):
	the_max=len(sel.options)-1
	the_min=0
	index=random.randint(the_min,the_max)
	sel.select_by_index(index)

dr=webdriver.Chrome()
dr.get(file_path)
kw=dr.find_element_by_name('ip_first')
high_light(dr,kw)

select_elmt=dr.find_element_by_name('phone')
select=Select(select_elmt)
select.select_by_value('mi3')

for i in range(1,10):
	rand_select(select)
	sleep(1)

sleep(1)
dr.find_element_by_id('click_to_drop').click()
w=WebDriverWait(dr,10)
w.until(lambda dr: dr.find_element_by_class_name('dropdown-menu').is_displayed())
high_light(dr,dr.find_element_by_link_text('Another action'))
