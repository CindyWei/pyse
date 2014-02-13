#coding=utf-8
'''
2014-2-9
习题12：raw_input()提示信息
'''

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

'''
学习总结：
raw_input()的括号中可加入提示信息参数，提示用户输入的内容
'''