#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time
from public import login


def upload_self(dr):
	select = dr.find_element_by_id("subject")
	select.find_element_by_xpath("//option[@value='42']").click()
	#上传图片操作
	dr.find_element_by_id("topic_img").send_keys('E:\\automation\\GitHub\\pyse\\image\\00.jpg')
	time.sleep(3)
	#选择自行标注按钮
	dr.find_element_by_id('self').click()
	time.sleep(2)
	#点击加载知识点
	dr.find_element_by_id('menuBtn').click()
	time.sleep(2)
	#双击选择知识点
	dr.find_element_by_id('treeDemo_1_switch').click()
	dr.find_element_by_id('treeDemo_2_switch').click()
	dr.find_element_by_id('treeDemo_3_switch').click()
	dr.find_element_by_id('treeDemo_4_switch').click()
	dr.find_element_by_id('treeDemo_5_switch').click()
	#双击底层知识点
	double = dr.find_element_by_id('treeDemo_6_span')
	ActionChains(dr).double_click(double).perform()
	time.sleep(3)
	#提交
	dr.find_element_by_link_text("确定").click()
	time.sleep(3)

