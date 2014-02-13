#-*-coding:utf-8-*-
'''
2014-2-9
习题6：字符串和文本
'''

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print  joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

'''
学习总结：
'+'可用来连接两个字符串；使用%r时，会在该变量上加上一对引号，使用%s时则不会。
%r 常用来做debug
''' 