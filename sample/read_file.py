import xlrd
import time,random
from datetime import datetime
from xlrd import xldate_as_datetime


def read_file(file,upload_time):
    table=file.sheets()[0]
    rows=table.nrows
    cols=table.ncols


    if cols<22:
        return [False,["数据字段数少于规定字段数，请检查！"]]
    else:
        #用于返回提示信息的数组
        err_info = []

        # 表头
        xls_cap=table.row_values(0)



        # 去掉字段名中的空格
        try:
            for i in xls_cap:
                i.replace(' ','')
        except:
            return [False,["excel文件格式有问题，请按照规范格式导入excel文件！"]]


        comp_item=["库存编码","样本类别","保存方式","每份样本数量","采集时间","保存机构名称","法人机构代码","法人机构类型","保存机构简介","通讯地址",
                   "邮政编码","联系人姓名","联系电话","电子邮箱","捐献人编号","性别", "年龄","民族","籍贯","出生地","疾病名称","正常人群"]
        complete_cap=True


        for i in comp_item:
            if i not in xls_cap:
                complete_cap=False
                err_info.append("'"+i+"'字段缺失，请检查！")

        if complete_cap==False:
            return [False,err_info]
        else:
            ls=[]
            for i in range(1,rows):
                rowValues = table.row_values(i)  # 某一行数据
                tmp=[]

                st=str(rowValues[0])+str(rowValues[5])+str(upload_time).replace(' ','')
                tmp.append(st)

                for item in rowValues:
                    tmp.append(item)


                ls.append(tmp)

            ln=len(ls)

            for i in range(ln):

                #excel读进来会将所有数字转化为浮点数，需要手动转化为整数

                try:
                    if int(ls[i][11])==ls[i][11]:
                        ls[i][11]=int(ls[i][11])
                except:
                    pass

                try:
                    if int(ls[i][17])==ls[i][17]:
                        ls[i][17]=int(ls[i][17])
                except:
                    pass

                # print(ls[i][5])
                try:
                    ls[i][5]=xldate_as_datetime(ls[i][5],0).strftime("%Y-%m-%d")
                except:
                    pass


            return [True,ls]


