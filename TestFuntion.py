#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

print("Hello")



a = 2

def ChangeInt():
	a = 10


ChangeInt()



print("a=",a)





def changeme(mylist):
	mylist.append([1,2,3,4])
	print("函数内取值: ", mylist)
	


mylist = [10,20,30];

print("函数外取值: ", mylist)
changeme(mylist);
print("函数外取值: ", mylist)	


print("===========================================================")


#可写函数说明
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print( "Name: ", name)
   print( "Age ", age)
   return;

#调用printinfo函数
printinfo( age=50, name="miki" );
printinfo( name="miki")

print("=========================不定长参数==================================")

# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;
 
# 调用printinfo 函数
printinfo( 10 );
printinfo( 70, 60, 50 );


print("=========================匿名函数==================================")

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))