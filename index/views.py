from . import index
from . import mongo


from flask import render_template,request,flash,redirect,session,url_for,json
from flask.ext.login import LoginManager,login_user, logout_user,login_required
import exts



@index.route('/index',methods=['POST','GET'])
@login_required
def render_index():

    return render_template('index.html')

    # if request.method=='GET':
    #     cnn=exts.create_mongo_cnn()
    #     dt=mongo.get_sample_count(cnn)
    #     cnn.close()
    #
    #     mydata = [
    #         {'name': '北京', 'value': 1000}, {'name': '天津', 'value': 1000},
    #         {'name': '上海', 'value': 10000}, {'name': '重庆', 'value': 10000},
    #         {'name': '河北', 'value': 100000}, {'name': '河南', 'value': 100000},
    #         {'name': '云南', 'value': 1000000}, {'name': '辽宁', 'value': 1000000},
    #         {'name': '黑龙江', 'value': 10000000}, {'name': '湖南', 'value': 10000000},
    #         {'name': '安徽', 'value': 10000000}, {'name': '山东', 'value': 10000000},
    #         {'name': '新疆', 'value': 1000000}, {'name': '江苏', 'value': 1000000},
    #         {'name': '浙江', 'value': 100000}, {'name': '江西', 'value': 1000000},
    #         {'name': '湖北', 'value': 10000000}, {'name': '广西', 'value': 100000},
    #         {'name': '甘肃', 'value': 1090900}, {'name': '山西', 'value': 1298371},
    #         {'name': '内蒙古', 'value': 141}, {'name': '陕西', 'value': 1235345},
    #         {'name': '吉林', 'value': 12341451}, {'name': '福建', 'value': 1234123},
    #         {'name': '贵州', 'value': 123412}, {'name': '广东', 'value': 123413412},
    #         {'name': '青海', 'value': 1234121}, {'name': '西藏', 'value': 12341234},
    #         {'name': '四川', 'value': 123213421}, {'name': '宁夏', 'value': 1234123},
    #         {'name': '海南', 'value': 1234123}, {'name': '台湾', 'value': 1234123},
    #         {'name': '香港', 'value': 1234132}, {'name': '澳门', 'value': 1234}
    #     ]
    #
    #
    #
    #     return render_template('map_page.html',dt=json.dumps(mydata))
    # else:
    #     pass


#
# @index.route('/test/')
# def test():
#     return render_template('index.html')