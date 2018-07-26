# !/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：输出 9*9 乘法口诀表。
"""

for x in range(1,10):
	for y in range(1,x+1):
		print("%d*%d=%2d" % (y,x,x*y),end=" ") # 使用占位符是格式对齐,end=" " 不换行输入
	print()