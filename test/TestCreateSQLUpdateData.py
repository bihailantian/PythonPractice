#!/usr/bin/python3
# -*- encoding；utf-8 -*-

''' 数据库更新操作 '''

import pymysql


# 打开数据库连接      ip         用户名  密码   数据名称
db = pymysql.connect("localhost","root","root","py_test")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor();


# SQL更新语句
sql = "update employee set age = age + 1 where sex = '%c'" % ('M')

try:
	# 执行SQl语句
	cursor.execute(sql)
	# 提交到数据库
	db.commit()
except:
	# 发生错误时回滚
	db.rollback()

# 关闭数据库连接
db.close()