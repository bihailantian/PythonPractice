#!/usr/bin/python3
# -*- encoding；utf-8 -*-
 
import pymysql
 """
 连接数据库
 """

# 打开数据库连接      ip         用户名  密码   数据名称
db = pymysql.connect("localhost","root","root","py_test" ) 
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()
