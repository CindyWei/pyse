#coding=utf-8
'''
2014-2-9
习题4：变量和命名
'''
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_drivern = drivers
carpool_capacity = cars_drivern * space_in_a_car
average_passengers_per_car = passengers / cars_drivern

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "peopel today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

print "Hey %s there." % "you"

'''
学习总结：
变量名最好找有意义的单词命名，常用下划线'_'来隔开单词；运算符两边最好加空格，使代码更易读。
'''