class Product:
    def __init__(self,name,price) -> None:
        self.name = name
        if price >=0:
            self._price = price
        else:
            raise ValueError("Ürün Fiyatına Negatif değer ataması yapılamaz.")


    def set_price(self,value):
        if value >=0:
            self._price = value
        else:
            raise ValueError("Ürün Fiyatına Negatif Değer Girmeyin.")
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if value >=0:
            self._price = value


    def get_price(self):
        return self._price

p = Product("İphone 12 ", 14000)


# p.price = -14000
# print(p.price)

print(p.get_price())
p.price = -9000
print(p.price)