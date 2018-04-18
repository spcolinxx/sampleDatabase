from exts import db
from models import User_info


def idf_user(id):
    user=User_info.query.filter(User_info.user_account==id).first()

    return user

def new_account(account,psd,lv):
    user=User_info(user_account=account,user_psd=psd,user_lv=lv)
    db.session.add(user)
    db.session.commit()


def psd_change(account,psd):
    user=User_info.query.filter(User_info.user_account==account).update({
    'user_psd':psd
    })
    db.session.commit()

def lv_change(account,lv):
    user=User_info.query.filter(User_info.user_account==account).update({'user_lv':lv})
    db.session.commit()