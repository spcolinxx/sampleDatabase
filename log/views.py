from . import log
from flask import render_template,request,flash,redirect,session,url_for
from . import db_op
from flask.ext.login import LoginManager,login_user, logout_user,login_required
from . import mongo
import exts
import models




@log.route('/login/',methods=['GET','POST'])
def render_login():
    session['user_lv']=""
    if request.method=='GET':
        return render_template('log_in.html')
    else:
        user_info=request.form.to_dict()

        cnn=exts.create_mongo_cnn()
        user=mongo.search_user(user_info,cnn)
        cnn.close()

        if user==None:
            flash('用户信息输入错误，请重新输入！')
            return render_template('log_in.html')
        else:

            session['user_lv']=user['user_lv']
            user_obj=models.User_obj(user['user_account'],user['user_psd'],user['user_lv'])
            login_user(user_obj)

            return redirect(url_for('index.render_index'))

@log.route('/auth/new_account/',methods=['POST','GET'])
@login_required
def render_new_account():
    if request.method=='GET':
        return render_template('new_account.html')
    else:

        new_user=request.form.to_dict()

        cnn=exts.create_mongo_cnn()
        rp_check=mongo.search_user({"user_account":new_user['user_account']},cnn)
        cnn.close()

        if rp_check!=None:
            flash('该用户已存在，请重新填写账号！')
            return redirect(url_for('log.render_new_account'))
        else:
            cnn=exts.create_mongo_cnn()
            mongo.add_user({'user_account':new_user['user_account'],'account_owner':new_user['account_owner'],'user_psd':new_user['user_psd'],'user_lv':new_user['user_lv']},cnn)
            cnn.close()

            flash("新账号添加成功！")
        return redirect(url_for('log.render_new_account'))




@log.route('/auth/psd_change/',methods=['GET','POST'])
@login_required
def render_psd_change():
    if request.method=='GET':
        user_account=session['user_id']
        return render_template('psd_change.html',user_account=user_account)
    else:
        new_info=request.form.to_dict()
        user_account={'user_account':new_info['user_account']}

        cnn=exts.create_mongo_cnn()
        userinfo=mongo.search_user(user_account,cnn)
        cnn.close()

        if userinfo['user_psd']==new_info['pre_psd']:
            cnn=exts.create_mongo_cnn()
            mongo.psd_change({'user_account':userinfo['user_account'],'user_psd':userinfo['user_psd']},
                             {'user_account':new_info['user_account'],'user_psd':new_info['user_psd']},cnn)
            cnn.close()
            flash("修改密码成功！")
            return redirect(url_for('log.render_psd_change'))
        else:
            flash("旧密码输入错误，请重新输入！")
            return redirect(url_for('log.render_psd_change'))


@log.route('/auth/lv_change/',methods=['POST','GET'])
@login_required
def render_lv_change():
    if request.method=='GET':
        return render_template('lv_change.html')
    else:
        new_lv_info=request.form.to_dict()

        cnn=exts.create_mongo_cnn()
        userinfo=mongo.search_user({'user_account':new_lv_info['user_account']},cnn)
        cnn.close()

        if userinfo==None:
            flash("该账号不存在！")
            return redirect(url_for('log.render_lv_change'))
        else:
            # db_op.lv_change(account,lv)
            cnn=exts.create_mongo_cnn()
            mongo.lv_change({'user_account':new_lv_info['user_account']},{'user_lv':new_lv_info['user_lv']},cnn)
            cnn.close()
            flash("修改权限成功！")

        return redirect(url_for('log.render_lv_change'))



@log.route('/logout',methods=['GET','POST'])
@login_required
def render_logout():
    logout_user()

    return redirect(url_for('log.render_login'))


@log.route('/auth/delete_account',methods=['POST','GET'])
@login_required
def render_delete_account():
    if request.method=='GET':
        return render_template('delete_account.html')
    else:
        dt={'user_account':request.form.get('delete_account')}
        cnn=exts.create_mongo_cnn()
        exist=mongo.search_user(dt,cnn)

        if exist==None:
            flash("该账号不存在，请检查后删除！")
        elif (exist['user_lv']=='0')&(session['user_lv']=='3'):
            flash("当前登录用户权限等级太低，无法删除超级管理员账号！")
        else:
            mongo.del_user(dt,cnn)
            flash("用户账号已删除！")

        cnn.close()
        return render_template("delete_account.html")







@log.route('/auth/user_list/',methods=['POST','GET'])
def render_userlist():
    if request.method=='GET':
        cnn=exts.create_mongo_cnn()
        user_rst=mongo.all_user({},cnn)
        user_list=[]
        for i in user_rst:
            user_list.append(i)

        for i in user_list:
            if i['user_lv']=='0':
                i['user_lv']="管理员"
            elif i['user_lv']=='1':
                i['user_lv']="普通用户"
            else:
                i['user_lv']="游客"

        cnn.close()


        return render_template('user_list.html',user_list=user_list)
    else:
        pass


@log.route('/auth/user_info/<user_account>',methods=['POST','GET'])
def render_userinfo(user_account):
    if request.method=='GET':
        cnn=exts.create_mongo_cnn()
        userinfo=mongo.search_user({'user_account':user_account},cnn)
        if userinfo['user_lv']=='0':
            userinfo['user_lv']="管理员"
        elif userinfo['user_lv']=='1':
            userinfo['user_lv']="普通用户"
        else:
            userinfo['user_lv']="游客"
        cnn.close()

        return render_template('user_info.html',userinfo=userinfo)
    else:
        pass