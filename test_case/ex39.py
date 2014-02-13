#coding=utf-8
'''
2014-2-10
习题39：字典
'''

#序列
things = ["a", "b", "c", 'd']
print things[1]
things[1] = 'm'
print things[1]
print things

# 字典
stuff = {'name': "Cindy", 'age': 28, "height": 20 * 5 + 2}
print stuff["name"]
print stuff['age']

stuff['age'] = 30
print stuff['age']

stuff['home'] = 'Hebei'
print stuff['home']

print stuff

stuff[1] = "wow"
print stuff[1]
print stuff

del stuff['home']
print stuff

class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
		#输出序列中数据
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
字典有.item()方法，例如 for i in dic.items():序列没有,写为for i in elements:
'''
