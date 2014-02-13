#coding=utf-8
'''
2014-2-10
习题33：While循环
'''

i = 0
numbers = []

while i <6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Numbers now:", numbers
	print "At the bottom i is %d" % i

print "The numbers:"
for num in numbers:
	print num

'''
学习总结：
尽量少用while循环，最好用for-in循环
while循环没有自动加1的功能，需写进模块内，for循环则不用写
'''