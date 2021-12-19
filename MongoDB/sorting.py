import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]
mycollection = mydb["products"]


result = mycollection.find().sort('name',1)  #SIRALAMA İSLEMLERİ

result = mycollection.find().sort('price',-1)

result = mycollection.find().sort([('name',1), ('price',-1)])


for i in result:
    print(i)
