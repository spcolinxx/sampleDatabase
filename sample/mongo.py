import pymongo.errors
import re


def add_info(dt,cnn):
    try:
        db=cnn.sampledb
        cl=db.saminfo
        cl.insert(dt,continue_on_error=True)
    except Exception:
        pass



def info_search(and_ls,or_ls,nor_ls,cnn):

    if (len(and_ls) == 0):
        and_ls = [{}]
    if (len(or_ls) == 0):
        or_ls = [{}]

    db=cnn.sampledb
    cl=db.saminfo
    if(len(nor_ls)==0):
        rst = cl.find({'$and': and_ls, '$or':or_ls})
    else:
        rst = cl.find({'$and': and_ls, '$or':or_ls,'$nor':nor_ls})


    return rst


def info_update(query_dt,dt,cnn):
    db=cnn.sampledb
    cl=db.saminfo
    cl.update_one(query_dt,{'$set':dt})


def info_delete(dt,cnn):
    db=cnn.sampledb
    cl=db.saminfo
    cl.remove(dt)


def get_catecode(cnn):
    db=cnn.sampledb
    cl=db.catecode
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    code1_dict=cl.find({'cate_level':1})
    for i in code1_dict:
        l1.append([i['cate_mark'],i['cate_name']])

    code2_dict=cl.find({'cate_level':2})
    for i in code2_dict:
        l2.append([i['cate_mark'],i['cate_name']])

    code3_dict = cl.find({'cate_level': 3})
    for i in code3_dict:
        l3.append([i['cate_mark'], i['cate_name']])

    code4_dict = cl.find({'cate_level': 4})
    for i in code4_dict:
        l4.append([i['cate_mark'], i['cate_name']])


    return [l1,l2,l3,l4]


def insert_op_rc(dt,cnn):
    db = cnn.sampledb
    cl = db.oprecord
    cl.insert(dt)