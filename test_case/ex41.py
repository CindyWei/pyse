#coding=utf-8
'''
2014-2-11
习题41：类
'''

class TheThing(object):
	def __init__(self):
		self.number = 0

	def some_function(self):
		print "I got called"

	def add_me_up(self, more):
		self.number += more
		return self.number

a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print a.add_me_up(20)
print b.add_me_up(30)

print a.number
print b.number

class TheMultiplier(object):
	def __init__(self, base):
		self.base = base
	def do_it(self, m):
		return m * self.base

x = TheMultiplier(a.number)
print x.base
print x.do_it(30)


class Dog(object):
	def __init__(self, name):
		self.name = name


class Person(object):
	def __init__(self, name):
		self.name = name
		self.pet = None  #定义了类的两变量 name 和pet

#类的继承
class Employee(Person):  
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary

class Fish(object):
	pass

class Salmon(Fish):
	pass
class Halibut(Fish):
	pass

rover = Dog("Rover")
print rover.name
mary = Person("Mary")
print mary.name
print mary.pet
employee = Employee('Cindy', 5000)
print employee.name  
print employee.salary


'''
学习总结：
创建的类都要加上（object）参数
类的继承，用父类super(Employee, self).__init__(name)来初始化
'''
		
		
		
		
