#coding=utf-8
import time

#逋ｻ蠖標ordPress
def login(dr):
	dr.find_element_by_id('login_username').send_keys("13683607947")
	dr.find_element_by_id('login_password').send_keys("123456")
	dr.find_element_by_id('login_captcode').send_keys("abcd")
	dr.find_element_by_link_text('登录').click()
	time.sleep(3)