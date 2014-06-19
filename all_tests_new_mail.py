#coding=utf-8
'''
整合自动发邮件功能
'''

import unittest
import HTMLTestRunner
import os,time,datetime,sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#定义发送邮件
def sent_mail(file_new):
	#发信邮件
	mail_from = "weiyaxin312@163.com"
	mail_to = "1584727048@qq.com"
	f = open(file_new, 'rb')
	mail_body = f.read()
	time.sleep(3)
	f.close()
	#print mail_body
	msg = MIMEText(mail_body, 'html', 'utf-8')
	#定义标题
	msg['Subject'] = u"测试报告"
	#定义发送时间（不定义可能有的邮件客户端会不显示发送时间）
	msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

	#msgRoot = MIMEMultipart('related')  
	#msgRoot['Subject'] = u"测试报告" 
  
	#构造附件  
	#att = MIMEText(mail_body, 'base32', 'utf-8')  
	#att["Content-Type"] = 'application/octet-stream'  
	#att["Content-Disposition"] = 'attachment; filename="report.html"'  
	#msgRoot.attach(att) 

	smtp = smtplib.SMTP()
	#连接SMTP服务器
	smtp.connect('smtp.163.com')
	#用户名密码
	smtp.login('weiyaxin312@163.com', '312314')
	smtp.sendmail(mail_from, mail_to, msg.as_string())
	smtp.quit()
	print 'email has send out!'

#查找测试报告，并调用发邮件功能
def find_newest_report():
	result_dir = 'E:\\automation\\GitHub\\pyse\\report'
	lists = os.listdir(result_dir)
	lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not os.path.isdir(result_dir+"\\"+fn) else 0)
	print ('最新生成的报告:'+lists[-1])
	#找到最新成功的文件路径
	file_new = os.path.join(result_dir,lists[-1])
	print file_new
	#调用发邮件模块
	sent_mail(file_new)

listaa='E:\\automation\\GitHub\\pyse\\test_case'
def creat_suite():

    testunit=unittest.TestSuite()
    #discover方法定义
    discover=unittest.defaultTestLoader.discover(listaa,
                      pattern ='*_start.py',
                      top_level_dir=None)
    
    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_file in discover:
        for  test_case in test_file:
            testunit.addTests(test_case)
    print testunit
    return testunit

#定义并生成测试报告
now = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
filename = 'E:\\automation\\GitHub\\pyse\\report\\'+now+'_result.html'
fp = file(filename, 'wb') 
runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'百度搜索测试报告',
    description=u'用例执行情况：')

alltestcases = creat_suite()

#执行测试用例
runner.run(alltestcases)
fp.close()
#执行发邮件
find_newest_report()



