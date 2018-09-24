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

for i in range(10):
    # table.write(i, 0,''.join(random.sample(string.ascii_letters + string.digits, 20)) )             #唯一标识码
    table.write(i, 0,"库存编码"+str(i) )              #库存编码
    table.write(i, 1,"GNG0" )             #样本类别
    table.write(i, 2,"室温" )             #保存方式
    table.write(i, 3,random.randint(1, 254))                                                        #每份样本数量
    table.write(i, 4,time.strftime("%Y-%m-%d",time.localtime(random.randint(start,end))) )          #采集时间
    table.write(i, 5,"保存机构名称test")             #保存机构名称
    table.write(i, 6,"法人机构代码"+str(i) )             #法人机构代码
    table.write(i, 7,"法人机构类型"+str(i) )             #法人机构类型
    table.write(i, 8,"保存机构简介"+str(i) )             #保存机构简介
    table.write(i, 9,"通信地址"+str(i) )             #通讯地址
    table.write(i, 10,"邮政编码"+str(i) )             #邮政编码
    table.write(i, 11,"管理员"+str(i) )             #联系人姓名
    table.write(i, 12,random.randint(1, 254) )       #联系电话
    table.write(i, 13,"电子信箱"+str(i) )             #电子邮箱
    table.write(i, 14,"捐献者匿名编号"+str(i) )             #捐献人编号
    table.write(i, 15,"男" )                         #性别
    table.write(i, 16,random.randint(1, 150) )                                                       #年龄
    table.write(i, 17,"民族"+str(i) )             #民族
    table.write(i, 18,"籍贯"+str(i) )             #籍贯
    table.write(i, 19,"出生地"+str(i))             #出生地
    table.write(i, 20,"疾病名称"+str(i) )       #疾病名称
    table.write(i, 21,"正常人群"+str(i))             #正常人群


file.save('test.xls')


