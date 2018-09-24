from flask import render_template,redirect,url_for,session,flash
from . import sample
import datetime
from flask import request
from . import read_file
import xlrd
from flask.ext.login import LoginManager,login_user, logout_user,login_required
from . import schema_validate
import exts
import datetime,time
from . import list_to_dict
from . import mongo
import re,threading
# from sampleDatabase import app
from . import path_op
import os
from flask import make_response,send_file
from urllib.parse import quote


def batch_add_thread(file,filename,file_path,user_id):

    if (file_path==False)&(file!=False):
        file_trans = xlrd.open_workbook(filename=None, file_contents=file.read())
    else:
        file_trans=xlrd.open_workbook(file_path)

    upload_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    read_rst = read_file.read_file(file_trans,upload_time)

    if read_rst[0] == False:
        err_info = []

        for i in read_rst[1]:
            err_info.append(i)

        cnn = exts.create_mongo_cnn()
        mongo.insert_op_rc(
            {'account': user_id, 'filename': filename, 'uploadtime': upload_time, 'rst': '入库不成功',
             'info': err_info}, cnn)
        cnn.close()

        # flash("正在检查样本信息格式及完成入库，结果详情请稍后在操作记录模块中查看！")
    else:

        excel_data = read_rst[1]
        err_log = schema_validate.schema_check(excel_data)

        if len(err_log) > 0:
            err_info = []
            for i in err_log:
                for j in i[1]:
                    err_info.append("第" + str(i[0] + 1) + "条记录错误信息：" + str(j))



            cnn = exts.create_mongo_cnn()
            mongo.insert_op_rc(
                {'account': user_id, 'filename': filename, 'uploadtime': upload_time, 'rst': '入库不成功',
                 'info': err_info}, cnn)
            cnn.close()

        else:

            to_upload_data = []

            for i in excel_data:
                i.append(upload_time)
                to_upload_data.append(i)

            std_data = list_to_dict.trans_to_dict(to_upload_data)
            sample_count = len(std_data)

            cnn = exts.create_mongo_cnn()
            mongo.add_info(std_data, cnn)
            mongo.insert_op_rc(
                {'account': user_id, 'filename': filename, 'uploadtime': upload_time, 'rst': '入库成功',
                 'info': ['该次入库操作成功，样本已添加到样本库中。'], 'count': sample_count}, cnn)

            cnn.close()







@sample.route('/sample/batchAdd',methods=['GET','POST'])
@login_required
def render_batchAdd():
    if request.method=='GET':
        return render_template('batchAdd.html')
    else:
        file=request.files['file_input']
        filename = file.filename.split(".")

        target_path=path_op.get_save_path()

        if target_path==False:
            if (filename[-1] != "xls") & (filename[-1] != "xlsx")& (filename[-1] != "xlsm"):
                flash("只能上传excel文件，请重新上传！")
                return redirect(url_for('sample.render_batchAdd'))
            else:

                add_thread = threading.Thread(target=batch_add_thread, args=(file,file.filename,False,session['user_id']))
                add_thread.start()

                flash("正在校验样本信息及完成入库，结果详情请稍后在样本增加记录模块中查看！")
                flash("文件备份路径错误，本次上传样本未备份，请通知管理员查看！")

                return redirect(url_for('sample.render_batchAdd'))

            return redirect(url_for('sample.render_batchAdd'))
        else:
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            format_time = now_time.replace('-', '')
            format_time = format_time.replace(' ', '')
            format_time = format_time.replace(':', '')

            target_file_name = filename[0] + format_time + '.' + filename[1]
            user_path = target_path + '/' + session['user_id']

            if os.path.exists(user_path):
                file_path = user_path + '/' + target_file_name
                file.save(file_path)

            else:
                os.makedirs(user_path)
                file_path = user_path + '/' + target_file_name
                file.save(file_path)

            if (filename[-1] != "xls") & (filename[-1] != "xlsx")& (filename[-1] != "xlsm"):
                flash("只能上传excel文件，请重新上传！")
                return redirect(url_for('sample.render_batchAdd'))
            else:

                add_thread = threading.Thread(target=batch_add_thread, args=(False,file.filename,file_path,session['user_id']))
                add_thread.start()

                flash("正在校验样本信息及完成入库，结果详情请稍后在样本增加记录模块中查看！")
                flash("样本文件已备份！")
                return redirect(url_for('sample.render_batchAdd'))



