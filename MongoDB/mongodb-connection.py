import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]
mycollection = mydb["products"]



#print(myclient.list_database_names())  #veri tabanlarını görüntüleme

# product = {"name":"Xiaomi Mİ 9", "price":2900}

# result = mycollection.insert_one(product)

# print(result)   #Bir Kaydı Listeye ekler.
# print(type(result))
# print(result.inserted_id)


productListe =[
        {"name":"Xiaomi Mİ 9", "price":2900, "description":"İyi telefon"},
        {"name":"Xiaomi Mİ 8", "price":1900 ,"categories":['telefon','elektronik']},
        {"name":"Xiaomi Mİ 6", "price":1900},
        {"name":"Xiaomi Mİ 5", "price":1900},
        {"name":"Xiaomi Mİ 4", "price":1900},
        {"name":"Xiaomi Mİ 3", "price":900}

]

result = mycollection.insert_many(productListe)
print(result.inserted_ids)







