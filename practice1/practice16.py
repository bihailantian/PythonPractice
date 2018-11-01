#!/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""


inputStr = input("请输入一行字符：\n")
#字母
letters = 0
#空格
spaces = 0
#数字
num = 0
#其他字符
others = 0

for str in inputStr:
	#print("当前字符：",str)
	if str.isalpha():
		letters +=1
	
	elif str.isspace():
		spaces += 1
	
	elif str.isalnum():
		num += 1
	else:
		others += 1
	
print("字母:%d个 \n空格:%d个 \n数字:%d个 \n其他:%d个" %(letters,spaces,num,others))
	

