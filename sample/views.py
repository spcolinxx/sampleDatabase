from flask import render_template,redirect,url_for,session,flash
from . import sample
import datetime
from flask import request
from . import read_file
import xlrd
from . import db_op
from flask.ext.login import LoginManager,login_user, logout_user,login_required
from . import schema_validate
import exts
import datetime

# @sample.route('/sample/addSample')
# @login_required
# def render_addSample():
#     current_year=datetime.datetime.now().year
#     return render_template('addSample.html',current_year=current_year)







@sample.route('/sample/batchAdd',methods=['GET','POST'])
@login_required
def render_batchAdd():
    if request.method=='GET':
        return render_template('batchAdd.html')
    else:
        file=request.files['file_input']
        file_trans=xlrd.open_workbook(filename=None,file_contents=file.read())

        read_rst=read_file.read_file(file_trans)



        if read_rst[0]==False:
            for i in read_rst[1]:
                flash(i)



            return redirect(url_for('sample.render_batchAdd'))
        else:
            excel_data=read_rst[1]
            err_log=schema_validate.schema_check(excel_data)

            if len(err_log)>0:
                flash("添加样本失败，样本格式与规定格式不符！")
                for i in err_log:
                    for j in i[1]:
                        flash("第"+str(i[0]+1)+"条记录错误信息："+str(j))
            else:

                sp_rst=db_op.sp_data(excel_data)
                sampleinfo_data=sp_rst[0]
                orginfo_data=sp_rst[1]
                donorinfo_data=sp_rst[2]
                projectinfo_data=sp_rst[3]


                sqldb=exts.create_sqldb_conn()

                db_op.sampleinfo_insert(sampleinfo_data,sqldb)
                db_op.orginfo_insert(orginfo_data,sqldb)
                db_op.donorinfo_insert(donorinfo_data,sqldb)
                db_op.projectinfo_insert(projectinfo_data,sqldb)


                sqldb.close()

                flash("批量样本添加完成！")


            return redirect(url_for('sample.render_batchAdd'))



@sample.route('/sample/search',methods=['GET','POST'])
@login_required
def render_search():
    if request.method=='GET':
        orgls=db_op.search_org()

        return render_template('search.html',orgls=orgls)
    else:
        inv_id=request.form.get('inv_id')
        org_name=request.form.get('org_name')

        search_rst=db_op.search_info(inv_id,org_name)

        if search_rst==None:
            flash("无此样本编号，请重新输入！")
            return redirect(url_for('sample.render_search'))
        else:
            session['sam_uni_id']=search_rst[0]
            session['inv_id']=search_rst[1]
            session['org_name']=search_rst[21]


            return  render_template('search_rst.html' ,search_rst=search_rst)

@sample.route('/sample/ele_search',methods=['POST','GET'])
@login_required
def render_ele_search():
    search_item = ["样本编码", "样本类别", "入库日期", "保存温度", "母本编码", "分管数", "样本量", "量单位", "知情同意", "样本别称", "样本描述", "关键词", "样本用途",
                   "采集部位", "分析前变量"
        , "采集动因", "采集时间", "采集计划", "采集机构", "其他采集者", "保存机构名称", "法人机构名称", "法人机构代码", "法人机构类型", "保存机构简介", "使用许可", "共享方式",
                   "通信地址",
                   "邮政编码", "管理员", "联系电话", "电子信箱", "捐献者匿名编号", "性别"
        , "年龄", "民族", "籍贯", "出生地", "国籍", "职业", "教育程度", "婚姻状况", "捐献途径", "疾病类目名称", "疾病类目代码", "主要诊断", "现病史", "检验记录",
                   "随访记录", "影像资料", "病例报告", "家系信息"
        , "课题名称", "课题编号", "课题级别", "资助机构", "纳入标准", "课题关键词", "收集目的", "收集方法", "收集数量", "起止时间"]
    if request.method=='GET':

        return render_template('ele_search.html',search_item=search_item)

    else:
        dt=request.form.to_dict()
        item_name=list(dt.keys())
        item_value=list(dt.values())



        if len(item_name)>0:

            sqldb = exts.create_sqldb_conn()

            search_rst=db_op.ele_search(item_name,item_value,sqldb)
            ln=len(search_rst)



            sqldb.close()

            if ln>0:

                for i in search_rst:
                    if i[9] == 0:
                        i[9] = "不同意"
                    else:
                        i[9] = "同意"

                return render_template('search_rst.html',search_rst=search_rst[0],rst=search_rst,ln=ln)
            else:
                flash("无符合条件的记录！")

                return  redirect(url_for('sample.render_ele_search'))
        else:
            flash("请添加搜索关键词！")

            return redirect(url_for('sample.render_ele_search'))



@sample.route('/to_update',methods=['POST','GET'])
def to_update():
    inv_id=request.form.get("inv_id")
    org_name=request.form.get("org_name")
    session["inv_id"]=inv_id
    session["org_name"]=org_name


    return ""

