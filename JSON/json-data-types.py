data = [
{
    "username":"sefaapinar",
    "firstName":"Sefa",
    "lastName":"Pınar"

},
{
  "username":"ahmet",
    "firstName":"ahmet",
    "lastName":"Pınar"   
}
]
import json

# with open("JSON/users.json","w") as file:
#     json.dump(data,file,ensure_ascii=False,indent=2)
user ={
    "username":"Tamerpinar",
    "firstName":"Tamer",
    "lastName":"Pınar"  
}

   




with open("JSON/users.json") as file:
   users = json.load(file)

users.append(user)

for user in users:   #Güncelleme İşlemi
    if user["username"]=="sefaapinar":
        user["username"] = "ahmetfatih"


users.remove(users[0]) #Silme İşlemi

print(type(users))


with open("JSON/users.json","w") as file:
    json.dump(users,file,ensure_ascii=False,indent=2)