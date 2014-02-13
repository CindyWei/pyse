#coding=utf-8
'''
2014-2-9
习题8：打印，打印
'''
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter,formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

'''
输出结果：
1 2 3 4
'one' 'two' 'three' 'four'
True False False True
'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
[Finished in 0.1s]

学习总结：
使用%r输出时，数字和真假关键字（True False）不会加单引号，字符串则会自动加上或转为单引号（即使原字符串用的是双引号），但是如有字符串内部已经含有单引号，则会自动加上双引号。
'''