@sample.route('/to_delete',methods=['POST','GET'])
def to_delete():

    sam_uni_id=request.form.get('sam_uni_id')
    session['sam_uni_id']=sam_uni_id

    return ""



@sample.route('/sample/smpUpdate/',methods=['POST','GET'])
@login_required
def render_update():
    if request.method=='GET':


        search_rst = db_op.search_info(session.get('inv_id'),session.get('org_name'))
        print(search_rst)
        current_year = datetime.datetime.now().year


        cate_ls=db_op.get_cate()
        l1=cate_ls[0]
        l2=cate_ls[1]
        l3=cate_ls[2]
        l4=cate_ls[3]

        tmp=str(search_rst[3])
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



        temp=search_rst[4]
        temp_ls=["室温","2°C～10°C","-35°C～-18°C","-85°C～-60°C","-196°C～-150°C","液氮","其它方式"]
        if temp in temp_ls:
            temp_ls.remove(temp)

        agr=[]
        nagr=[]
        agr.append(search_rst[9])
        if agr[0]==True:
            agr.append("同意")
            nagr.append("False")
            nagr.append("不同意")
        else:
            agr.append("不同意")
            nagr.append("True")
            nagr.append("同意")


        sx=[]
        sx.append(search_rst[34])
        if sx[0]=="男":
            sx.append("女")
        else:
            sx.append("男")

        age=search_rst[35]

        age_ls=[]

        for i in range(1,151):
            age_ls.append(i)

        if age in age_ls:
            age_ls.remove(age)


        ac_tmp=str(search_rst[17])
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




        return render_template('smpUpdate.html',search_rst=search_rst,l1=l1,l2=l2,l3=l3,l4=l4,in_date=in_date,in_year_ls=in_year_ls,in_month_ls=in_month_ls,
                               in_day_ls=in_day_ls,temp=temp,temp_ls=temp_ls,agr=agr,nagr=nagr,sx=sx,age=age,age_ls=age_ls,ac_date=ac_date,
                               ac_year=ac_year,ac_month=ac_month,ac_day=ac_day)
    else:

        ps_ls=[]
        ps_ls.append(request.form.get('sam_uni_id'))
        ps_ls.append(request.form.get('inv_id'))


        if request.form.get('new_cate_code')=="":

            ps_ls.append(request.form.get('smp_cate'))
        else:
            ps_ls.append(request.form.get('new_cate_code'))

        submit_date=str(request.form.get('submit_year'))+"-"+str(request.form.get('submit_month'))+"-"+str(request.form.get('submit_day'))
        ps_ls.append(datetime.datetime.strptime(submit_date,'%Y-%m-%d'))
        ps_ls.append(request.form.get('temperature'))
        ps_ls.append(request.form.get('parent_id'))
        ps_ls.append(request.form.get('same_batch_count'))
        ps_ls.append(request.form.get('smp_count'))
        ps_ls.append(request.form.get('unit'))
        agr=request.form.get('awareness')
        if agr=='True':
            ps_ls.append(True)
        else:
            ps_ls.append(False)

        ps_ls.append(request.form.get('smp_name'))
        ps_ls.append(request.form.get('smp_desc'))
        ps_ls.append(request.form.get('keyword'))
        ps_ls.append(request.form.get('uses'))
        ps_ls.append(request.form.get('part'))
        ps_ls.append(request.form.get('pre_variable'))
        ps_ls.append(request.form.get('reason'))
        ac_date=str(request.form.get('collect_year'))+"-"+str(request.form.get('collect_month'))+"-"+str(request.form.get('collect_day'))
        ps_ls.append(datetime.datetime.strptime(ac_date,'%Y-%m-%d'))
        ps_ls.append(request.form.get('collect_plan'))
        ps_ls.append(request.form.get('collect_org'))
        ps_ls.append(request.form.get('other_collector'))
        ps_ls.append(request.form.get('org_name'))
        ps_ls.append(request.form.get('jur_name'))
        ps_ls.append(request.form.get('jur_id'))
        ps_ls.append(request.form.get('jur_type'))
        ps_ls.append(request.form.get('org_intro'))
        ps_ls.append(request.form.get('agr'))
        ps_ls.append(request.form.get('share_way'))
        ps_ls.append(request.form.get('adr'))
        ps_ls.append(request.form.get('post_code'))
        ps_ls.append(request.form.get('manager'))
        ps_ls.append(request.form.get('tel'))
        ps_ls.append(request.form.get('email'))
        ps_ls.append(request.form.get('donor_id'))
        ps_ls.append(request.form.get('sex'))
        ps_ls.append(request.form.get('age'))
        ps_ls.append(request.form.get('eth_group'))
        ps_ls.append(request.form.get('nativ_pla'))
        ps_ls.append(request.form.get('bir_pla'))
        ps_ls.append(request.form.get('nation'))
        ps_ls.append(request.form.get('occup'))
        ps_ls.append(request.form.get('edu'))
        ps_ls.append(request.form.get('mari'))
        ps_ls.append(request.form.get('donate_way'))
        ps_ls.append(request.form.get('dise_name'))
        ps_ls.append(request.form.get('dise_id'))
        ps_ls.append(request.form.get('diag'))
        ps_ls.append(request.form.get('dise_his'))
        ps_ls.append(request.form.get('exam_rec'))
        ps_ls.append(request.form.get('itv_rec'))
        ps_ls.append(request.form.get('media_rec'))
        ps_ls.append(request.form.get('medi_rec'))
        ps_ls.append(request.form.get('fam_his'))
        ps_ls.append(request.form.get('prj_name'))
        ps_ls.append(request.form.get('prj_id'))
        ps_ls.append(request.form.get('prj_level'))
        ps_ls.append(request.form.get('spon_org'))
        ps_ls.append(request.form.get('in_std'))
        ps_ls.append(request.form.get('prj_kw'))
        ps_ls.append(request.form.get('aim'))
        ps_ls.append(request.form.get('collect_way'))
        ps_ls.append(request.form.get('collect_count'))
        ps_ls.append(request.form.get('be_end_time'))


        sam_uni_id=request.form.get('sam_uni_id')

        smp=db_op.uni_search(sam_uni_id)

        inv_id=smp.inv_id
        org_name=smp.org_name
        don_id=smp.don_id
        proj_id=smp.proj_id

        smp_check=db_op.up_sam_check(sam_uni_id,ps_ls[1],ps_ls[21])

        if smp_check==True:
            flash("所修改样本的样本编码和保存机构名称与样本库中已有样本重复，请重新修改！")
            return redirect(url_for('sample.render_search'))
        else:
            db_op.sampleinfo_update(sam_uni_id,ps_ls)


            org=db_op.org_search(ps_ls[21])

            if org!=None:
                db_op.orginfo_update(ps_ls)
            else:
                sqldb = exts.create_sqldb_conn()

                org_data = ps_ls[21:33]
                db_op.orginfo_insert([org_data],sqldb)

                sqldb.close()


            don=db_op.donor_search(ps_ls[33],ps_ls[21])

            if don!=None:
                db_op.donorinfo_update(ps_ls)
            else:
                sqldb = exts.create_sqldb_conn()

                donor_data=ps_ls[33:53]
                donor_data.append(ps_ls[21])
                db_op.donorinfo_insert([donor_data],sqldb)

                sqldb.close()


            proj=db_op.proj_search(ps_ls[54],ps_ls[21])

            if proj!=None:
                db_op.projinfo_update(ps_ls)
            else:
                sqldb = exts.create_sqldb_conn()

                prj_data=ps_ls[53:]
                prj_data.append(ps_ls[21])
                db_op.projectinfo_insert([prj_data],sqldb)
                sqldb.close()


            dn_exist=db_op.donor_exist_check(don_id,org_name)

            if dn_exist==None:
                sqldb = exts.create_sqldb_conn()

                db_op.delete_dn_info(don_id,org_name,sqldb)

                sqldb.close()


            proj_exist=db_op.proj_exist_check(proj_id,org_name)
            if proj_exist==None:
                sqldb = exts.create_sqldb_conn()
                db_op.delete_prj_info(proj_id,org_name,sqldb)
                sqldb.close()


            org_exist=db_op.org_exist_check(org_name)
            if org_exist==None:
                sqldb = exts.create_sqldb_conn()
                db_op.delete_org_info(org_name,sqldb)
                sqldb.close()


            flash("样本信息修改完成！")

            return redirect(url_for('sample.render_ele_search'))



