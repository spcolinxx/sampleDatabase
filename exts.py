# 此模块是为解决循环引用创建

from flask_sqlalchemy import SQLAlchemy
import pymysql

ormdb=SQLAlchemy()


def create_sqldb_conn():
    sqldb=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='lcp3281038',db='sampledb',charset='utf8')

    sqldb.autocommit(False)

    return sqldb