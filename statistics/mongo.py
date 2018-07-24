def get_orglist(cnn):
    db=cnn.sampledb
    cl=db.saminfo
    org_list=cl.find({}).distinct("org_name")
    return org_list


def get_count(org_name,cnn):
    db=cnn.sampledb
    cl=db.saminfo
    count=cl.find({'org_name':org_name}).count()
    return count


def get_date(org_name,cnn):
    db=cnn.sampledb
    cl=db.saminfo
    date_list=cl.find({'org_name':org_name}).sort('upload_time',-1).distinct('upload_time')

    return date_list


def get_count_of_date(org_name,upload_time,cnn):
    db=cnn.sampledb
    cl=db.saminfo
    count=cl.find({'org_name':org_name,'upload_time':upload_time}).count()

    return count

def get_sample_num(cnn):
    db=cnn.sampledb
    cl=db.saminfo
    sum=cl.find({}).count()
    return sum