def search_user(dt,cnn):
    db=cnn.sampledb
    cl=db.userinfo
    user_info=cl.find_one(dt)

    return user_info



def add_user(dt,cnn):
    db=cnn.sampledb
    cl=db.userinfo
    cl.insert(dt)


def psd_change(query_dt,dt,cnn):
    db=cnn.sampledb
    cl=db.userinfo
    cl.update(query_dt,{'$set':dt})


def lv_change(query_dt,dt,cnn):
    db=cnn.sampledb
    cl=db.userinfo
    cl.update(query_dt,{'$set':dt})


def all_user(dt,cnn):
    db=cnn.sampledb
    cl=db.userinfo
    user_info=cl.find(dt)
    return user_info

def del_user(dt,cnn):
    db=cnn.sampledb
    cl=db.userinfo
    cl.remove(dt)