@sample.route('/sample/ele_search',methods=['POST','GET'])
@login_required
def render_ele_search():
    search_item = ["库存编码", "样本类别", "保存方式","每份样本数量","采集时间","保存机构名称", "法人机构代码", "法人机构类型",
                   "保存机构简介", "通讯地址","邮政编码", "联系人姓名", "联系电话", "电子邮箱", "捐献人编号", "性别", "年龄",
                   "民族", "籍贯", "出生地", "疾病名称", "正常人群"]
    if request.method=='GET':

        return render_template('ele_search.html',search_item=search_item)

    else:
        dt={}
        receive_data=request.form.to_dict()

        for i in receive_data:
            if receive_data[i]!="":
                dt[i]=receive_data[i]
            if i.endswith('date_of_bir'):
                dt[i]=int(receive_data[i])

        if len(dt)>0:

            and_ls=[]
            or_ls=[]
            nor_ls=[]

            for ky,vl in dt.items():
                if ky.startswith('and'):
                    if ky.endswith('date_of_bir'):
                        and_ls.append({ky[7:]: vl})
                    else:
                        and_ls.append({ky[7:]:re.compile(vl)})
                elif ky.startswith('or'):
                    if ky.endswith('date_of_bir'):
                        or_ls.append({ky[6:]:re.compile(vl)})
                    else:
                        or_ls.append({ky[6:]:re.compile(vl)})
                else:
                    if ky.endswith('date_of_bir'):
                        nor_ls.append({ky[7:]:re.compile(vl)})
                    else:
                        nor_ls.append({ky[7:]:re.compile(vl)})


            cnn = exts.create_mongo_cnn()
            dict_rst = mongo.info_search(and_ls,or_ls,nor_ls, cnn)

            # rst为数组形式，需遍历才能取出数据
            # 每条数据为字典形式，需要转化为数组

            cnn.close()

            search_rst = []
            for i in dict_rst:
                search_rst.append(list(i.values()))

            if len(search_rst)>1000:
                search_rst=search_rst[:1000]

            ln=len(search_rst)


            if ln>0:
                return render_template('search_list.html',search_rst=search_rst)

            else:
                flash("无符合条件的记录！")
                return  redirect(url_for('sample.render_ele_search'))

        else:
            flash("请添加搜索关键词！")

            return redirect(url_for('sample.render_ele_search'))



@sample.route('/sample/<sam_uni_id>',methods=['POST','GET'])
@login_required
def render_sampleinfo(sam_uni_id):
    if request.method=='GET':
        return sam_uni_id
    else:
        pass





