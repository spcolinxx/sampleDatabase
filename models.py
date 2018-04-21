from exts import ormdb

from flask.ext.login import UserMixin

class SampleInfo(ormdb.Model):
    __tablename__="sampleinfo"                      #表名
    sam_uni_id=ormdb.Column(ormdb.String(300),nullable=False,primary_key=True)            #唯一表示码

    inv_id=ormdb.Column(ormdb.String(500))               #样本编码
    sam_cate_name=ormdb.Column(ormdb.String(500))         #样本类别
    ent_date=ormdb.Column(ormdb.Date)                      #入库日期
    stor_meth = ormdb.Column(ormdb.String(500))           # 保存温度
    parent_id=ormdb.Column(ormdb.String(500))             #母本编码
    batch_count=ormdb.Column(ormdb.Integer)                #分管数
    sam_qty=ormdb.Column(ormdb.Integer)                   #样本量
    unit_amou=ormdb.Column(ormdb.String(500))             #量单位
    consent=ormdb.Column(ormdb.Boolean)                   #知情同意
    sam_title=ormdb.Column(ormdb.String(500))             #样本别称
    sam_desc=ormdb.Column(ormdb.Text)                     #样本描述
    keyword=ormdb.Column(ormdb.String(500))               #关键词
    sam_uses=ormdb.Column(ormdb.String(500))              #样本用途
    acqui_pos=ormdb.Column(ormdb.String(500))             #采集部位
    s_pre_c=ormdb.Column(ormdb.String(500))               #分析前变量
    acqui_mot=ormdb.Column(ormdb.String(500))             #采集动因
    acqui_time=ormdb.Column(ormdb.Date)                   #采集时间
    acqui_plan=ormdb.Column(ormdb.Text)                   #采集计划
    acqui_org=ormdb.Column(ormdb.String(500))             #采集机构
    acqui_assis=ormdb.Column(ormdb.String(500))           #其他采集者
    org_name = ormdb.Column(ormdb.String(500))           # 保存机构名称
    don_id = ormdb.Column(ormdb.String(500))             # 捐献者匿名编号
    proj_id=ormdb.Column(ormdb.String(500 ))               #课题编号


class OrgInfo(ormdb.Model):
    __tablename__="orginfo"
    org_name=ormdb.Column(ormdb.String(500),primary_key=True)     #保存机构名称
    jur_per_name=ormdb.Column(ormdb.String(1000))                  #法人机构名称
    jur_per_id=ormdb.Column(ormdb.String(1000))                    #法人机构代码
    jur_per_type=ormdb.Column(ormdb.String(1000))                  #法人机构类型
    org_intro=ormdb.Column(ormdb.Text)                            #保存机构简介
    use_agr=ormdb.Column(ormdb.String(1000))                       #使用许可
    share_rule=ormdb.Column(ormdb.String(1000))                    #共享方式
    adr=ormdb.Column(ormdb.Text)                                  #通信地址
    post_code=ormdb.Column(ormdb.String(1000))                     #邮政编码
    manager_name=ormdb.Column(ormdb.String(1000))                  #管理员
    tel=ormdb.Column(ormdb.Integer)                              #联系电话
    email=ormdb.Column(ormdb.String(1000))                         #电子信箱


class DonorInfo(ormdb.Model):
    __tablename__="donorinfo"
    don_id=ormdb.Column(ormdb.String(500),primary_key=True)       #捐献者匿名编号
    col_obj=ormdb.Column(ormdb.String(1000))                       #性别
    date_of_bir=ormdb.Column(ormdb.Integer)                          #年龄
    eth_gro=ormdb.Column(ormdb.String(1000))                       #民族
    nativ_pla=ormdb.Column(ormdb.String(1000))                     #籍贯
    bir_pla=ormdb.Column(ormdb.String(1000))                       #出生地
    nation=ormdb.Column(ormdb.String(1000))                        #国籍
    occup=ormdb.Column(ormdb.String(1000))                         #职业
    edu_lev=ormdb.Column(ormdb.String(1000))                       #教育程度
    mari_sta=ormdb.Column(ormdb.String(1000))                      #婚姻状况
    donate_way=ormdb.Column(ormdb.String(1000))                    #捐献途径
    dise_name=ormdb.Column(ormdb.String(1000))                     #疾病类目名称
    dise_id=ormdb.Column(ormdb.String(1000))                       #疾病类目代码
    dig_desc=ormdb.Column(ormdb.Text)                             #主要诊断
    dise_his=ormdb.Column(ormdb.Text)                             #现病史
    exa_rec=ormdb.Column(ormdb.Text)                              #检验记录
    inter_rec=ormdb.Column(ormdb.String(1000))                     #随访记录
    media_rec=ormdb.Column(ormdb.String(1000))                     #影像资料
    medi_rep=ormdb.Column(ormdb.String(1000))                      #病历报告
    fam_his=ormdb.Column(ormdb.String(1000))                       #家系信息
    org_name=ormdb.Column(ormdb.String(300))                      #保存机构名称


class ProjectInfo(ormdb.Model):
    __tablename__="projectinfo"
    prj_name=ormdb.Column(ormdb.String(1000))                         #课题名称
    prj_id=ormdb.Column(ormdb.String(500),primary_key=True)          #课题编号
    prj_level=ormdb.Column(ormdb.String(1000))                        #课题级别
    spon_org=ormdb.Column(ormdb.String(1000))                         #资助机构
    in_level=ormdb.Column(ormdb.String(1000))                         #纳入标准
    keyword=ormdb.Column(ormdb.String(1000))                          #课题关键词
    aim=ormdb.Column(ormdb.String(1000))                              #收集目的
    mtd=ormdb.Column(ormdb.String(1000))                              #收集方法
    total_amt=ormdb.Column(ormdb.Integer)                             #收集数量
    be_end_time=ormdb.Column(ormdb.String(1000))                      #起止时间
    org_name=ormdb.Column(ormdb.String(300))                          #保存机构名称




class Cate_code(ormdb.Model):
    __tablename__="catecode"
    cate_name=ormdb.Column(ormdb.String(100),primary_key=True)
    cate_level = ormdb.Column(ormdb.Integer)
    cate_mark=ormdb.Column(ormdb.String(100))


class User_info(ormdb.Model,UserMixin):
    __tablename__="userinfo"
    user_account=ormdb.Column(ormdb.String(300),primary_key=True)
    user_psd=ormdb.Column(ormdb.String(300))
    user_lv=ormdb.Column(ormdb.String(300))

    @property
    def id(self):
        return self.user_account

