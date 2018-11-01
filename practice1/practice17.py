#!/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
"""

a = input("请输入s=a+aa+aaa+aaaa+aa...a的a的值：\n")

numStr = input("请输入相加的个数：")
s = 0
str = ""
if numStr.isalnum():
	num = int(numStr)
	for i in range(num):
		print("a=",a)
		print("i=",i)
		addition = a * (i+1)
		print("addition=",addition)
		s = s + int(addition)
		str = str + "+" + addition
	print(str[1:],"=",s)
else:
	print("请输入数字！")