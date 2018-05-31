#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

'''
 Python 文件I/O
'''

import os


fo = open("file/foo.txt","r+")

str = fo.read()
print(str)

position = fo.tell()

print("当前文件的位置：",position)

fo.close()


# 重名文件
#os.rename("file/foo.txt","file/foo2.txt")

# 删除文件
os.remove("file/test.txt")