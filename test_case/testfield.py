#coding=utf-8
from selenium import webdriver
import os
from time import sleep


file_path = 'file:///' + os.path.abspath('textfield.html')

class TestField(object):
	def __init__(self, dr, ele):
		self.dr = dr
		self.ele = ele
	#往text field中输入文字
	def set1(self, text):
		self.ele.send_keys(text)
		print "I type some text"
		sleep(2)
	#清除文字
	def clear1(self):
		self.ele.clear()
		print 'I clear it'
	#点击text field
	def click1(self):
		self.ele.click()
		print "I click it"
	#focus该text field
	def focus1(self):
		self.click1()
		print 'i click it ,then i focus it'
	#高亮该text field
	def high_light1(self):
		self.dr.execute_script("arguments[0].style.border = '2px solid red'", ele)
		print 'i hight light it'
		sleep(2)


dr = webdriver.Chrome()
dr.get(file_path)
ele = dr.find_element_by_id("tf")
tf = TestField(dr, ele)
tf.set1('bbb')
tf.clear1()
tf.high_light1()
tf.click1()
tf.focus1()
dr.close()






