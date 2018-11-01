#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
Python 文件I/O
"""

import os


print("Python 文件I/O")

'''
print("\n=================键盘输入======================\n")

str = input("请输入:")
print("输入的内容是:",str)
'''


print("\n=================打开一个文件======================\n")

#如果foo.txt文件不存在，将会创建foo.txt
fo = open("file/foo.txt","w")

print("文件名:",fo.name)
print("是否已关闭:",fo.closed)
print("访问模式：",fo.mode)
#print("末尾是否强制加空格：", fo.softspace)

print("\n=======================================\n")

#fo.write("Hello Python!")
#fo.write("第二行写入，Hello Python!")
fo.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
fo.flush()
#关闭文件
fo.close()
print("是否已关闭:",fo.closed)

print("\n=======================================\n")

file = open("file/foo.txt","r")
str = file.read()
print("输出文件内容：")
print(str)


#创建目录
os.mkdir("newdir")



