
import pymongo
from pymongo import results


myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]
mycollection = mydb["products"]


#find_one # tek kayıt kullancaksak

# result = mycollection.find_one()
# print(result)

mycollection.find()

for i in mycollection.find({},{"_id":0, "name":1, "price":1}):  #istediğimiz kolonları getirir veya getirmez

    print(i)