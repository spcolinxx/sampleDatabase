from exts import ormdb
from models import SampleInfo,OrgInfo,DonorInfo,ProjectInfo,Cate_code
import threading

def sp_data(dt):
    # sampleinfo_data=[]
    # orginfo_data=[]
    # projectinfo_data=[]
    # donorinfo_data=[]

    # for i in dt:
    #     tmp=i[0:22]
    #     tmp.append(i[33])
    #     tmp.append(i[54])
    #     sampleinfo_data.append(tmp)
    #
    #     orginfo_data.append(i[21:33])
    #
    #     tmp=i[33:53]
    #     tmp.append(i[21])
    #     donorinfo_data.append(tmp)
    #
    #     tmp=i[53:]
    #     tmp.append(i[21])
    #     projectinfo_data.append(tmp)
    #
    # return [sampleinfo_data,orginfo_data,donorinfo_data,projectinfo_data]


    return [get_sampleinfo_data(dt),get_orginfo_data(dt),get_donorinfo_data(dt),get_projectinfo_data(dt)]



def get_sampleinfo_data(dt):
    sampleinfo_data=[]
    for i in dt:
        tmp = i[0:22]
        tmp.append(i[33])
        tmp.append(i[54])
        sampleinfo_data.append(tmp)

    return sampleinfo_data

def get_orginfo_data(dt):
    orginfo_data=[]
    for i in dt:
        orginfo_data.append(i[21:33])
    return orginfo_data

def get_donorinfo_data(dt):
    donorinfo_data=[]
    for i in dt:
        tmp = i[33:53]
        tmp.append(i[21])
        donorinfo_data.append(tmp)
    return donorinfo_data


def get_projectinfo_data(dt):
    projectinfo_data=[]
    for i in dt:
        tmp = i[53:]
        tmp.append(i[21])
        projectinfo_data.append(tmp)

    return projectinfo_data







def sampleinfo_insert(dt,sqldb):
    try:
        cursor=sqldb.cursor()
        sql="insert ignore  into sampleinfo values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.executemany(sql,dt)
        sqldb.commit()
        cursor.close()
    except:
        pass

def orginfo_insert(dt,sqldb):
    try:
        cursor=sqldb.cursor()
        sql="insert ignore  into orginfo values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.executemany(sql,dt)
        sqldb.commit()
        cursor.close()
    except:
        pass

def donorinfo_insert(dt,sqldb):
    try:
        cursor=sqldb.cursor()
        sql="insert ignore  into donorinfo values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.executemany(sql,dt)
        sqldb.commit()
        cursor.close()
    except:
        pass

def projectinfo_insert(dt,sqldb):
    try:
        cursor=sqldb.cursor()
        sql="insert ignore  into projectinfo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.executemany(sql,dt)
        sqldb.commit()
        cursor.close()
    except:
        pass




def search_org():
    orgls=[]
    org=OrgInfo.query.filter().all()
    for i in org:
        orgls.append(i.org_name)

    return orgls


