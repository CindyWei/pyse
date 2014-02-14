#coding=utf-8
'''
自动发送邮件到邮箱
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮箱
sender = "weiyaxin312@163.com"
#接收邮箱
receiver = '1584727048@qq.com'
#发送邮件的主题
subject = 'Python email test'
#发送邮箱服务器
smtpserver = 'smtp.163.com'
#发送邮箱用户名、密码
username = 'weiyaxin312@163.com'
password = '312314'

#中文需要有参数'utf-8',单字节字符不需要
#msg = MIMEText('你好！','text','utf-8') #第二个参数是设置邮件格式，也可为html，RTF
#msg['Subject'] = Header(subject)
#以上两句代码执行后，文件内容以附件形式保存
#以下是HTML形式的文件内容，直接显示在邮件主体
msg = MIMEText('<html><h1>你好！</h1></html>','text','utf-8')
msg['Subject'] = subject

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
