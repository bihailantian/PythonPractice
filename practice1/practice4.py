# !/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
"""

arr = []

for i in range(3):
	x= input("输入三个整数:\n")
	arr.append(x)

print(arr)

arr.sort()

print(arr)