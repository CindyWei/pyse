#-*-coding:utf-8-*-
'''
2014-2-9
习题5：更多的变量和打印
'''
my_name = 'Zed A. Shaw'
my_age = 35 #not a lie
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inchs tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

'''
学习总结：
根据变量的类型，打印字符串语句中使用相应的格式符号；语句中含多个变量格式符号时，后面用括号括起来多个变量。
'''