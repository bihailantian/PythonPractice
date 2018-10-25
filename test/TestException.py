#!/use/bin/env python3
# -*- coding:UTF-8 -*-

'''
python的异常(Exception)处理

'''

try:
	fh = open("file/testFile.txt","w")
	fh.write("这是一个测试文件，用于测试异常")
except IOError:
	print("Error: 没有找到文件或读取文件失败")
else:
	print("内容写入文件成功")
	fh.close()