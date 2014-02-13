#coding=utf-8
import unittest 
import HTMLTestRunner
import os ,time


listaa='E:\\automation\\Selenium Script\\pyse\\test_case'
def creatsuitel():
    testunit=unittest.TestSuite()
    #discover方法定义
    discover=unittest.defaultTestLoader.discover(listaa,
                      pattern ='*_start.py',
                      top_level_dir=None)
    
    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for  test_case in test_suite:
            testunit.addTests(test_case)
            print testunit
    return testunit


alltestnames = creatsuitel()

now = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
filename = 'E:\\automation\\Selenium Script\\pyse\\report\\'+now+'_result.html'
fp = file(filename, 'wb') 

runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'百度搜索测试报告',
    description=u'用例执行情况：')

#执行测试用例
runner.run(alltestnames)
