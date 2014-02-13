#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import  time
from public import login   #从public文件夹中引人login文件
from public import createpost

class WordPress_Delete(unittest.TestCase):
	post_list_url = "http://127.0.0.1:8080/wordpress/wp-admin/edit.php"

	def setUp(self):
		self.dr = webdriver.Chrome()

	def test_delete_post1(self):
		"""利用弹出菜单删除post的用例"""
		login.login(self.dr)  #调用login公用方法
		createpost.create_post(self.dr)   #为了保持case的独立性，在删除之前先创建一个post文章
		self.dr.get(self.post_list_url)
		post = self.dr.find_element_by_partial_link_text("new post")
		time.sleep(3)
		#移动鼠标到要删除的元素,等待10s直到弹出菜单出现并点击
		ActionChains(self.dr).move_to_element(post).perform()
		w = WebDriverWait(self.dr, 10)
		w.until(lambda dr: self.dr.find_element_by_class_name('row-actions').is_displayed())
		self.dr.find_element_by_link_text("移至回收站").click()
		#删除成功后，获取提示信息模块的class属性值来做断言
		cancel = self.dr.find_element_by_id("message").get_attribute('class')
		self.assertTrue("updated below-h2" in cancel)
		print "Delete_Method1: success"

	def test_delete_post2(self):
		"""选中后，利用下拉菜单删除post的用例"""
		login.login(self.dr)   #调用login公用方法
		createpost.create_post(self.dr)
		self.dr.get(self.post_list_url)
		self.dr.find_element_by_name("post[]").click()
		#选择下拉选项"移至回收站"
		select_ele = self.dr.find_element_by_name("action")
		select = Select(select_ele)
		select.select_by_value("trash")
		#点击“应用”按钮
		time.sleep(3)
		self.dr.find_element_by_id("doaction").click()
		#删除成功后，获取提示信息模块的class属性值来做断言
		cancel = self.dr.find_element_by_id("message").get_attribute('class')
		self.assertTrue("updated below-h2" in cancel)
		print "Delete_Method2: success"


	def tearDown(self):
		time.sleep(3)
		self.dr.quit()

if __name__ == "__main__":
	unittest.main()

"""
两种方法删除post的用例

第一种：利用移动鼠标后的弹出菜单，引入ActionChains
第二中：利用Select下拉菜单，引入Select
缺陷：仅能删除现有的标题含“new post”的或者是checkbox的name为“post[]”的（列表中所有的checkbox的name都是一样的），经运行发现，两种方法均仅能删除最新的，不能随意删除任意一个
"""