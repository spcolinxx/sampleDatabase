from . import log
from flask import render_template,request,flash,redirect,session,url_for
from . import db_op
from flask.ext.login import LoginManager,login_user, logout_user,login_required




@log.route('/login/',methods=['GET','POST'])
def render_login():
    session['user_lv']=""
    if request.method=='GET':
        return render_template('log_in.html')
    else:
        user_id=request.form.get('user_id')
        user_psd=request.form.get('user_psd')

        user=db_op.idf_user(user_id)

        if user==None:
            flash('无此用户，请重新输入！')
            return render_template('log_in.html')
        elif user.user_psd!=user_psd:
            flash('密码错误！')
            return render_template('log_in.html')
        else:
            session['user_lv']=user.user_lv
            login_user(user)

            return redirect(url_for('sample.render_ele_search'))

@log.route('/auth/new_account/',methods=['POST','GET'])
@login_required
def render_new_account():
    if request.method=='GET':
        return render_template('new_account.html')
    else:
        new_account=request.form.get('new_account')
        psd=request.form.get('psd')
        account_lv=request.form.get('account_lv')
        rp_check=db_op.idf_user(new_account)
        if rp_check!=None:
            flash('该用户已存在，请重新填写账号！')
            return redirect(url_for('log.render_new_account'))
        else:
            db_op.new_account(new_account,psd,account_lv)
            flash("新账号添加成功！")
            return redirect(url_for('log.render_new_account'))




@log.route('/auth/psd_change/',methods=['GET','POST'])
@login_required
def render_psd_change():
    if request.method=='GET':
        user_account=session['user_id']
        return render_template('psd_change.html',user_account=user_account)
    else:
        account=request.form.get('account')
        pre_psd=request.form.get('pre_psd')
        psd=request.form.get('psd')
        user=db_op.idf_user(account)
        if user.user_psd==pre_psd:
            db_op.psd_change(account,psd)
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
        account=request.form.get("account")
        lv=request.form.get("lv")
        user=db_op.idf_user(account)
        if user==None:
            flash("该账号不存在！")
            return redirect(url_for('log.render_lv_change'))
        else:
            db_op.lv_change(account,lv)
            flash("修改权限成功！")

            return redirect(url_for('log.render_lv_change'))



@log.route('/logout',methods=['GET','POST'])
@login_required
def render_logout():
    logout_user()
    return redirect(url_for('log.render_login'))