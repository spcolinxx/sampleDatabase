from . import oprecord
from flask import render_template,request,flash,redirect,session,url_for
from flask.ext.login import LoginManager,login_user, logout_user,login_required
import exts
from . import mongo



@oprecord.route('/record_list/',methods=['GET','POST'])
def render_record_list():
    user=session['user_id']
    cnn=exts.create_mongo_cnn()
    record_list=mongo.get_record_list(user,cnn)
    cnn.close()

    return render_template("record_list.html",record_list=record_list)




@oprecord.route('/record_detail/<user_account>/<filename>/<uploadtime>/')
def render_record_detail(user_account,filename,uploadtime):
    cnn=exts.create_mongo_cnn()
    record_list=mongo.get_record_detail({'account':user_account,'filename':filename,'uploadtime':uploadtime},cnn)
    cnn.close()

    record=record_list[0]


    return render_template("record_detail.html",record=record)
