from lxml import html
from io import StringIO
import sys
etree=html.etree


# item_list=["","samCateName","入库日期","storMeth","parentId","batchCount","samQTY","unit","consent",
#            "samTitle","samDesc","keyWord","samUse","organ","sPreC","acquiFor","acquiDate",
#            "acquiPlan","acquiOrg","acquiAssis","orgName","jurPerName","jurPerId","jurPerType",
#            "orgIntro","usePerm","shareWay","addr","postCode","manager","tel","email","donId",
#            "sex","age","ethGroup","nativePla","birPla","nation","occup","edu","mariState","donWay",
#            "diseName","diseId","diag","diseHis","exaRec","interRec","mediaRec","mediRep","famHis",
#            "projName","projId","projLevel","sponOrg","intakeLevel","projKeyword","aim","mtd","total_amt",
#            "beTime","endTime"]

schema_doc=etree.parse(sys.path[0]+"/sample/scm.xsd")
xmlschema=etree.XMLSchema(schema_doc)
item_list=["样本编码","样本类别","入库日期","保存温度","母本编码","分管数","样本量","量单位","知情同意",
           "样本别称","样本描述","关键词","样本用途","采集部位","分析前变量","采集动因","采集时间",
           "采集计划","采集机构","其他采集者","保存机构名称","法人机构名称","法人机构代码","法人机构类型",
           "保存机构简介","使用许可","共享方式","通信地址","邮政编码","管理员","联系电话","电子信箱","捐献者匿名编号",
           "性别","年龄","民族","籍贯","出生地","国籍","职业","教育程度","婚姻状况","捐献途径",
           "疾病类目名称","疾病类目代码","主要诊断","现病史","检验记录","随访记录","影像资料","病例报告","家系信息",
           "课题名称","课题编号","课题级别","资助机构","纳入标准","课题关键词","收集目的","收集方法","收集数量",
           "课题开始时间","课题结束时间"]


def get_valid_str(smp):

    hd_str="""<sampleinfo xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="scm.xsd">"""
    tl_str="""</sampleinfo>"""
    content_str=""""""

    for i in range(len(smp)):
        if smp[i]!='':
            content_str=content_str+"<"+item_list[i]+">"+str(smp[i])+"</"+item_list[i]+">"


    valid_str=StringIO(hd_str+content_str+tl_str)

    return valid_str





def schema_check(dt):
    err_log=[]
    for i in range(len(dt)):
        valid_str=get_valid_str(dt[i][1:])
        xml=etree.parse(valid_str)
        xmlschema.validate(xml)
        if xmlschema.error_log:
            if i<100:
                err_log.append([i,xmlschema.error_log])


    return err_log
