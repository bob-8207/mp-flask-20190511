#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:BOB-Y
# datetime:2019/5/6 17:42
# software: PyCharm

from flask import Flask, url_for
from flask import render_template
from flask import request
import traceback
import pymysql

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login1.html')

@app.route('/regist')
def regist():
    return render_template('regist1.html')


@app.route('/registuser')
def getRigistRequest():
    regist_user = request.args.get('user')
    regist_password = request.args.get('password')
    regist_phone_number = request.args.get('phone_number')
    db = pymysql.connect("192.168.1.221", "root", "cmdbcmdb", "WECHAT_DATA")
    cursor = db.cursor()
    #sql = "INSERT INTO WECHAT_USER_INFOR(user, password, phone_number) VALUES ("+request.args.get('user')+", "+request.args.get('password')+", "+request.args.get('phone_number')+")"
    sql = "INSERT INTO WECHAT_USER_INFOR(user, password, phone_number) VALUES ('%s', '%s', '%s')"%(regist_user,regist_password,regist_phone_number)

    try:

        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
         #注册成功之后跳转到登录页面
        return render_template('login1.html')
    except:
        #抛出错误信息
        traceback.print_exc()
        # 如果发生错误则回滚
        db.rollback()
        return '注册失败'
    # 关闭数据库连接
    db.close()

#获取登录参数及处理
@app.route('/login')
def getLoginRequest():
#查询用户名及密码是否匹配及存在
    login_user = request.args.get('user')
    login_password = request.args.get('password')
    #连接数据库,此前在数据库中创建数据库TESTDB
    db = pymysql.connect("192.168.1.221","root","cmdbcmdb","WECHAT_DATA" )
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "select * from WECHAT_USER_INFOR where user ="+ login_user +" and password ="+ login_password +""
    #sql = "select * from WECHAT_USER_INFOR where user="+request.args.get('user')+" and password="+request.args.get('password')+""
    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()
        print(len(results))
        if len(results)==1:
            return '登录成功'
        else:
            return '用户名或密码不正确'
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
        return '请输入有效的用户名和密码'
    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
