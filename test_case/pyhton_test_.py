#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys 


try:
    driver = webdriver.Chrome()
    driver.get("http://sports.qq.com/seriea/")
    guomi_title = driver.find_element_by_id("inter")
    hot_list = guomi_title.find_element_by_class_name("hot_list")
    hot_list_details = hot_list.find_element_by_xpath("/html/body/div[6]/div/div[4]/div[2]/div/ul")

    detail_li = ["/html/body/div[6]/div/div[4]/div[2]/div/ul/li"]
    detail_link = ["/html/body/div[6]/div/div[4]/div[2]/div/ul/li/a"]
    for i in range(2, 12):
        detail_li.append("/html/body/div[6]/div/div[4]/div[2]/div/ul/li[" + str(i) + "]")
    # print detail_li
    for i in range(2, 12):
        detail_link.append("/html/body/div[6]/div/div[4]/div[2]/div/ul/li[" + str(i) + "]/a")
    # print detail_link
    j = 0
    now_handle = driver.current_window_handle
    for detail_li_text in detail_li:
        li = hot_list_details.find_element_by_xpath(detail_li_text)
        a_link = li.find_element_by_xpath(detail_link[j])
        a_text = a_link.text
        print a_text
        # a_link.click()  # occur error
        a_link.send_keys(Keys.ENTER)
        time.sleep(5)
        j = j + 1
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to_window(handle)
                if driver.title.find(a_text) == -1:
                    continue 
                # need to modify -----------------------
                body = driver.find_element_by_id('Wrap')
                print body
                # --------------------------------------
                driver.switch_to_window(now_handle)

except Exception as e:
    print str(e)

finally:
    time.sleep(10)
    driver.quit()
