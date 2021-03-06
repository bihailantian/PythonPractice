#!/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：斐波那契数列
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
"""


def fib(n):
	'''
	n是大于0的整数
	'''
	if n < 1:
		print("n是大于0的整数")
		return []
	if n == 1:
		return [1]
	if n == 2:
		return [1, 1]
	fibs = [1, 1]
	for i in range(2, n):
		fibs.append(fibs[-1] + fibs[-2])
	return fibs
 
# 输出前 10 个斐波那契数列
print (fib(0))
