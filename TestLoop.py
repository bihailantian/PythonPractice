# -*- encoding；utf-8 -*-
'''
python 循环语句

1、可以尝试打印九九乘法表

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