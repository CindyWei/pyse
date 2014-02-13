#coding=utf-8

class Person(object):
	def __init__(self, name):
		self.name = name
		self.pet = None  #定义了类的两变量 name 和pet

#类的继承
class Employee(Person):  
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary

mary = Person("Mary")
print mary.name
print mary.pet
employee = Employee("Cindy", 5000)
print employee.name 
print employee.salary



