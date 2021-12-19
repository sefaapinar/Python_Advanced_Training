import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]
mycollection = mydb["products"]



# filter = {"name":"Xiaomi Mİ 6"}
# result = mycollection.find(filter)


# result = mycollection.find_one({"_id":ObjectId("61beef8ea3e8525194705aa1")})


# for i in result:
# #     print(i)

# result = mycollection.find({
#     "name":{
#         "$in": ["Xiaomi Mİ9","Xiaomi Mİ8"]
#     }
# # })
# result = mycollection.find({
#     "price":{
#         "$gt": 10000
#     }
# })


result = mycollection.find({
    "name":{"$regex": "^S"}
})

print(result)


