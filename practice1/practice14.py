#!/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
"""

score = int(input("请输入成绩："))

result = ""
if score < 0 or score > 100:
	print("此成绩无效")
elif score >= 90:
	result = "A"
elif score >= 60 and score < 90:
	result = "B"
else:
	result = "C"

print(result)