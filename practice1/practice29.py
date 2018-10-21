# !/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
"""

a = input("输入一串数字: ")
b = a[::-1]
if a == b:
    print("%s 是回文"% a)
else:
    print("%s 不是回文"% a)