# !/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
"""


def reverse2(s):
    '''
    反转字符串
    '''

    l=list(s)
    l.reverse()
    print("".join(l))

 
if __name__ == "__main__":
    s = input("请输入的5个字符：\n")
    #方法一
    print(s[::-1])
    #方法二
    reverse2(s)