#!/use/bin/python3
# -*- coding:UTF-8 -*-

'''
 pyhton 多线程
'''

import _thread
import time

# 为线程定义一个函数
def printTime(threadName,delay):
	count = 0;
	while count < 5:
		time.sleep(delay)
		count += 1
		print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
		

# 创建两个线程
try:
	_thread.start_new_thread( printTime, ("Thread-1", 2, ) )
	_thread.start_new_thread( printTime, ("Thread-2", 4, ) )
except:
	print ("Error: 无法启动线程")

while 1:
	pass