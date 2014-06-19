#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time,sys

reload(sys)   
sys.setdefaultencoding('utf8')  

class News(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://sports.qq.com/seriea"


    def test_print_news(self):
        self.driver.get(self.base_url+'/')
        handle1 = self.driver.current_window_handle
        #获取“国米”下的<li>标签元素
        tag_lis = self.driver.find_elements_by_xpath("//div[@id='inter']/div[2]/div/ul/li") 
        for tag_li in tag_lis:
            a = tag_li.find_element_by_tag_name('a')
            sub_url = a.get_attribute('href')
            print sub_url

            a.click()
            self.driver.implicitly_wait(30)
            allhandles = self.driver.window_handles
            for handle in allhandles:
                if handle != handle1:
                    self.driver.switch_to_window(handle)
                    print self.driver.title
                    body = self.driver.find_element_by_id('Wrap')  # 另外还有一个body id='p-QQ', 暂时还无法打印body
                    print body.text
                    time.sleep(3)
                    self.driver.close()
            
                self.driver.switch_to_window(handle1)

            



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()