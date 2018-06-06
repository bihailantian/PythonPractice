#!/usr/bin/python3
# -*- encoding；utf-8 -*-

''' 数据库插入操作 '''
import pymysql

# 打开数据库连接      ip         用户名  密码   数据名称
db = pymysql.connect("localhost","root","root","py_test" ) 

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()
 
# 关闭数据库连接
db.close()