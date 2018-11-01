#!/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
"""

import math


n=int(input('Please input a number:'))
n1=n
l=[]
while n>1:
    for i in range(2,math.floor(n)+1):
        if n%i==0:
            n=n/i
            l.append(str(i))
            break

print ('%d=' % n1 + '*'.join(l))