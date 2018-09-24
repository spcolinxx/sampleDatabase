import exts


cnn=exts.create_mongo_cnn()

db=cnn.sampledb

cl=db.saminfo

# p=cl.find({'$or':[{'inv_id':1},{'inv_id':8}],'$and':[{'upload_time':'2018-09-20 14:20:44'}],'$not':[{}]})


p=cl.find({'inv_id':{'$not':{1}}})

for i in p:
    print(i)

