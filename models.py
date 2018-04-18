from exts import db

from flask.ext.login import UserMixin

class SampleInfo(db.Model):
    __tablename__="sampleinfo"                      #表名
    sam_uni_id=db.Column(db.String(300),nullable=False,primary_key=True)            #唯一表示码

    inv_id=db.Column(db.String(500))               #样本编码
    sam_cate_name=db.Column(db.String(500))         #样本类别
    ent_date=db.Column(db.Date)                      #入库日期
    stor_meth = db.Column(db.String(500))           # 保存温度
    parent_id=db.Column(db.String(500))             #母本编码
    batch_count=db.Column(db.Integer)                #分管数
    sam_qty=db.Column(db.Integer)                   #样本量
    unit_amou=db.Column(db.String(500))             #量单位
    consent=db.Column(db.Boolean)                   #知情同意
    sam_title=db.Column(db.String(500))             #样本别称
    sam_desc=db.Column(db.Text)                     #样本描述
    keyword=db.Column(db.String(500))               #关键词
    sam_uses=db.Column(db.String(500))              #样本用途
    acqui_pos=db.Column(db.String(500))             #采集部位
    s_pre_c=db.Column(db.String(500))               #分析前变量
    acqui_mot=db.Column(db.String(500))             #采集动因
    acqui_time=db.Column(db.Date)                   #采集时间
    acqui_plan=db.Column(db.Text)                   #采集计划
    acqui_org=db.Column(db.String(500))             #采集机构
    acqui_assis=db.Column(db.String(500))           #其他采集者
    org_name = db.Column(db.String(500))           # 保存机构名称
    don_id = db.Column(db.String(500))             # 捐献者匿名编号
    proj_id=db.Column(db.String(500 ))               #课题编号


class OrgInfo(db.Model):
    __tablename__="orginfo"
    org_name=db.Column(db.String(1000),primary_key=True)     #保存机构名称
    jur_per_name=db.Column(db.String(1000))                  #法人机构名称
    jur_per_id=db.Column(db.String(1000))                    #法人机构代码
    jur_per_type=db.Column(db.String(1000))                  #法人机构类型
    org_intro=db.Column(db.Text)                            #保存机构简介
    use_agr=db.Column(db.String(1000))                       #使用许可
    share_rule=db.Column(db.String(1000))                    #共享方式
    adr=db.Column(db.Text)                                  #通信地址
    post_code=db.Column(db.String(1000))                     #邮政编码
    manager_name=db.Column(db.String(1000))                  #管理员
    tel=db.Column(db.Integer)                              #联系电话
    email=db.Column(db.String(1000))                         #电子信箱


class DonorInfo(db.Model):
    __tablename__="donorinfo"
    don_id=db.Column(db.String(1000),primary_key=True)       #捐献者匿名编号
    col_obj=db.Column(db.String(1000))                       #性别
    date_of_bir=db.Column(db.Integer)                          #年龄
    eth_gro=db.Column(db.String(1000))                       #民族
    nativ_pla=db.Column(db.String(1000))                     #籍贯
    bir_pla=db.Column(db.String(1000))                       #出生地
    nation=db.Column(db.String(1000))                        #国籍
    occup=db.Column(db.String(1000))                         #职业
    edu_lev=db.Column(db.String(1000))                       #教育程度
    mari_sta=db.Column(db.String(1000))                      #婚姻状况
    donate_way=db.Column(db.String(1000))                    #捐献途径
    dise_name=db.Column(db.String(1000))                     #疾病类目名称
    dise_id=db.Column(db.String(1000))                       #疾病类目代码
    dig_desc=db.Column(db.Text)                             #主要诊断
    dise_his=db.Column(db.Text)                             #现病史
    exa_rec=db.Column(db.Text)                              #检验记录
    inter_rec=db.Column(db.String(1000))                     #随访记录
    media_rec=db.Column(db.String(1000))                     #影像资料
    medi_rep=db.Column(db.String(1000))                      #病历报告
    fam_his=db.Column(db.String(1000))                       #家系信息
    org_name=db.Column(db.String(300),primary_key=True)                      #保存机构名称


class ProjectInfo(db.Model):
    __tablename__="projectinfo"
    prj_name=db.Column(db.String(1000))                         #课题名称
    prj_id=db.Column(db.String(1000),primary_key=True)          #课题编号
    prj_level=db.Column(db.String(1000))                        #课题级别
    spon_org=db.Column(db.String(1000))                         #资助机构
    in_level=db.Column(db.String(1000))                         #纳入标准
    keyword=db.Column(db.String(1000))                          #课题关键词
    aim=db.Column(db.String(1000))                              #收集目的
    mtd=db.Column(db.String(1000))                              #收集方法
    total_amt=db.Column(db.Integer)                             #收集数量
    be_end_time=db.Column(db.String(1000))                      #起止时间
    org_name=db.Column(db.String(300),primary_key=True)                          #保存机构名称




class Cate_code(db.Model):
    __tablename__="catecode"
    cate_name=db.Column(db.String(100),primary_key=True)
    cate_level = db.Column(db.Integer)
    cate_mark=db.Column(db.String(100))


class User_info(db.Model,UserMixin):
    __tablename__="userinfo"
    user_account=db.Column(db.String(300),primary_key=True)
    user_psd=db.Column(db.String(300))
    user_lv=db.Column(db.String(300))

    @property
    def id(self):
        return self.user_account

