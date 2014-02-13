#coding=utf-8
'''
2014-2-9
习题18：命名、变量、代码、函数
'''

#this one is like your scripts with argv
def print_two(*args): #将函数的所有参数都接收进来
	arg1, arg2 = args #将参数解包
	print "arg1: %r, arg2: %r" %(arg1, arg2)

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
	print "I got nothing"

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

'''
学习总结：
def 定义函数，函数名后跟参数和冒号
第二个函数的传参形式用的更多
'''

