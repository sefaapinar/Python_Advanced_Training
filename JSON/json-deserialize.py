#serialize



#deserialize

import json

# with open("JSON/person.json") as file:
#     data = json.load(file)

data ="""
{
    "firstName":"Sefa",
    "lastName":"Pınar",
    "hobbies":["Spor","Sinema","Dizi"],
    "age":21
   
}
"""

data = json.loads(data)

print(data)
print(type(data))
print(data["hobbies"])


