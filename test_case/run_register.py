#coding=utf-8
import unittest 
import HTMLTestRunner
import os ,time
from register import Register
import math


def suite():
    suite = unittest.TestSuite()
    suite.addTest(Register("test_register"))
    return suite
# 测试
if __name__ == "__main__":
    unittest.main(defaultTest = 'suite')

for i in range(100,999):
	print '13683600'+str(i)
	phone = '13683600'+str(i)
   	reg = Register(phone)
   	reg.test_register()