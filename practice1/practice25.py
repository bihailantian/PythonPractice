# !/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：利用递归方法求5!。
"""


def factorial(num):
    '''
    求num!的阶乘
    '''
    sum = 0
    a = 1
    for j in range(1,num + 1):
        a = a * j
    sum = sum + a
    return sum
    
print("5! = %d" % factorial(5))