#codeing:utf-8
from selenium import webdriver
import os,time


dr = webdriver.Chrome()
url = 'http://sports.qq.com/seriea/'


dr.get(url)
links = dr.find_element_by_css_selector('#inter .hot_list').find_elements_by_tag_name('a')




result = {}
urls = []
for a in links:
 urls.append(a.get_attribute('href'))
print urls


for url in urls:
 dr.get(url)
 try:
 title = dr.find_element_by_css_selector('#C-Main-Article-QQ h1').text
 print title
 content = dr.find_element_by_id('Cnt-Main-Article-QQ').text
 print content
 result[title] = content
 except:
 print 'do nothing'


print result


dr.quit()
