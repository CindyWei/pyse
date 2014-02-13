#coding=utf-8
'''
2014-2-9
习题14：提示和传递
'''

from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about like me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

'''
学习总结：
raw_input()中的参数提示信息，可用一个变量来代替，不用重复输入了。
'''
