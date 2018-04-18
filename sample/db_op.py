from exts import db
from models import SampleInfo,OrgInfo,DonorInfo,ProjectInfo,Cate_code

# def sp_data(dt):
#     sampleinfo_data=[]
#     orginfo_data=[]
#     projectinfo_data=[]
#     donorinfo_data=[]
#     for i in dt:
#         tmp=i[0:22]
#         tmp.append(i[33])
#         tmp.append(i[54])
#         sampleinfo_data.append(tmp)
#
#         orginfo_data.append(i[21:33])
#
#         tmp=i[33:53]
#         tmp.append(i[21])
#         donorinfo_data.append(tmp)
#
#         tmp=i[53:]
#         tmp.append(i[21])
#         projectinfo_data.append(tmp)
#
#     return [sampleinfo_data,orginfo_data,donorinfo_data,projectinfo_data]
#
#
# def org_dup_rm(dt):
#
#     raw_org=dt
#     org_ls=OrgInfo.query.filter().all()
#
#     for i in raw_org:
#         for j in org_ls:
#             if i[0]==j.org_name:
#                 i[0]=-1
#                 break
#
#     org_rst=[]
#     for i in raw_org:
#         if i[0]!=-1:
#             org_rst.append(i)
#
#
#     return org_rst
#
#
# def proj_dup_rm(dt):
#     raw_proj=dt
#     proj_ls=ProjectInfo.query.filter().all()
#
#
#     for i in raw_proj:
#         for j in proj_ls:
#             if (i[1]==j.prj_id)&(i[10]==j.org_name):
#                 i[0]=-1
#                 break
#
#     proj_rst=[]
#     for i in raw_proj:
#         if i[0]!=-1:
#             proj_rst.append(i)
#
#     return proj_rst
#
#
# def donor_dup_rm(dt):
#     raw_donor=dt
#     donor_ls=DonorInfo.query.filter().all()
#
#     for i in raw_donor:
#         for j in donor_ls:
#             if (i[0]==j.don_id)&(i[20]==j.org_name):
#                 i[0]=-1
#                 break
#
#     donor_rst=[]
#
#     for i in raw_donor:
#         if i[0]!=-1:
#             donor_rst.append(i)
#
#     return donor_rst









def info_insert(dt):
    smp_list=[]
    org_list=[]
    dn_list=[]
    prj_list=[]

    # for i in sampleinfo_data:
    #     smp_list.append(smp_info_insert(i))
    # for i in orginfo_data:
    #     org_list.append(org_info_insert(i))
    # for i in donorinfo_data:
    #     dn_list.append(dn_info_insert(i))
    # for i in projectinfo_data:
    #     prj_list.append(prj_info_insert(i))


    for item in dt:
        smp_list.append(smp_info_insert(item))
        org_list.append(org_info_insert(item))
        dn_list.append(dn_info_insert(item))
        prj_list.append(prj_info_insert(item))

    for i in smp_list:
        db.session.add(i)
    for i in org_list:
        db.session.add(i)
    for i in dn_list:
        db.session.add(i)
    for i in prj_list:
        db.session.add(i)

    try:
        db.session.commit()
    except:
        print("err")



def smp_info_insert(dt):

        smpinfo=SampleInfo(sam_uni_id=dt[0],inv_id=dt[1],sam_cate_name=dt[2],ent_date=dt[3],stor_meth=dt[4],parent_id=dt[5],batch_count=dt[6],sam_qty=dt[7],unit_amou=dt[8],consent=dt[9],
                           sam_title=dt[10],sam_desc=dt[11],keyword=dt[12],sam_uses=dt[13],acqui_pos=dt[14],s_pre_c=dt[15],acqui_mot=dt[16],acqui_time=dt[17],acqui_plan=dt[18],
                           acqui_org=dt[19],acqui_assis=dt[20],org_name=dt[21],don_id=dt[33],proj_id=dt[54])

        return smpinfo
        # return db.session.execute(
        #     'insert ignore into sampleinfo values(:dt0,:dt1,:dt2,:dt3,:dt4,:dt5,:dt6,:dt7,:dt8,:dt9,:dt10,:dt11,:dt12,:dt13,:dt14,:dt15,:dt16,:dt17,:dt18,:dt19,:dt20,:dt21,:dt22,:dt23)',
        #     params={"dt0": dt[0], "dt1": dt[1], "dt2": dt[2], "dt3": dt[3], "dt4": dt[4], "dt5": dt[5], "dt6": dt[6],
        #             "dt7": dt[7], "dt8": dt[8], "dt9": dt[9], "dt10": dt[10], "dt11": dt[11], "dt12": dt[12],
        #             "dt13": dt[13], "dt14": dt[14], "dt15": dt[15], "dt16": dt[16], "dt17": dt[17], "dt18": dt[18],
        #             "dt19": dt[19], "dt20": dt[20], "dt21": dt[21], "dt22": dt[22], "dt23": dt[23]})
        # db.session.commit()
        # return smpinfo



