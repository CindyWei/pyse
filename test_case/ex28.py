#coding=utf-8
'''
2014-2-10
习题28：布尔表达式练习
'''

True and True	#结果：Ture
False and True	#结果：False
1==1 and 2==2   #结果：True
"test"=="test"	#结果：True
1==1 or 2!=1    #结果：True
True and 1 == 1   #结果：True
False and 0 != 0	#结果：False
True or 1 == 1       #结果：True
"test" == "testing"		#结果：False
1 != 0 and 2 == 1       #结果：False
"test" != "testing"		#结果：True
"test" == 1          #结果：False
not (True and False)   #结果：True
not (1 == 1 and 0 != 1)    #结果：False
not (10 == 1 or 1000 == 1000)     #结果：False
not (1 != 10 or 3 == 4)       #结果：False
not ("testing" == "testing" and "Zed" == "Cool Guy")    #结果：True
1 == 1 and not ("testing" == 1 or 1 == 0)   #结果：True
"chunky" == "bacon" and not (3 == 4 or 3 == 3)    #结果：False
3 == 3 and not ("testing" == "testing" or "Python" == "Fun")     #结果：False