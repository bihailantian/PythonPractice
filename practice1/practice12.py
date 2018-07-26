# !/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方
"""

i = 153
x = i % 10
y = int(i / 10 % 10)
z = int(i / 100)
# print(x) # 个位上的数
# print(y) # 十位上的数
# print(z) # 百位上的数

for i in range(100,1000):
	x = i % 10
	y = int(i / 10 % 10)
	z = int(i / 100)
	if i == x**3 + y**3 + z**3:
		print(i)