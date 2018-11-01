#!/use/bin/env/python3
# -*- encoding: utf-8 -*-

"""
题目：修改输出字体的颜色
"""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)

print('=============================================')
print('\033[1;31;40m')
print('*' * 50)
print('*HOST:\t', 2002)
print('*URI:\t', 'http://127.0.0.1')
print('*ARGS:\t', 111)
print('*TIME:\t', '22:28')
print('*' * 50)
print('\033[0m')

