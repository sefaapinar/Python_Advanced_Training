db = {
    "users":{
        "sefapinar":{
            "firstName":"sefa",
            "lastName":"pinar"
        },
         "meryempinar":{
            "firstName":"meryem",
            "lastName":"pinar"
    },
    "products":{
        "1":{
            "productName":"Iphone 8",
            "price":5000
        },
         "2":{
            "productName":"Iphone 7",
            "price":4000
        }
    }
    
    }
}

import json
from os import waitpid

# with open("JSON/db.json","w") as file:
#     json.dump(db,file,indent=2)


with open("JSON/db.json") as file:
    json.load(file)


print(db["users"] ["sefapinar"])


db["products"].update({
    "3":{
        "productName":"İphone 12",
        "price":5000
    }
})


with open("JSON/db.json","w") as file:
    json.dump(db,file,indent=2)