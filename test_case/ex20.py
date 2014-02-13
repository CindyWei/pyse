#coding=utf-8
'''
2014-2-9
习题20：函数和文件
 '''

from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
 	f.seek(0) #类似于磁头，每次运行则回到文件的开始位置即0字节的位置

def print_a_line(line_count, f):
 	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)

'''
学习总结：
打印输出某行数据时，需要把行号传递过去
seek(0): 使文件磁头返回到0字节的位置，即最开始的位置
'''