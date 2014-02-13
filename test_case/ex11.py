#coding=utf-8
'''
2014-2-9
习题11：输入
'''

print "How old are you?",
age =  raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall, and %r heavy." % (age, height, weight)

'''
学习总结：
用户输入用raw_input（）函数，用户的输入均为字符串，通过int（）可将字符串转为整型数据，如x=int(raw_input())
input()会将你输入的东西当作代码来处理，会有安全问题，尽量避开不用此函数。
'''
