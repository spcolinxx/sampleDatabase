from lxml import html
from io import StringIO
import sys
etree=html.etree


schema_doc=etree.parse(sys.path[0]+"/sample/scm.xsd")
xmlschema=etree.XMLSchema(schema_doc)
item_list=["invId","samCateName","entDate","storMeth","parentId","batchCount","samQTY","unit","consent",
           "samTitle","samDesc","keyWord","samUse","organ","sPreC","acquiFor","acquiDate",
           "acquiPlan","acquiOrg","acquiAssis","orgName","jurPerName","jurPerId","jurPerType",
           "orgIntro","usePerm","shareWay","addr","postCode","manager","tel","email","donId",
           "sex","age","ethGroup","nativePla","birPla","nation","occup","edu","mariState","donWay",
           "diseName","diseId","diag","diseHis","exaRec","interRec","mediaRec","mediRep","famHis",
           "projName","projId","projLevel","sponOrg","intakeLevel","projKeyword","aim","mtd","total_amt",
           "beEndTime"]


def get_valid_str(smp):

    hd_str="""<sampleinfo xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="scm.xsd">"""
    tl_str="""</sampleinfo>"""
    content_str=""""""

    for i in range(len(smp)):
        if smp!='':
            content_str=content_str+"<"+item_list[i]+">"+str(smp[i])+"</"+item_list[i]+">"

    print(hd_str+content_str+tl_str)

    valid_str=StringIO(hd_str+content_str+tl_str)



    # valid_str=StringIO("""
    # <sampleinfo xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="scm.xsd">
    #
    #     <invId>"""+smp[1]+""""</invId>
    #     <entDate>"""+smp[3]+"""</entDate>
    #     <storMeth>"""+smp[4]+"""</storMeth>
    #     <samQTY>"""+str(int(smp[7]))+"""</samQTY>
    #     <consent>"""+str(smp[9]).lower()+"""</consent>
    #     <samTitle>"""+smp[10]+"""</samTitle>
    #     <organ>"""+smp[14]+"""</organ>
    #     <orgName>"""+smp[21]+"""</orgName>
    #     <jurPerName>"""+smp[22]+"""</jurPerName>
    #     <jurPerId>"""+smp[23]+"""</jurPerId>
    #     <donId>"""+smp[33]+"""</donId>
    #     <sex>"""+smp[34]+"""</sex>
    #     <age>"""+str(int(smp[35]))+"""</age>
    #     <projId>"""+smp[54]+"""</projId>
    #
    # </sampleinfo>
    # """)
    #
    #
    #
    #
    return valid_str


# xml=etree.parse(valid_str)
# print(xmlschema.validate(xml))
# print(xmlschema.error_log)



def schema_check(dt):
    err_log=[]
    for i in range(len(dt)):
        valid_str=get_valid_str(dt[i][1:])
        xml=etree.parse(valid_str)
        xmlschema.validate(xml)
        if xmlschema.error_log:
            # print(i,list(xmlschema.error_log))
            err_log.append([i,xmlschema.error_log])

    return err_log
