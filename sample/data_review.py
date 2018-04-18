from exts import db
from models import SampleInfo

def dup_check(dt):

    for i in dt:
        exst=SampleInfo.query.filter(SampleInfo.inv_id==i[1],SampleInfo.org_name==i[21]).all()
        ln=len(exst)

        if ln>0:
            return i[1]

    return False





















# import time
#
# # 判断日期有效函数
# def valid_date(dt):
#     try:
#         time.strptime(dt, "%Y-%m-%d")
#         return True
#     except:
#         return False
#
# def isnumber(aString):
#     try:
#         float(aString)
#         return True
#     except:
#         return False
#
#
#
#
# def dt_review(ls):
#
#     ln=len(ls)
#
#     rst=[]
#
#     for i in range(ln):
#         if ls[i][0]=="":
#             rst.append("第"+str(i)+"条数据缺失<样本编码>字段")
#         if ls[i][2]=="":
#             rst.append("第" + str(i) + "条数据缺失<入库日期>字段")
#         elif valid_date(str(ls[i][2]))==False:
#             rst.append("第"+str(i)+"条数据<入库日期>为无效日期")
#         else:
#             pass
#
#         if ls[i][3]=="":
#             rst.append("第" + str(i) + "条数据缺失<保存温度>字段")
#
#         if ls[i][6]=="":
#             rst.append("第" + str(i) + "条数据缺失<样本量>字段")
#         elif isnumber(ls[i][6])==False:
#             rst.append("第"+str(i)+"条数据<样本量>为无效数字")
#         else:
#             pass
#
#         if ls[i][8]=="":
#             rst.append("第" + str(i) + "条数据缺失<知情同意>字段")
#         if ls[i][9]=="":
#             rst.append("第" + str(i) + "条数据缺失<样本别称>字段")
#         if ls[i][13]=="":
#             rst.append("第" + str(i) + "条数据缺失<采集部位>字段")
#         if ls[i][20] == "":
#             rst.append("第" + str(i) + "条数据缺失<保存机构名称>字段")
#         if ls[i][21]=="":
#             rst.append("第" + str(i) + "条数据缺失<法人机构名称>字段")
#         if ls[i][22]=="":
#             rst.append("第" + str(i) + "条数据缺失<法人机构代码>字段")
#         if ls[i][32]=="":
#             rst.append("第" + str(i) + "条数据缺失<捐献者匿名编号>字段")
#         if ls[i][33]=="":
#             rst.append("第" + str(i) + "条数据缺失<性别>字段")
#         if ls[i][34]=="":
#             rst.append("第" + str(i) + "条数据缺失<年龄>字段")
#         if isnumber(ls[i][34])==False:
#             rst.append("第" + str(i) + "条数据<年龄>为无效数字")
#         if (int(ls[i][34])<0)|(int(ls[i][34])>150)==True:
#             rst.append("第" + str(i) + "条数据<年龄>超出正常范围")
#         if ls[i][53]=="":
#             rst.append("第" + str(i) + "条数据缺失<课题编号>字段")
#
#
#     return rst
