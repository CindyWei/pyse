#coding=utf-8
import unittest
#这里需要导入测试文件
#import baidu,youdao  
import HTMLTestRunner
import time

#把test_case目录添加到path下，这里用的相对路径
import sys 
sys.path.append("\test_case")
from test_case import *
import allcase_list  #调用数组文件

#获取数组方法
alltestnames = allcase_list.caselist()
#将用例组装数组
'''
alltestnames = [
    baidu.Baidu,
    youdao.Youdao,
    ]
'''

testunit=unittest.TestSuite()

#循环读取数组中的用例
for test in alltestnames:
    testunit.addTest(unittest.makeSuite(test))
#将测试用例加入到测试容器(套件)中

#testunit.addTest(unittest.makeSuite(baidu.Baidu))  
#testunit.addTest(unittest.makeSuite(youdao.Youdao))


#取前面时间
now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))

#定义个报告存放路径，支持相对路径。
filename = 'E:\\automation\\GitHub\\pyse\\report\\'+now+'result.html'
fp = file(filename, 'wb') 

runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'搜索测试报告',
    description=u'用例执行情况：')

#执行测试套件
runner.run(testunit)
