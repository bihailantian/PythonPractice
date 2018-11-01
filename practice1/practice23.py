#!/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
"""

def test(count):
    '''
    count 列表的项数，并且大于2
    '''
    #分子
    mem_first = 2
    mem_secede = 3
    #分母
    den_first = 1
    den_secede = 2

    sum = mem_first/den_first + mem_secede/den_secede
    for i in range(2,count):
        mem = mem_first + mem_secede
        den = den_first + den_secede
        sum = sum + mem/den
        mem_first = mem_secede
        mem_secede = mem
        den_first = den_secede
        den_secede = den
    return sum
    
print("前20项之和",test(20))