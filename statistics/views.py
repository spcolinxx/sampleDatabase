from . import statistics
from flask import render_template,request,flash,redirect,session,url_for,jsonify
from flask.ext.login import LoginManager,login_user, logout_user,login_required
from statistics import mongo
import exts

@statistics.route('/statistics/data_distribution/')
@login_required
def render_distribution():
    cnn=exts.create_mongo_cnn()
    org_name_list=mongo.get_orglist(cnn)
    sample_sum=mongo.get_sample_num(cnn)
    org_dict=[]
    for i in org_name_list:
        count=mongo.get_count(i,cnn)
        org_dict.append({'org_name':i,'count':count})
    cnn.close()


    return render_template('distribution.html',org_dict=org_dict,sample_sum=sample_sum)



@statistics.route('/statistics/org_statistics/',methods=['GET','POST'])
@login_required
def render_org_statistics():
    cnn=exts.create_mongo_cnn()
    org_list=mongo.get_orglist(cnn)
    cnn.close()

    return render_template('org_data.html',org_list=org_list)

@statistics.route('/return_org_info/',methods=['GET','POST'])
@login_required
def return_org_info():
    org_name=request.form.get('org_name')
    org_count=[]

    cnn=exts.create_mongo_cnn()
    org_date=mongo.get_date(org_name,cnn)
    for i in org_date:
        org_count.append(mongo.get_count_of_date(org_name,i,cnn))

    cnn.close()


    return jsonify([org_date,org_count])
