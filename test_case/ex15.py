#coding=utf-8
'''
2014-2-9
习题15：读取文件
'''

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's you file %r:" % filename
print  txt.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()

'''
学习总结：
打开文件并赋值给一个变量txt=open(filename)
读取文件内容用read()方法，如txt.read()
'''
