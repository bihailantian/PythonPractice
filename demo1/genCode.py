#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

"""
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
"""
import uuid

def genCode(n):
    '''
    生成激活码
    n:激活码的个数
    '''
    activity_code = []
    for i in range(n):
        code = uuid.uuid1()
        #print(code)
        activity_code.append(str(code))
    
    return activity_code


if __name__ == "__main__":
    activity_code = genCode(200)
    print("-----------------------------------")
    for i in range(len(activity_code)):
        print(activity_code[i])
