#!/usr/bin/env python3
# -*- encoding；utf-8 -*-

# break 语句

for x in range(1,10):
	for y in range(1,x+1):
		if y == 2:
			break
		print("%d*%d=%2d" % (y,x,x*y),end=" ") # 使用站位符是格式对齐
		
	print()