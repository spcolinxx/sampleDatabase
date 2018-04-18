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
            return [False,["excel文件格式有问题，请按照标准格式导入excel文件！"]]

        comp_item=["样本编码","入库日期","保存温度","样本量","知情同意","样本别称","采集部位","保存机构名称","法人机构名称","法人机构代码"
            ,"捐献者匿名编号","性别","年龄","课题编号"]

        complete_cap=True


        for i in comp_item:
            if i not in xls_cap:
                complete_cap=False
                err_info.append("'"+i+"'必选字段缺失，请检查！")

        if complete_cap==False:
            return [False,err_info]
        else:
            ls=[]
            for i in range(1,rows):
                rowValues = table.row_values(i)  # 某一行数据
                tmp=[]
                random.seed(time.time())
                # st1 = str(random.randint(0, 99999)).zfill(5)
                # random.seed(time.time())
                # st2 = str(random.randint(0, 99999)).zfill(5)
                # st = "smp" + str(int(time.time()))+st1 + st2
                st=str(rowValues[0])+str(rowValues[20])
                tmp.append(st)

                for item in rowValues:
                    tmp.append(item)

                ls.append(tmp)

            ln=len(ls)

            for i in range(ln):
                if ls[i][9]==0:
                    ls[i][9]=False
                else:
                    ls[i][9]=True

                if int(ls[i][6])==ls[i][6]:
                    ls[i][6]=int(ls[i][6])

                if int(ls[i][7])==ls[i][7]:
                    ls[i][7]=int(ls[i][7])

                if int(ls[i][31])==ls[i][31]:
                    ls[i][31]=int(ls[i][31])

                if int(ls[i][35])==ls[i][35]:
                    ls[i][35]=int(ls[i][35])
                if int(ls[i][61])==ls[i][61]:
                    ls[i][61]=int(ls[i][61])



            return [True,ls]


