#coding=utf-8
'''
2014-2-9
习题17：更多的文件操作
'''

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#We could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit ENTER to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

'''
学习总结：
from os.path import exists， exist（filename)用来判断文件是否存在，存在则返回True，反之False
读取第一个文件的内容并赋值给一个变量，之后再用write方法将此变量内容写入另一个文件，完成文件的拷贝
'''
