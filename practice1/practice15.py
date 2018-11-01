#!/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：
# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法


# 日期替换
"""

import datetime


def test():
	print("test")

if __name__ == '__main__':
	# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
	print(datetime.date.today().strftime('%d/%m/%y'))
	# 创建日期对象
	mDate = datetime.date(2018,10,8)
	print(mDate.strftime("%d/%m/%y"))
	# 日期算术运算
	mDate = mDate + datetime.timedelta(days=1)
	print("-------------")
	print(mDate.strftime("%d/%m/%y"))
	mDate = mDate.replace(year=mDate.year + 1 )
	print(mDate.strftime("%d/%m/%y"))