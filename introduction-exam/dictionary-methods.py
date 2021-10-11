opelObj = {
    "marka" :"Opel",
    "model" :"Corsa",
    "yil" : 2021
}

sonuc = opelObj["marka"]
sonuc = opelObj.get("marka")


for x in opelObj:
    print(opelObj[x])






obj = opelObj

opelObj.update({
    "marka":"BMW",
    "model":"320İ"
})
obj["marka"] = "Mercedes"
print(obj)
print(sonuc)

