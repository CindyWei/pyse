#coding=utf-8
'''
2014-2-9
习题13：参数、解包、变量
'''

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variabl is:", third

'''
学习总结：
在cmd命令行输入 python ex13.py a b c 回车运行，后面的四个参数分别赋值于脚本内的四个变量并将其输出。
argv和raw_input()有什么不同? 不同点在于用户输入的时机不同。如果参数是在用户执行命令时就要输入的，则是argv，如果是在脚本运行过程中需要用户输入，那就是raw_input()
命令行参数也是字符串类型，即使输入的是数字
'''
		