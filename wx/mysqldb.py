#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:BOB-Y
# datetime:2019/4/25 10:12
# software: PyCharm

import pymysql
pymysql.install_as_MySQLdb()

class DBmysql(object):
    def __init__(self, host, port, user, passwd, db ):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.conn = None
        self.cur = None
        try:
            self.conn = pymysql.connect(host = self.host, port = self.port, user = self.user, passwd = self.passwd, db= self.db)
            self.cur = self.conn.cursor()
        except:
            raise Exception("DataBase connect error,please check the db config!!!")
    def close(self):
#      if not self.conn:
        self.conn.commit()
        self.cur.close()
        self.conn.close()
#       else:
#            raise Exception("DataBase doesn't connect,close connectiong error;please check the db config!!!")