#coding=utf-8
'''
2014-2-11
'''

"""
从东西里获取东西
现在我有三种方法可以从某个东西里获取它的内容：
# 从字典获取
mystuff['apples']
# 从模块.py文件中获取
mystuff.apples()
print mystuff.tangerine
# 从类class中获取
thing = MyStuff()
thing.apples()
print thing.tangerine
"""

class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

'''
学习总结：
为什么创建 __init__ 或者别的类函数时需要多加一个 self 变量？
如果你不加 self ， cheese = 'Frank' 这样的代码意义就不明确了，它指的既可能
是实例的 cheese 属性，或者一个叫做 cheese 的局部变量。有了 self.cheese =
'Frank' 你就清楚地知道了这指的是实例的属性 self.cheese 。、
'''