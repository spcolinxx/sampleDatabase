import xlwt
import random
import time
import string

# ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))

a1=(1976,1,1,0,0,0,0,0,0)              #设置开始日期时间元组（1976-01-01 00：00：00）
a2=(1990,12,31,23,59,59,0,0,0)    #设置结束日期时间元组（1990-12-31 23：59：59）

start=time.mktime(a1)    #生成开始时间戳
end=time.mktime(a2)      #生成结束时间戳



file = xlwt.Workbook() #注意这里的Workbook首字母是大写，无语吧

table = file.add_sheet('sheet1')

for i in range(10000):
    # table.write(i, 0,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #唯一标识码
    table.write(i, 0,''.join(random.sample(string.ascii_letters + string.digits, 20)) )                                                                        #样本编码
    table.write(i, 1,"GNG0" )             #样本类别
    table.write(i, 2,time.strftime("%Y-%m-%d",time.localtime(random.randint(start,end))) )          #入库日期
    table.write(i, 3,"室温" )             #保存温度
    table.write(i, 4,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #母本编码
    table.write(i, 5,random.randint(1, 254))                                                        #分管数
    table.write(i, 6,random.randint(1, 254))                                                        #样本量
    table.write(i, 7,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #量单位
    table.write(i, 8,random.choice([True, False]) )                                                 #知情同意
    table.write(i, 9,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #样本别称
    table.write(i, 10,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #样本描述
    table.write(i, 11,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #关键词
    table.write(i, 12,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #样本用途
    table.write(i, 13,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #采集部位
    table.write(i, 14,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #分析前变量
    table.write(i, 15,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #采集动因
    table.write(i, 16,time.strftime("%Y-%m-%d",time.localtime(random.randint(start,end))) )          #采集时间
    table.write(i, 17,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #采集计划
    table.write(i, 18,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #采集机构
    table.write(i, 19,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #其他采集者
    table.write(i, 20,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #保存机构名称
    table.write(i, 21,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #法人机构名称
    table.write(i, 22,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #法人机构代码
    table.write(i, 23,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #法人机构类型
    table.write(i, 24,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #保存机构简介
    table.write(i, 25,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #使用许可
    table.write(i, 26,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #共享方式
    table.write(i, 27,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #通信地址
    table.write(i, 28,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #邮政编码
    table.write(i, 29,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #管理员
    table.write(i, 30,random.randint(1, 254) )                                                      #联系电话
    table.write(i, 31,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #电子邮箱
    table.write(i, 32,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #捐献者匿名编号
    table.write(i, 33,"男" )             #性别
    table.write(i, 34,random.randint(1, 150) )                                                       #年龄
    table.write(i, 35,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #民族
    table.write(i, 36,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #籍贯
    table.write(i, 37,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #出生地
    table.write(i, 38,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #国籍
    table.write(i, 39,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #职业
    table.write(i, 40,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #教育程度
    table.write(i, 41,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #婚姻状况
    table.write(i, 42,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #捐献途径
    table.write(i, 43,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #疾病类目名称
    table.write(i, 44,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #疾病类目代码
    table.write(i, 45,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #主要诊断
    table.write(i, 46,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #现病史
    table.write(i, 47,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #检验记录
    table.write(i, 48,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #随访记录
    table.write(i, 49,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #影像资料
    table.write(i, 50,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #病例报告
    table.write(i, 51,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #家系信息
    table.write(i, 52,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #课题名称
    table.write(i, 53,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #课题编号
    table.write(i, 54,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #课题级别
    table.write(i, 55,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #资助机构
    table.write(i, 56,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #纳入标准
    table.write(i, 57,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #课题关键词
    table.write(i, 58,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #收集目的
    table.write(i, 59,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #收集方法
    table.write(i, 60,random.randint(1, 255) )                                                       #收集数量
    table.write(i, 61,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #起止时间



file.save('wdemo.xls')




#
# #随机生成10个日期字符串
# for i in range(10):
#     t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
#     date_touple=time.localtime(t)          #将时间戳生成时间元组
#     date=time.strftime("%Y-%m-%d",date_touple)  #将时间元组转成格式化字符串（1976-05-21）
#     print(date)