#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

'''
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
'''

import genCode
import pymysql


def connectDB(sql):
    # 打开数据库连接      ip         用户名  密码   数据名称
    conn = pymysql.connect("localhost","root","root","py_test" ) 
     
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()
     
    # 使用 execute()  方法执行 SQL 查询 
    rows = cursor.execute(sql)
    print("影响行数：%d" % rows)
    #需要注意的是:在执行完插入或删除或修改操作后,需要调用一下conn.commit()方法进行提交.这样,数据才会真正保存在数据库中。
    #否则数据不会保留在数据库中，rows也不会为0
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    activity_code = genCode.genCode(200)
    #print("','".join(activity_code))
    sqlValues = "'),('".join(activity_code)
    sql = "insert into activity_code (activity_code) values ('" + sqlValues + "')"
    #print(sql)
    connectDB(sql)
