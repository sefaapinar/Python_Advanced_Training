import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]
mycollection = mydb["products"]


# update_one
# update_many

# mycollection.update_one({'name':'Xiaomi Mİ9'},
#     {'$set': {
#         'name':'Iphone 12'
#     }})  #güncelleme islemleri

# for i in mycollection.find():
#     print(i)


# delete_one()
# delete_many()

for i in mycollection.find():
    print(i)


print('*'*50)

mycollection.delete_one({"name:","Xiaomi MI 6"})

for i in mycollection.find():
    print(i)

    