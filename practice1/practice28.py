#!/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
"""

num = int(input("请不多于5位的正整数：\n"))

numStr = str(num)

length = len(numStr)

if length <= 5:
    print("%d位数，%s" % (length,numStr[::-1]))