# !/use/bin/python3
#  -*- coding:UTF-8 -*-

# 1、导入socket、sys模块
import socket
import sys

# 2、创建socket对象
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 3、获取本地主机名
host = socket.gethostname()

# 4、绑定端口号
port = 9999
serverSocket.bind((host,port))

# 5、设置最大连接数，超过后排队
serverSocket.listen(5)

# 6、建立客户端连接
while True:
	clientSocket,addre = serverSocket.accept()
	print(addre)
	msg = "客户端，您好"
	clientSocket.send(msg.encode('utf-8'))
	clientSocket.close()




