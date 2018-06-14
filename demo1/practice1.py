# !/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
count = 0
for x in range(1,5):
	for y in range(1,5):
		for z in range(1,5):
			if (x != y) and (x != z) and (y != z):
				print(x,y,z)
				count += 1

print("一共"+str(count)+"个")  # 字符串不能直接拼接数字