@sample.route('/sample/smpUpdate/<inv_id>/<org_name>/<jur_per_id>',methods=['POST','GET'])
@login_required
def render_update(inv_id,org_name,jur_per_id):
    if request.method=='GET':

        dt={'inv_id':inv_id,'org_name':org_name,'jur_per_id':jur_per_id}


        cnn=exts.create_mongo_cnn()
        search_rst=list(mongo.info_search(dt,cnn)[0].values())
        cate_ls=mongo.get_catecode(cnn)


        cnn.close()


        current_year = datetime.datetime.now().year


        l1=cate_ls[0]
        l2=cate_ls[1]
        l3=cate_ls[2]
        l4=cate_ls[3]



        tmp=str(search_rst[4])
        in_date=tmp.split('-')
        in_year_ls=[]
        in_month_ls=[]
        in_day_ls=[]


        for i in range(1970,current_year+1):
            in_year_ls.append(str(i))
        for i in range(1,13):
            in_month_ls.append(str(i).zfill(2))
        for i in range(1,32 ):
            in_day_ls.append(str(i).zfill(2))


        if in_date[0] in in_year_ls:
            in_year_ls.remove(in_date[0])
        if in_date[1] in in_month_ls:
            in_month_ls.remove(in_date[1])
        if in_date[2] in in_day_ls:
            in_day_ls.remove(in_date[2])



        temp=search_rst[5]
        temp_ls=["室温","2°C～10°C","-35°C～-18°C","-85°C～-60°C","-196°C～-150°C","液氮","其它方式"]
        if temp in temp_ls:
            temp_ls.remove(temp)

        agr=[]
        nagr=[]
        agr.append(search_rst[10])
        if agr[0]=='1':
            agr.append("同意")
            nagr.append("False")
            nagr.append("不同意")
        else:
            agr.append("不同意")
            nagr.append("True")
            nagr.append("同意")


        sx=[]
        sx.append(search_rst[35])
        if sx[0]=="男":
            sx.append("女")
        else:
            sx.append("男")

        age=search_rst[36]

        age_ls=[]

        for i in range(1,151):
            age_ls.append(i)

        if age in age_ls:
            age_ls.remove(age)


        ac_tmp=str(search_rst[18])
        ac_date=ac_tmp.split('-')

        ac_year=[]
        ac_month=[]
        ac_day=[]

        for i in range(1970,current_year+1):
            ac_year.append(str(i))
        for i in range(1,13):
            ac_month.append(str(i).zfill(2))
        for i in range(1,32):
            ac_day.append(str(i).zfill(2))


        if ac_date[0] in ac_year:
            ac_year.remove(ac_date[0])
        if ac_date[1] in ac_month:
            ac_month.remove(ac_date[1])
        if ac_date[2] in ac_day:
            ac_day.remove(ac_date[2])



        be_tmp = str(search_rst[63])
        be_date = be_tmp.split('-')
        be_year_ls = []
        be_month_ls = []
        be_day_ls = []

        for i in range(1970, current_year + 1):
            be_year_ls.append(str(i))
        for i in range(1, 13):
            be_month_ls.append(str(i).zfill(2))
        for i in range(1, 32):
            be_day_ls.append(str(i).zfill(2))

        if be_date[0] in be_year_ls:
            be_year_ls.remove(be_date[0])
        if be_date[1] in be_month_ls:
            be_month_ls.remove(be_date[1])
        if be_date[2] in be_day_ls:
            be_day_ls.remove(be_date[2])

        end_tmp = str(search_rst[64])
        end_date = end_tmp.split('-')
        end_year_ls = []
        end_month_ls = []
        end_day_ls = []

        for i in range(1970, current_year + 1):
            end_year_ls.append(str(i))
        for i in range(1, 13):
            end_month_ls.append(str(i).zfill(2))
        for i in range(1, 32):
            end_day_ls.append(str(i).zfill(2))

        if end_date[0] in end_year_ls:
            end_year_ls.remove(end_date[0])
        if end_date[1] in end_month_ls:
            end_month_ls.remove(end_date[1])
        if end_date[2] in end_day_ls:
            end_day_ls.remove(end_date[2])


        return render_template('smpUpdate.html',search_rst=search_rst,l1=l1,l2=l2,l3=l3,l4=l4,in_date=in_date,in_year_ls=in_year_ls,in_month_ls=in_month_ls,
                               in_day_ls=in_day_ls,temp=temp,temp_ls=temp_ls,agr=agr,nagr=nagr,sx=sx,age=age,age_ls=age_ls,ac_date=ac_date,
                               ac_year=ac_year,ac_month=ac_month,ac_day=ac_day,be_date=be_date,be_year_ls=be_year_ls,be_month_ls=be_month_ls,
                               be_day_ls=be_day_ls,end_date=end_date,end_year_ls=end_year_ls,end_month_ls=end_month_ls,end_day_ls=end_day_ls)


    else:

        rc=request.form.to_dict()
        inv_id=rc['inv_id']
        org_name=rc['org_name']
        jur_per_id=rc['jur_per_id']

        query_dt={'inv_id':inv_id,'org_name':org_name,'jur_per_id':jur_per_id}

        cnn=exts.create_mongo_cnn()

        exists=mongo.info_search(query_dt,cnn).count()

        cnn.close()

        if (~((inv_id==session['inv_id'])&(org_name==session['org_name'])&(jur_per_id==session['jur_per_id'])))&(exists>0):
            flash("所修改样本的样本编码、保存机构名称和法人机构代码与样本库中已有样本重复，请重新修改！")
        else:

            update_dt={}
            update_dt['inv_id']=rc['inv_id']
            if rc['sam_cate_name']=="":
                update_dt['sam_cate_name']=rc['pre_sam_cate_name']
            else:
                update_dt['sam_cate_name']=rc['sam_cate_name']

            update_dt['ent_date']=rc['submit_year']+'-'+rc['submit_month']+'-'+rc['submit_day']
            update_dt['stor_meth']=rc['stor_meth']
            update_dt['parent_id']=rc['parent_id']
            update_dt['batch_count']=rc['batch_count']
            update_dt['sam_qty']=rc['sam_qty']
            update_dt['uni_amou']=rc['uni_amou']
            update_dt['consent']=rc['consent']
            update_dt['sam_title']=rc['sam_title']
            update_dt['sam_desc']=rc['sam_desc']
            update_dt['keyword']=rc['keyword']
            update_dt['sam_uses']=rc['sam_uses']
            update_dt['acqui_pos']=rc['acqui_pos']
            update_dt['s_pre_c']=rc['s_pre_c']
            update_dt['acqui_mot']=rc['acqui_mot']
            update_dt['acqui_time']=rc['collect_year']+'-'+rc['collect_month']+'-'+rc['collect_day']
            update_dt['acqui_plan']=rc['acqui_plan']
            update_dt['acqui_org']=rc['acqui_org']
            update_dt['acqui_assis']=rc['acqui_assis']
            update_dt['org_name']=rc['org_name']
            update_dt['jur_per_name']=rc['jur_per_name']
            update_dt['jur_per_id']=rc['jur_per_id']
            update_dt['jur_per_type']=rc['jur_per_type']
            update_dt['org_intro']=rc['org_intro']
            update_dt['use_agr']=rc['use_agr']
            update_dt['share_rule']=rc['share_rule']
            update_dt['adr']=rc['adr']
            update_dt['post_code']=rc['post_code']
            update_dt['manager_name']=rc['manager_name']
            update_dt['tel']=rc['tel']
            update_dt['email']=rc['email']
            update_dt['don_id']=rc['don_id']
            update_dt['gender']=rc['gender']
            update_dt['date_of_bir']=rc['date_of_bir']
            update_dt['eth_gro']=rc['eth_gro']
            update_dt['nativ_pla']=rc['nativ_pla']
            update_dt['bir_pla']=rc['bir_pla']
            update_dt['nation']=rc['nation']
            update_dt['occup']=rc['occup']
            update_dt['edu_lev']=rc['edu_lev']
            update_dt['mari_sta']=rc['mari_sta']
            update_dt['donate_way']=rc['donate_way']
            update_dt['dise_name']=rc['dise_name']
            update_dt['dise_id']=rc['dise_id']
            update_dt['dig_desc']=rc['dig_desc']
            update_dt['dise_his']=rc['dise_his']
            update_dt['exa_rec']=rc['exa_rec']
            update_dt['inter_rec']=rc['inter_rec']
            update_dt['media_rec']=rc['media_rec']
            update_dt['medi_rep']=rc['medi_rep']
            update_dt['fam_his']=rc['fam_his']
            update_dt['prj_name']=rc['prj_name']
            update_dt['prj_id']=rc['prj_id']
            update_dt['prj_level']=rc['prj_level']
            update_dt['spon_org']=rc['spon_org']
            update_dt['in_level']=rc['in_level']
            update_dt['prj_keyword']=rc['prj_keyword']
            update_dt['aim']=rc['aim']
            update_dt['mtd']=rc['mtd']
            update_dt['total_amt']=rc['total_amt']
            update_dt['be_time']=rc['be_year']+'-'+rc['be_month']+'-'+rc['be_day']
            update_dt['end_time']=rc['end_year']+'-'+rc['end_month']+'-'+rc['end_day']


            cnn=exts.create_mongo_cnn()
            mongo.info_update(query_dt,update_dt,cnn)
            cnn.close()
            flash("样本信息修改成功！")




        return redirect(url_for('sample.render_ele_search'))





@sample.route('/sample/smpdelete/<inv_id>/<org_name>/<jur_per_id>',methods=['POST','GET'])
@login_required
def render_delete(inv_id,org_name,jur_per_id):

    if request.method=='GET':

        delete_dt={'inv_id':inv_id,'org_name':org_name,'jur_per_id':jur_per_id}


        cnn=exts.create_mongo_cnn()
        mongo.info_delete(delete_dt,cnn)
        cnn.close()


        flash("样本已删除！")

        return redirect(url_for('sample.render_ele_search'))



    else:
        pass





@sample.route('/download_data_template',methods=['GET'])
def render_data_template():
    file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_name=file_path+'/'+"样本信息收集表.xlsx"
    response = make_response(send_file(file_name))
    basename = os.path.basename(file_name)
    response.headers["Content-Disposition"] = \
        "attachment;" \
        "filename*=UTF-8''{utf_filename}".format(
            utf_filename=quote(basename.encode('utf-8'))
        )
    return response





















































