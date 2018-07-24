def get_record_list(user_account,cnn):
    db=cnn.sampledb
    cl=db.oprecord
    record_list=cl.find({'account':user_account}).sort("uploadtime",-1).limit(20)

    return record_list



def get_record_detail(dt,cnn):
    db=cnn.sampledb
    cl=db.oprecord
    record_detail=cl.find(dt)

    return record_detail