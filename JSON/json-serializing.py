#serializing
import json

person = {
    "firstName":"Sefa",
    "lastName":"Pınar",
    "hobbies":["Spor","Sinema","Dizi"],
    "age":21
   
}


print(person)
print(person["firstName"])
print(type(person))

sonuc = json.dumps(person,ensure_ascii=False,indent=2)

# print(sonuc)
# print(type(sonuc))

with open("JSON/person.json","w") as file:
    json.dump(person,file, ensure_ascii=False,indent=2)