def search_info(inv_id,org_name):

    rst=[]
    smpinfo=SampleInfo.query.filter(SampleInfo.inv_id==inv_id,SampleInfo.org_name==org_name).first()

    if smpinfo==None:
        return None
    else:

        donor_id=smpinfo.don_id
        proj_id=smpinfo.proj_id



        orginfo=OrgInfo.query.filter(OrgInfo.org_name==org_name).first()
        dninfo=DonorInfo.query.filter(DonorInfo.don_id==donor_id,DonorInfo.org_name==org_name).first()
        prjinfo=ProjectInfo.query.filter(ProjectInfo.prj_id==proj_id,ProjectInfo.org_name==org_name).first()


        rst.append(smpinfo.sam_uni_id)
        rst.append(smpinfo.inv_id)
        rst.append(smpinfo.sam_cate_name)
        rst.append(smpinfo.ent_date)
        rst.append(smpinfo.stor_meth)
        rst.append(smpinfo.parent_id)
        rst.append(smpinfo.batch_count)
        rst.append(smpinfo.sam_qty)
        rst.append(smpinfo.unit_amou)
        rst.append(smpinfo.consent)
        rst.append(smpinfo.sam_title)
        rst.append(smpinfo.sam_desc)
        rst.append(smpinfo.keyword)
        rst.append(smpinfo.sam_uses)
        rst.append(smpinfo.acqui_pos)
        rst.append(smpinfo.s_pre_c)
        rst.append(smpinfo.acqui_mot)
        rst.append(smpinfo.acqui_time)
        rst.append(smpinfo.acqui_plan)
        rst.append(smpinfo.acqui_org)
        rst.append(smpinfo.acqui_assis)
        rst.append(orginfo.org_name)
        rst.append(orginfo.jur_per_name)
        rst.append(orginfo.jur_per_id)
        rst.append(orginfo.jur_per_type)
        rst.append(orginfo.org_intro)
        rst.append(orginfo.use_agr)
        rst.append(orginfo.share_rule)
        rst.append(orginfo.adr)
        rst.append(orginfo.post_code)
        rst.append(orginfo.manager_name)
        rst.append(orginfo.tel)
        rst.append(orginfo.email)
        rst.append(dninfo.don_id)
        rst.append(dninfo.col_obj)
        rst.append(dninfo.date_of_bir)
        rst.append(dninfo.eth_gro)
        rst.append(dninfo.nativ_pla)
        rst.append(dninfo.bir_pla)
        rst.append(dninfo.nation)
        rst.append(dninfo.occup)
        rst.append(dninfo.edu_lev)
        rst.append(dninfo.mari_sta)
        rst.append(dninfo.donate_way)
        rst.append(dninfo.dise_name)
        rst.append(dninfo.dise_id)
        rst.append(dninfo.dig_desc)
        rst.append(dninfo.dise_his)
        rst.append(dninfo.exa_rec)
        rst.append(dninfo.inter_rec)
        rst.append(dninfo.media_rec)
        rst.append(dninfo.medi_rep)
        rst.append(dninfo.fam_his)
        rst.append(prjinfo.prj_name)
        rst.append(prjinfo.prj_id)
        rst.append(prjinfo.prj_level)
        rst.append(prjinfo.spon_org)
        rst.append(prjinfo.in_level)
        rst.append(prjinfo.keyword)
        rst.append(prjinfo.aim)
        rst.append(prjinfo.mtd)
        rst.append(prjinfo.total_amt)
        rst.append(prjinfo.be_end_time)

        return rst


def uni_search(sam_uni_id):
    smp=SampleInfo.query.filter(SampleInfo.sam_uni_id==sam_uni_id).first()
    return smp





def up_sam_check(sam_uni_id,inv_id,org_name):
    smp=SampleInfo.query.filter(SampleInfo.sam_uni_id!=sam_uni_id,SampleInfo.inv_id==inv_id,SampleInfo.org_name==org_name).all()

    if len(smp)>0:
        return True
    else:
        return False


def sampleinfo_update(sam_uni_id,dt):

    smp=SampleInfo.query.filter(SampleInfo.sam_uni_id==sam_uni_id).update({

        'inv_id':dt[1],
        'sam_cate_name':dt[2],
        'ent_date': dt[3],
        'stor_meth': dt[4],
        'parent_id' :dt[5],
        'batch_count': dt[6],
        'sam_qty':dt[7],
        'unit_amou': dt[8],
        'consent': dt[9],
        'sam_title': dt[10],
        'sam_desc': dt[11],
        'keyword': dt[12],
        'sam_uses': dt[13],
        'acqui_pos': dt[14],
        's_pre_c':dt[15],
        'acqui_mot': dt[16],
        'acqui_time': dt[17],
        'acqui_plan': dt[18],
        'acqui_org': dt[19],
        'acqui_assis': dt[20],
        'org_name': dt[21],
        'don_id': dt[33],
        'proj_id':dt[54],

    })
    ormdb.session.commit()


def orginfo_update(dt):
    org=OrgInfo.query.filter(OrgInfo.org_name==dt[21]).update({
        'jur_per_name':dt[22],
        'jur_per_id':dt[23],
        'jur_per_type':dt[24],
        'org_intro':dt[25],
        'use_agr':dt[26],
        'share_rule':dt[27],
        'adr':dt[28],
        'post_code':dt[29],
        'manager_name':dt[30],
        'tel':dt[31],
        'email':dt[32]

    })
    ormdb.session.commit()


