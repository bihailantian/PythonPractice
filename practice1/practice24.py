# !/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：求1+2!+3!+...+20!的和
"""

sum = 0
#阶乘数
num = 20
for i in range(1,num + 1):
    a = 1
    for j in range(1,i + 1):
        a = a * j
    sum = sum + a

print("1+2!+3!+...+20! = %d" % sum)