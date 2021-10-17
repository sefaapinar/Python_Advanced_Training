class Product:
    def __init__(self,_name,_price): #Class içerisine bir özellik tanımlamak için kullanılır.
        self.name = _name
        self.price = _price
        print('Product Nesneni Oluşturuldu.')
p1 = Product("Samsung s10",7450)
p2 = Product("Iphone 12",17000)

print(p1.name,p1.price)
print(p2.name,p2.price)