def donorinfo_update(dt):
    donor=DonorInfo.query.filter(DonorInfo.don_id==dt[33],DonorInfo.org_name==dt[21]).update({
        'col_obj':dt[34],
        'date_of_bir': dt[35],
        'eth_gro': dt[36],
        'nativ_pla': dt[37],
        'bir_pla': dt[38],
        'nation': dt[39],
        'occup': dt[40],
        'edu_lev': dt[41],
        'mari_sta': dt[42],
        'donate_way': dt[43],
        'dise_name':dt[44],
        'dise_id': dt[45],
        'dig_desc': dt[46],
        'dise_his':dt[47],
        'exa_rec': dt[48],
        'inter_rec': dt[49],
        'media_rec' :dt[50],
        'medi_rep' :dt[51],
        'fam_his' :dt[52],
        'org_name':dt[21]

    })
    ormdb.session.commit()

def projinfo_update(dt):
    proj=ProjectInfo.query.filter(ProjectInfo.prj_id==dt[54],ProjectInfo.org_name==dt[21]).update({
        'prj_name':dt[53],
        'prj_level':dt[55],
        'spon_org':dt[56],
        'in_level':dt[57],
        'keyword':dt[58],
        'aim':dt[59],
        'mtd':dt[60],
        'total_amt':dt[61],
        'be_end_time':dt[62],
        'org_name':dt[21]

    })
    ormdb.session.commit()




def org_search(org_name):
    org=OrgInfo.query.filter(OrgInfo.org_name==org_name).first()

    return org

def donor_search(don_id,org_name):
    don=DonorInfo.query.filter(DonorInfo.don_id==don_id,DonorInfo.org_name==org_name).first()
    return don

def proj_search(proj_id,org_name):
    proj=ProjectInfo.query.filter(ProjectInfo.prj_id==proj_id,ProjectInfo.org_name==org_name).first()

    return proj



def donor_exist_check(donor_id,org_name):
    dn=SampleInfo.query.filter(SampleInfo.don_id==donor_id,SampleInfo.org_name==org_name).first()

    return dn




def proj_exist_check(proj_id,org_name):
    proj=SampleInfo.query.filter(SampleInfo.proj_id==proj_id,SampleInfo.org_name==org_name).first()
    return proj


def org_exist_check(org_name):
    org=SampleInfo.query.filter(SampleInfo.org_name==org_name).first()

    return org








# def delete_sampleinfo(smp_id):
#     smp=SampleInfo.query.filter(SampleInfo.inv_id==smp_id).first()
#     ormdb.session.delete(smp)
#     ormdb.session.commit()




def delete_dn_info(dn_id,org_name):
    dn=DonorInfo.query.filter(DonorInfo.don_id==dn_id,DonorInfo.org_name==org_name).first()
    ormdb.session.delete(dn)
    ormdb.session.commit()


def delete_org_info(org_name):
    org=OrgInfo.query.filter(OrgInfo.org_name==org_name).first()
    ormdb.session.delete(org)
    ormdb.session.commit()


def delete_prj_info(prj_id,org_name):
    prj=ProjectInfo.query.filter(ProjectInfo.prj_id==prj_id,ProjectInfo.org_name==org_name).first()
    ormdb.session.delete(prj)
    ormdb.session.commit()




def delete_sampleinfo(sam_uni_id):
    smp=SampleInfo.query.filter(SampleInfo.sam_uni_id==sam_uni_id).first()
    ormdb.session.delete(smp)
    ormdb.session.commit()



def get_cate():
    l1_tmp = Cate_code.query.filter(Cate_code.cate_level=='1').all()
    l1=[]
    for i in l1_tmp:
        l1.append([i.cate_mark,i.cate_name])



    l2_tmp = Cate_code.query.filter(Cate_code.cate_level == '2').all()
    l2 = []
    for i in l2_tmp:
        l2.append([i.cate_mark, i.cate_name])

    l3_tmp = Cate_code.query.filter(Cate_code.cate_level == '3').all()
    l3 = []
    for i in l3_tmp:
        l3.append([i.cate_mark, i.cate_name])

    l4_tmp = Cate_code.query.filter(Cate_code.cate_level == '4').all()
    l4 = []
    for i in l4_tmp:
        l4.append([i.cate_mark, i.cate_name])

    return [l1,l2,l3,l4]








