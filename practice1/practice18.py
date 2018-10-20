# !/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数
"""

import math


for n in range(2,1000):
	#因子数组
	factor = []
	sum = 0
	"""
	if n == 6 or n == 7:
		print("n",n,math.floor(n/2) +1)
	"""
	#math.floor(n/2) +1 因为range()的右边是开区间,math.floor():向下取整
	for i in range(1,math.floor(n/2) +1):
		if n % i == 0:
			sum += i
			factor.append(str(i))
			
	if sum == n:
		print ('%d=' % n + '*'.join(factor))