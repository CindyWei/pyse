#coding=utf-8
'''
2014-2-10
习题32：循环和列表
'''

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

elements = []
for i in range(0,6):
	print "Adding %d to the list." % i
	elements.append(i)      #在列表尾部追加元素

#打印元素
for i in elements:
	print "elements was: %d" % i

'''
学习总结：
for-in 循环语句格式
创建序列 elements=[]
追加元素到列表，用elements.append(i)
rang(0,6) 不包含6 类似[0,6)
'''