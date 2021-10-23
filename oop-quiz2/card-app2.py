
class Kart:
    def __init__(self,tip,deger) -> None:
        self.tip = tip
        self.deger = deger

    # def kartiGetir():
    #     return f"{self.tip} {self.deger}"

    def __repr__(self) -> str:  #Representation 
        return f"{self.tip} {self.deger}"

sinek5 = Kart("sinek","5")
karoAs = Kart("karo","A")

# print(sinek5.kartiGetir())
# print(karoAs.kartiGetir())

print(sinek5)
print(karoAs)