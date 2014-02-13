#coding=utf-8
'''
2014-2-9
习题16:读写文件
'''

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open (filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

'''
学习总结：
open(filename) 默认是以只读方式，即'r'模式打开文件。另外还有写入模式'w'和追加模式'a'
如果各自后面加上修饰符'+',如'w+','a+','r+',文件将以读写的方式打开

close():保存并关闭文件
write(xxx):讲内容写入文件
read():读取整个文件
readline():读取文本文件中的一行
truncate():清除文件内容
'''