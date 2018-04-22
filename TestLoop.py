#!/usr/bin/python
# -*- encoding；utf-8 -*-

'''
python 循环语句

'''


# while 循环

count = 0;
while ( count < 9 ) :
	print("this count is " ,count) # print("this count is " + count) 是错误的
	count = count +1

print("end")



# 循环使用 else 语句


print("\n循环使用 else 语句:\n")

count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")


print("\nfor循环语句:\n")

for letter in 'Python':    			# 第一个实例
	print ( '当前字母 :', letter )


fruits = ["banana","apple","mango"]

for fruit in fruits : 				# 第二个实例
	print("当前水果：",fruit)

print("end")



# 九九乘法表

for x in range(1,10):
	for y in range(1,x+1):
		# print(y,"*",x,"=",x*y,end=" ")
		print("%d*%d=%2d" % (y,x,x*y),end=" ") # 使用站位符是格式对齐
	print()