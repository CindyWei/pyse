#coding=utf-8
'''
2014-2-11
习题44：继承VS合成
'''

#隐式继承
class Parent(object):
	def implicit(self):
		print "PARENT implicit()"
class Child(Parent):
	pass

dad = Parent()
son = Child()
dad.implicit()
son.implicit()

"""
输出结果：
PARENT implicit()
PARENT implicit()
"""

#显式复写
class Parent(object):
	def override(self):
		print "PARENT override()"
class Child(Parent):
	def override(self):
		print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()

"""
输出结果：
PARENT override()
CHILD override()
"""

#在运行前或运行后覆写
class Parent(object):
	def altered(self):
		print "PARENT altered()"
class Child(Parent):
	def altered(self):
		print  "CHILD, before Parent altered()"
		super(Child, self).altered()
		print "CHILD, after Parent altered()"

dad = Parent()
son = Child()
dad.altered()
son.altered()

"""
运行结果：
PARENT altered()
CHILD, before Parent altered()
PARENT altered()
CHILD, after Parent altered()
"""

#一起使用三种方式
class Parent(object):
	def override(self):
		print "PARENT override()"
	def implicit(self):
		print "PARENT implicit()"
	def altered(self):
		print "PARENT altered()"
class Child(Parent):
	def override(self):
		print "CHILD override()"
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"	


dad = Parent()
son = Child()

dad.implicit()
son.implicit()
dad.override()
son.override()
dad.altered()
son.altered()

"""
运行结果：
PARENT implicit()
PARENT implicit()
PARENT override()
CHILD override()
PARENT altered()
CHILD, BEFORE PARENT altered()
PARENT altered()
CHILD, AFTER PARENT altered()
"""
#多重继承
class SuperFun(Child, Parent):
	pass

#super()和__init__搭配使用
class Child(Parent):
	def __init__(self, stuff):
		self.stuff = stuff
		super(Child, self).__init__()

#合成
class Other(object):
	def override(self):
		print "OTHER override()"
	def implicit(self):
		print "OTHER implicit()"
	def altered(self):
		print "OTHER altered()"
class Child(object):   #此处没继承父类
	def __init__(self):
		self.other = Other()   #初始化一个类对象作为自己的变量
	def implicit(self):
		self.other.implicit()
	def override(self):
		print "CHILD override()"
	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD, AFTER OTHER altered()"

son = Child()
son.implicit()
son.override()
son.altered()

"""
运行结果：
OTHER implicit()
CHILD override()
CHILD, BEFORE OTHER altered()
OTHER altered()
CHILD, AFTER OTHER altered()
"""


		
		