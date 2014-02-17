#coding: utf8

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://sports.qq.com/seriea/")

guomi_title = driver.find_element_by_id("inter")

hot_list = guomi_title.find_element_by_class_name("hot_list")
hot_list_details = hot_list.find_element_by_xpath("/html/body/div[6]/div/div[4]/div[2]/div/ul")

detail_li = ["/html/body/div[6]/div/div[4]/div[2]/div/ul/li"]
detail_link = ["/html/body/div[6]/div/div[4]/div[2]/div/ul/li/a"]

for i in range(2, 12):
    detail_li.append("/html/body/div[6]/div/div[4]/div[2]/div/ul/li[" + str(i) + "]")
print detail_li

for i in range(2, 12):
    detail_link.append("/html/body/div[6]/div/div[4]/div[2]/div/ul/li[" + str(i) + "]/a")
print detail_link

j = 0
for detail_li_text in detail_li:
    li = hot_list_details.find_element_by_xpath(detail_li_text)
    print li.find_element_by_xpath(detail_link[j]).text
    j = j + 1

driver.quit()


