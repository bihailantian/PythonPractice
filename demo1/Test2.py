#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

import genCode
import pymysql

def connectDB(sql):
    # 打开数据库连接      ip         用户名  密码   数据名称
    db = pymysql.connect("localhost","root","root","py_test" ) 
     
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
     
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute(sql)

if __name__ == '__main__':
    activity_code = genCode.genCode(200)
    #print("','".join(activity_code))
    sqlValues = "','".join(activity_code)
    sql = "insert into activity_code (activity_code) values (" + sqlValues + ")"
    connectDB(sql)
