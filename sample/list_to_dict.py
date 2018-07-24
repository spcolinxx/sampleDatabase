def trans_to_dict(dt):
    item_ls=["sam_uni_id","inv_id","sam_cate_name","ent_date","stor_meth","parent_id","batch_count","sam_qty","uni_amou"
             ,"consent","sam_title","sam_desc","keyword","sam_uses","acqui_pos","s_pre_c",
             "acqui_mot","acqui_time","acqui_plan","acqui_org","acqui_assis","org_name"
        ,"jur_per_name","jur_per_id","jur_per_type","org_intro","use_agr","share_rule",
             "adr","post_code","manager_name","tel","email","don_id","gender","date_of_bir"
        ,"eth_gro","nativ_pla","bir_pla","nation","occup","edu_lev","mari_sta","donate_way"
             ,"dise_name","dise_id","dig_desc","dise_his","exa_rec","inter_rec","media_rec",
             "medi_rep","fam_his","prj_name","prj_id","prj_level","spon_org","in_level"
        ,"prj_keyword","aim","mtd","total_amt","be_time","end_time","upload_time"]

    dt_ls=[]
    for i in dt:
        tmp = {}
        for j in range(len(i)):
            tmp[item_ls[j]]=i[j]

        dt_ls.append(tmp)


    return dt_ls
