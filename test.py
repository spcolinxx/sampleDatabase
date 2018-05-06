import exts

cnn=exts.create_sqldb_conn()
cursor=cnn.cursor()
sql='select * from sampleinfo JOIN orginfo ON sampleinfo.org_name=orginfo.org_name JOIN donorinfo ON sampleinfo.don_id=donorinfo.don_id JOIN ' \
    'projectinfo ON sampleinfo.proj_id=projectinfo.prj_id where sam_cate_name="GNG0"'

cursor.execute(sql)

rst=cursor.fetchall()

for i in rst:
    print(len(i))
    print(i)
cursor.close()
cnn.close()

# 日期问题用js解决，忽略日期select的名字，那样select就不会提交
# 不同表中字段名重复问题：直接将html标签名改为表名+标签名
