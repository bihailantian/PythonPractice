# !/use/bin/python3
# -*- coding:UTF-8 -*-

import socket
import sys


serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口号
serverSocket.bind((host,port))

serverSocket.listen(5)

while True:
	# 建立客户端连接
	clientsocket,addr = serverSocket.accept()

	print("连接地址: %s" % str(addr))
	
	msg='欢迎访问菜鸟教程！'+ "\r\n"
	clientsocket.send(msg.encode('utf-8'))
	clientsocket.close()

