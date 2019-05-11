#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:BOB-Y
# datetime:2019/5/6 20:19
# software: PyCharm
from flask import Flask, url_for
from flask import render_template
from flask import request
import traceback
import pymysql



#查询用户名及密码是否匹配及存在
    #连接数据库,此前在数据库中创建数据库TESTDB
db = pymysql.connect("192.168.1.221","root","cmdbcmdb","WECHAT_DATA" )
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 查询语句
#sql = "select * from WECHAT_USER_INFOR where user=" + request.args.get('user') + " and password=" + request.args.get('password') + ""
sql = "select * from WECHAT_USER_INFOR where user=" + '2 ' + " and password=" + '1' + ""

try:
    # 执行sql语句
    cursor.execute(sql)
    results = cursor.fetchall()

    print(len(results))
    if len(results)==1:
        print(2222222222)#return '登录成功'
    else:
        print(11111)
        #return '用户名或密码不正确'
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    traceback.print_exc()
    db.rollback()
# 关闭数据库连接
db.close()