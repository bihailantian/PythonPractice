#!/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
	求它在第10次落地时，共经过多少米？第10次反弹多高?
"""

height = 100
#走过的路程
distance = 0
#反弹次数
count = 10
#反弹高度
reHeight = 0


for i in range(1,count+1):
	if i == 1:
		distance = height
		reHeight = height / 2
	else:
		distance = distance + reHeight
		reHeight = reHeight/2
	
	print("第%d次落地时，共经过%f米，第%d次反弹%f米" % (i,distance,i,reHeight))
	