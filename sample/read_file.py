import xlrd
import time,random



def read_file(file):
    table=file.sheets()[0]
    rows=table.nrows
    cols=table.ncols

    if cols<62:
        return [False,["数据字段数少于规定字段数，请检查！"]]
    else:
        #用于返回提示信息的数组
        err_info = []

        # 去掉字段名中的空格
        xls_cap=table.row_values(0)

        try:
            for i in xls_cap:
                i.replace(' ','')

        except:
            return [False,["excel文件格式有问题，请按照规范格式导入excel文件！"]]

        # comp_item=["样本编码","入库日期","保存温度","样本量","知情同意","样本别称","采集部位","保存机构名称","法人机构名称","法人机构代码"
        #     ,"捐献者匿名编号","性别","年龄","课题编号"]

        comp_item=["样本编码","样本类别","入库日期","保存温度","母本编码","分管数","样本量","量单位","知情同意","样本别称","样本描述","关键词","样本用途","采集部位","分析前变量"
            , "采集动因","采集时间","采集计划","采集机构","其他采集者","保存机构名称","法人机构名称","法人机构代码","法人机构类型","保存机构简介","使用许可","共享方式","通信地址",
                   "邮政编码","管理员","联系电话","电子信箱","捐献者匿名编号","性别"
            , "年龄","民族","籍贯","出生地","国籍","职业","教育程度","婚姻状况","捐献途径","疾病类目名称","疾病类目代码","主要诊断","现病史","检验记录","随访记录","影像资料","病例报告","家系信息"
            , "课题名称","课题编号","课题级别","资助机构","纳入标准","课题关键词","收集目的","收集方法","收集数量","起止时间"]
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

                st=str(rowValues[0])+str(rowValues[20])
                tmp.append(st)

                for item in rowValues:
                    tmp.append(item)

                ls.append(tmp)

            ln=len(ls)

            for i in range(ln):
                pass
                if ls[i][9]==0:
                    ls[i][9]=False
                else:
                    ls[i][9]=True

                try:
                    if int(ls[i][6])==ls[i][6]:
                        ls[i][6]=int(ls[i][6])
                except:
                    pass

                try:
                    if int(ls[i][7])==ls[i][7]:
                        ls[i][7]=int(ls[i][7])
                except:
                    pass

                try:
                    if int(ls[i][31])==ls[i][31]:
                        ls[i][31]=int(ls[i][31])
                except:
                    pass
                try:
                    if int(ls[i][35])==ls[i][35]:
                        ls[i][35]=int(ls[i][35])
                except:
                    pass

                try:
                    if int(ls[i][61])==ls[i][61]:
                        ls[i][61]=int(ls[i][61])
                except:
                    pass


            return [True,ls]


