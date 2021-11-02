class Product:
    def __init__(self,name,price) -> None:
        self.name= name
        self.price = price


p1 = Product("TV",7000)
p2 = Product("LAPTOP",11111)

products =[p1.__dict__,p2.__dict__]
products ={p1.id: p1.__dict__,
p2.id: p2.__dict__}

import json

print(p1.__dict__)



with open("JSON/newurunler.json","w") as file:
    json.dump(p1.__dict__,file)

with open("JSON/newurunler.json") as file:
    data = json.load(file)

urunler = []
for p in data:
    urunler.append(Product(p["name"],p["price"]))

    print(urunler[0].name)

    