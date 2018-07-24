import configparser

cf = configparser.ConfigParser()
cf.read("database.conf")
db_ip=cf.get("db","db_ip")
db_name=cf.get("db","db_name")
db_user=cf.get("db","db_user")
db_password=cf.get("db","db_password")
uri="mongodb://"+db_user+":"+db_password+"@"+db_ip+"/"+db_name

print(uri)




# import time
#
# now_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print(now_time)
# format_time=now_time.replace('-','')
# format_time=format_time.replace(' ','')
# format_time=format_time.replace(':','')
# print(format_time)


# from pymongo import MongoClient
#
# try:
#
#     uri = "mongodb://admin:123@localhost/sampledb"
#
#     cnn = MongoClient(uri)
#
#     db = cnn.sampledb
#
#     cl = db.catecode
#     ls1 = [{'cate_name':'大体样本','cate_level':1,'cate_mark':'G'},
#            {'cate_name': '组织', 'cate_level':1, 'cate_mark':'T'},
#           {'cate_name': '血液', 'cate_level':1, 'cate_mark':'B'},
#           {'cate_name': '头发、指甲', 'cate_level':1, 'cate_mark':'H'},
#           {'cate_name': '细胞混悬液', 'cate_level':1, 'cate_mark':'C'},
#           {'cate_name': '排泄物', 'cate_level':1, 'cate_mark':'E'},
#           {'cate_name': '分泌物', 'cate_level':1, 'cate_mark':'S'},
#           {'cate_name': '精液', 'cate_level':1, 'cate_mark':'M'},
#           {'cate_name': '干细胞', 'cate_level':1, 'cate_mark':'T'}]
#     ls2=[{'cate_name':'正常大体样本','cate_level':2,'cate_mark':'NG'},
#          {'cate_name': '病理大体样本', 'cate_level':2, 'cate_mark':'PG'},
#          {'cate_name': '肿瘤组织', 'cate_level':2, 'cate_mark':'T'},
#          {'cate_name': '癌旁组织', 'cate_level':2, 'cate_mark':'P'},
#          {'cate_name': '正常组织', 'cate_level':2, 'cate_mark':'N'},
#          {'cate_name': '转移组织', 'cate_level':2, 'cate_mark':'M'},
#          {'cate_name': '全血滤纸片', 'cate_level':2, 'cate_mark':'BB'},
#          {'cate_name': '血浆', 'cate_level':2, 'cate_mark':'BP'},
#          {'cate_name': '白细胞', 'cate_level':2, 'cate_mark':'BW'},
#          {'cate_name': '血清', 'cate_level':2, 'cate_mark':'BS'},
#          {'cate_name': '红细胞', 'cate_level':2, 'cate_mark':'BE'},
#          {'cate_name': '血小板', 'cate_level':2, 'cate_mark':'BT'},
#          {'cate_name': '血凝块', 'cate_level':2, 'cate_mark':'BC'},
#          {'cate_name': '头发（需包含毛囊）', 'cate_level':2, 'cate_mark':'HA'},
#          {'cate_name': '指甲', 'cate_level':2, 'cate_mark':'NA'},
#          {'cate_name': '脑脊液', 'cate_level':2, 'cate_mark':'C'},
#          {'cate_name': '胸腔积液', 'cate_level':2, 'cate_mark':'H'},
#          {'cate_name': '心包液', 'cate_level':2, 'cate_mark':'P'},
#          {'cate_name': '腹腔积液', 'cate_level':2, 'cate_mark':'A'},
#          {'cate_name': '关节腔液', 'cate_level':2, 'cate_mark':'J'},
#          {'cate_name': '尿液', 'cate_level':2, 'cate_mark':'U'},
#          {'cate_name': '粪便', 'cate_level':2, 'cate_mark':'F'},
#          {'cate_name': '唾液', 'cate_level':2, 'cate_mark':'S'},
#          {'cate_name': '乳汁', 'cate_level':2, 'cate_mark':'L'},
#          {'cate_name': '汗液', 'cate_level':2, 'cate_mark':'H'},
#          {'cate_name': '宫颈分泌物', 'cate_level':2, 'cate_mark':'C'},
#          {'cate_name': '口腔分泌物', 'cate_level':2, 'cate_mark':'O'},
#          {'cate_name': '精液', 'cate_level':2, 'cate_mark':'SE'},
#          {'cate_name': '精浆', 'cate_level':2, 'cate_mark':'SP'},
#          {'cate_name': '精子', 'cate_level':2, 'cate_mark':'SM'},
#          {'cate_name': '胚胎干细胞', 'cate_level':2, 'cate_mark':'ST'},
#          {'cate_name': '成体干细胞', 'cate_level':2, 'cate_mark':'AS'},
#          {'cate_name': '造血干细胞', 'cate_level':2, 'cate_mark':'HS'},
#          {'cate_name': '神经干细胞', 'cate_level':2, 'cate_mark':'NS'},]
#     ls3=[{'cate_name':'省缺','cate_level':3,'cate_mark':''},
#          {'cate_name': '新鲜组织', 'cate_level':3, 'cate_mark':'F'},
#          {'cate_name': '冰冻组织', 'cate_level':3, 'cate_mark':'R'},
#          {'cate_name': 'OTC包埋冰冻组织', 'cate_level':3, 'cate_mark':'O'},
#          {'cate_name': '石蜡包埋组织', 'cate_level':3, 'cate_mark':'A'},
#          {'cate_name': '脑脊液', 'cate_level':3, 'cate_mark':'E'},
#          {'cate_name': '脑脊液上清', 'cate_level':3, 'cate_mark':'S'},
#          {'cate_name': '脑脊液细胞', 'cate_level':3, 'cate_mark':'C'},
#          {'cate_name': '胸腔积液', 'cate_level':3, 'cate_mark':'H'},
#          {'cate_name': '胸腔积液上清', 'cate_level':3, 'cate_mark':'S'},
#          {'cate_name': '胸腔积液细胞', 'cate_level':3, 'cate_mark':'C'},
#          {'cate_name': '心包液', 'cate_level':3, 'cate_mark':'E'},
#          {'cate_name': '心包液上清', 'cate_level':3, 'cate_mark':'S'},
#          {'cate_name': '心包液细胞', 'cate_level':3, 'cate_mark':'C'},
#          {'cate_name': '腹腔积液', 'cate_level':3, 'cate_mark':'B'},
#          {'cate_name': '腹腔积液上清', 'cate_level':3, 'cate_mark':'S'},
#          {'cate_name': '腹腔积液细胞', 'cate_level':3, 'cate_mark':'C'},
#          {'cate_name': '关节腔液', 'cate_level':3, 'cate_mark':'O'},
#          {'cate_name': '关节腔液上清', 'cate_level':3, 'cate_mark':'S'},
#          {'cate_name': '关节腔液细胞', 'cate_level':3, 'cate_mark':'C'},
#          {'cate_name': '尿液', 'cate_level':3, 'cate_mark':'R'},
#          {'cate_name': '尿液上清', 'cate_level':3, 'cate_mark':'S'},
#          {'cate_name': '尿沉渣', 'cate_level':3, 'cate_mark':'A'},
#          {'cate_name': '粪便', 'cate_level':3, 'cate_mark':'A'},
#          {'cate_name': '全唾液', 'cate_level':3, 'cate_mark':'S'},
#          {'cate_name': '颔下腺唾液', 'cate_level':3, 'cate_mark':'M'},
#          {'cate_name': '舌下腺唾液', 'cate_level':3, 'cate_mark':'L'},
#          {'cate_name': '腮腺唾液', 'cate_level':3, 'cate_mark':'R'},
#          {'cate_name': '乳汁', 'cate_level':3, 'cate_mark':'A'},
#          {'cate_name': '汗液', 'cate_level':3, 'cate_mark':'I'},
#          {'cate_name': '宫颈粘液', 'cate_level':3, 'cate_mark':'E'},
#          {'cate_name': '宫颈脱落细胞', 'cate_level':3, 'cate_mark':'C'},
#          {'cate_name': '口腔粘液', 'cate_level':3, 'cate_mark':'S'},
#          {'cate_name': '口腔粘液细胞', 'cate_level':3, 'cate_mark':'C'}]
#     ls4=[{'cate_name':'省缺','cate_level':4,'cate_mark':'0'},
#     {'cate_name': 'DNA', 'cate_level':4, 'cate_mark': '1'},
#     {'cate_name': 'RNA', 'cate_level':4, 'cate_mark': '2'},
#     {'cate_name': '蛋白质', 'cate_level':4, 'cate_mark': '3'}]
#
#     cl.insert(ls4, continue_on_error=True)
#
#
#     cnn.close()
#
#
# except Exception as e:
#     print(e)



# import datetime
# a="1923-1-3"
# b=datetime.datetime.strptime(a,"%Y-%m-%d")
#
# print(b)



# import exts
#
# cnn=exts.create_sqldb_conn()
# cursor=cnn.cursor()
#
# sql="insert into testtb values('1','2','1')"
# cursor.execute(sql)
# cnn.commit()
# # rst=cursor.fetchall()
#
# cursor.close()
# cnn.close()
# sql='select * from sampleinfo JOIN orginfo ON sampleinfo.org_name=orginfo.org_name JOIN donorinfo ON sampleinfo.don_id=donorinfo.don_id JOIN ' \
#     'projectinfo ON sampleinfo.proj_id=projectinfo.prj_id where sam_cate_name="GNG0"'
#
# cursor.execute(sql)
#
# rst=cursor.fetchall()
#
# for i in rst:
#     print(len(i))
#     print(i)
# cursor.close()
# cnn.close()

# 日期问题用js解决，忽略日期select的名字，那样select就不会提交
# 不同表中字段名重复问题：直接将html标签名改为表名+标签名
