#coding=utf-8
'''
2014-2-9
习题7：更多打印
'''
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,    #此处的逗号是下一语句换行，去掉逗号的话，会分两行输出
print end7 + end8 + end9 + end10 + end11 +end12

'''
学习总结：
%后不仅可以直接跟变量，也可以直接跟字符串，但字符串要加上引号，如% 'snow'
重复输出多个字符时，用*，如第9行的10个点 '.' * 10
25行的逗号的作用是：让26行不用换行直接在后面输出，去掉逗号，则各自占用一行
单引号常用来创建简短的字符串，双引号常用来创建较长的字符串
'''