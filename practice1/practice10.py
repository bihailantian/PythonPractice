# !/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：暂停一秒输出，并格式化当前时间。
"""

import time

print (time.strftime('%Y-%m-%d %H:%M:%S' , time.localtime(time.time())))

time.sleep(1)

print (time.strftime('%Y-%m-%d %H:%M:%S' , time.localtime(time.time())))