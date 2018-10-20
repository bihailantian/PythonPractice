# !/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
   
"""


def pic(lines):
    '''
    计算空格、*与输出行数的关系
    '''
    middle = int(lines / 2)
    lines = int(lines / 2) * 2 + 1
    print(middle,lines)
    for i in range(1, lines + 1):        
        empty = abs(i - middle - 1)        
        print(' ' * empty, '*' * (2 * (middle - empty) + 1))
line = 7 # 设置输出行数
pic(7)