def org_info_insert(dt):
    # exst = OrgInfo.query.filter(OrgInfo.org_name == dt[21]).all()
    # ln=len(exst)
    # if ln>0:
    #     pass
    # else:
    # try:
        orginfo=OrgInfo(org_name=dt[21],jur_per_name=dt[22],jur_per_id=dt[23],jur_per_type=dt[24],org_intro=dt[25],use_agr=dt[26],
                        share_rule=dt[27],adr=dt[28],post_code=dt[29],manager_name=dt[30],tel=dt[31],email=dt[32])
        return orginfo
        # return db.session.execute('insert  into orginfo values(:dt21,:dt22,:dt23,:dt24,:dt25,:dt26,:dt27,:dt28,:dt29,:dt30,:dt31,:dt32)',
        #                           params={"dt21":dt[21],"dt22":dt[22],"dt23":dt[23],"dt24":dt[24],"dt25":dt[25],"dt26":dt[26],"dt27":dt[27]
        #                                   ,"dt28":dt[28],"dt29":dt[29],"dt30":dt[30],"dt31":dt[31],"dt32":dt[32]
        #                                   })
        # db.session.add(orginfo)
        # db.session.commit()
    # except:
    #     print("冲突")


def dn_info_insert(dt):

    # exst = DonorInfo.query.filter(DonorInfo.don_id==dt[33],DonorInfo.org_name==dt[21]).all()
    #
    # ln=len(exst)
    # if ln>0:
    #     pass
    # else:
    # try:
        dninfo=DonorInfo(don_id=dt[33],col_obj=dt[34],date_of_bir=dt[35],eth_gro=dt[36],nativ_pla=dt[37],bir_pla=dt[38],nation=dt[39],
                         occup=dt[40],edu_lev=dt[41],mari_sta=dt[42],donate_way=dt[43],dise_name=dt[44],dise_id=dt[45],dig_desc=dt[46],
                         dise_his=dt[47],exa_rec=dt[48],inter_rec=dt[49],media_rec=dt[50],medi_rep=dt[51],fam_his=dt[52],org_name=dt[21])
        return dninfo
        # return db.session.execute('insert into donorinfo values(:dt33,:dt34,:dt35,:dt36,:dt37,:dt38,:dt39,:dt40,:dt41,:dt42,:dt43,:dt44,:dt45,'
        #                           ':dt46,:dt47,:dt48,:dt49,:dt50,:dt51,:dt52,:dt21)',
        #                           params={"dt33":dt[33],"dt34":dt[34],"dt35":dt[35],"dt36":dt[36], "dt37":dt[37],"dt38":dt[38],"dt39":dt[39],
        #                                   "dt40":dt[40],"dt41":dt[41],"dt42":dt[42],"dt43":dt[43],"dt44":dt[44],"dt45":dt[45],"dt46":dt[46],
        #                                 "dt47":dt[47],"dt48":dt[48],"dt49":dt[49],"dt50":dt[50],"dt51":dt[51],"dt52":dt[52],"dt21":dt[21]})
        # db.session.add(dninfo)
        # db.session.commit()
    # except:
    #     print("冲突")



def prj_info_insert(dt):
    # exst=ProjectInfo.query.filter(ProjectInfo.prj_id==dt[54],ProjectInfo.org_name==dt[21]).all()
    # ln=len(exst)
    # if ln>0:
    #     pass
    # else:
    # try:
        prjinfo=ProjectInfo(prj_name=dt[53],prj_id=dt[54],prj_level=dt[55],spon_org=dt[56],in_level=dt[57],keyword=dt[58],aim=dt[59],
                            mtd=dt[60],total_amt=dt[61],be_end_time=dt[62],org_name=dt[21])
        return prjinfo

        # return db.session.execute('insert  into projectinfo values(:dt53,:dt54,:dt55,:dt56,:dt57,:dt58,:dt59,:dt60,:dt61,:dt62,:dt21)',
        #                           params={"dt53":dt[53],"dt54":dt[54],"dt55":dt[55],"dt56":dt[56],"dt57":dt[57],"dt58":dt[58],"dt59":dt[59],"dt60":dt[60],
        #                                   "dt61":dt[61],"dt62":dt[62],"dt21":dt[21]})
    # except:
    #     print("冲突")



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
    db.session.commit()


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
    db.session.commit()


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
    db.session.commit()

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
    db.session.commit()




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
#     db.session.delete(smp)
#     db.session.commit()




def delete_dn_info(dn_id,org_name):
    dn=DonorInfo.query.filter(DonorInfo.don_id==dn_id,DonorInfo.org_name==org_name).first()
    db.session.delete(dn)
    db.session.commit()


def delete_org_info(org_name):
    org=OrgInfo.query.filter(OrgInfo.org_name==org_name).first()
    db.session.delete(org)
    db.session.commit()


def delete_prj_info(prj_id,org_name):
    prj=ProjectInfo.query.filter(ProjectInfo.prj_id==prj_id,ProjectInfo.org_name==org_name).first()
    db.session.delete(prj)
    db.session.commit()




def delete_sampleinfo(sam_uni_id):
    smp=SampleInfo.query.filter(SampleInfo.sam_uni_id==sam_uni_id).first()
    db.session.delete(smp)
    db.session.commit()



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








