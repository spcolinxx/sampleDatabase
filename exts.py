# 此模块是为解决循环引用创建

from flask_sqlalchemy import SQLAlchemy
import pymysql
from pymongo import MongoClient
import configparser,os

ormdb=SQLAlchemy()


def create_sqldb_conn():
    sqldb=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='lcp3281038',db='sampledb',charset='utf8')

    sqldb.autocommit(False)

    return sqldb






def create_mongo_cnn():
    path=os.path.dirname(os.path.abspath(__file__))
    conf_file_path=path+"/database.conf"
    cf = configparser.ConfigParser()
    cf.read(conf_file_path)

    db_ip=cf.get("db","db_ip")
    db_name=cf.get("db","db_name")
    db_user=cf.get("db","db_user")
    db_password=cf.get("db","db_password")
    uri="mongodb://"+db_user+":"+db_password+"@"+db_ip+"/"+db_name

    # uri = "mongodb://admin:123@localhost/sampledb"
    cnn = MongoClient(uri)

    return cnn

