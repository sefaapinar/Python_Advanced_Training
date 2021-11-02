data = {
    "sefapinar":{
        "firstName":"Sefa",
        "lastName":"Pınar"
    },
    "tamerpinar":{
        "firstName":"Tamer",
        "lastName":"Pınar"
    }
}

import json

with open("JSON/users2.json","w") as file:
    json.dump(data,file,ensure_ascii=False,indent=2)

with open("JSON/users2.json") as file:
    users = json.load(file)

print(users["sefapinar"])