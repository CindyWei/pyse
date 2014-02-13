#coding=utf-8
'''
2014-2-9
习题10：转义
'''

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "I am 6'2\" tall."
print 'I am 6\'2" tall.'

'''
输出结果：
	I'm tabbed in.
I'm split
on a line.
I'm \ a \ cat.

I'll do a list:
	* Cat food
	* Fishies
	* Catnip
	* Grass

I am 6'2" tall.
I am 6'2" tall.

学习总结：
"\t":转义为按下tab键
"\n":转义为换行
"\\":转义为输出字符\
"\'":转义为输出字符'
'\"':转义为输出字符"

'''
