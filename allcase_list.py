#coding=utf-8
#把test_case目录添加到path下，这里用的相对路径
import sys 
sys.path.append("\test_case")
from test_case import *

#用例文件列表
def caselist():
    alltestnames = [
        baidu_start.Baidu,
        youdao_start.Youdao,
        
        ]
    print "success  read case list!!"

    return alltestnames
if __name__ == "__main__":
	caselist()