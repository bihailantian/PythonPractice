# !/use/bin/python3
#  -*- coding:UTF-8 -*-

# 1、导入socket、sys模块
import socket
import sys

# 2、创建socket对象
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 3、获取本地主机名
host = socket.gethostname()

# 4、绑定端口号,连接服务端
port = 9999
clientSocket.connect((host,port))

# 5、接收小于1024字节的数据
msg = clientSocket.recv(1024)

clientSocket.close()

print(msg.decode('utf-8'))


