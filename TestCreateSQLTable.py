#!/usr/bin/python3
# -*- encoding；utf-8 -*-

''' 创建数据库表 '''
import pymysql

# 打开数据库连接      ip         用户名  密码   数据名称
db = pymysql.connect("localhost","root","root","py_test" ) 

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("drop table if exists employee")

# 使用预处理语句创建表
sql = """ create table employee(
		FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT
		)"""

cursor.execute(sql)

#关闭数据库
db.close()
		
