from exts import sqldb

def sampleinfo_insert(dt):
    cursor=db2.cursor()
    sql="insert ignore into sampleinfo values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.executemany(sql,dt)
    db2.commit()

def orginfo_insert(dt):
    cursor=db2.cursor()
    sql="insert ignore into orginfo values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.executemany(sql,dt)
    db2.commit()

def donorinfo_insert(dt):
    cursor=db2.cursor()
    sql="insert ignore into donorinfo values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.executemany(sql,dt)
    db2.commit()

def projectinfo_insert(dt):
    cursor=db2.cursor()
    sql="insert ignore into projectinfo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.executemany(sql,dt)
    db2.commit()






# cursor=db2.cursor()
#
# sql3="insert into userinfo values(%s,%s,%s)"
# cursor.executemany(sql3,a)
#
#
# db2.commit()
#
#
#
# db2.close()