@sample.route('/sample/smpdelete/',methods=['POST','GET'])
@login_required
def render_delete():

    if request.method=='GET':
        sam_uni_id=session.get('sam_uni_id')
        smp=db_op.uni_search(sam_uni_id)

        org_name=smp.org_name
        don_id=smp.don_id
        proj_id=smp.proj_id

        db_op.delete_sampleinfo(sam_uni_id)

        dn_exist = db_op.donor_exist_check(don_id, org_name)

        if dn_exist == None:
            sqldb = exts.create_sqldb_conn()

            db_op.delete_dn_info(don_id, org_name, sqldb)

            sqldb.close()

            # db_op.delete_dn_info(don_id, org_name)

        proj_exist = db_op.proj_exist_check(proj_id, org_name)
        if proj_exist == None:
            sqldb = exts.create_sqldb_conn()
            db_op.delete_prj_info(proj_id, org_name, sqldb)
            sqldb.close()
            # db_op.delete_prj_info(proj_id, org_name)

        org_exist = db_op.org_exist_check(org_name)
        if org_exist == None:
            sqldb = exts.create_sqldb_conn()
            db_op.delete_org_info(org_name, sqldb)
            sqldb.close()
            # db_op.delete_org_info(org_name)


        flash("样本已删除！")

        return redirect(url_for('sample.render_ele_search'))



    else:
        pass


























































