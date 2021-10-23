import random  #Bu tanımlama ise genel olarak bütün özelliklerini kullanma özelliği
from random import shuffle #Bu sadece kullanılmak istenen özellik
class Kart:
    def __init__(self,tip,deger) -> None:
        self.tip = tip
        self.deger = deger


    def __repr__(self) -> str:  #Representation 
        return f"{self.tip} {self.deger}"


class Deste:
    tipler = ["karo","sinek","kupa","maça"]
    degerler = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self) -> None:
        self.kartlar = [Kart(tip,deger) for tip in Deste.tipler for deger in Deste.degerler]
        
        print(self.kartlar)

    def kartSayisi(self):
        return len(self.kartlar)

    def kartlariKaristir(self):
        if(self.kartSayisi()<52):
            raise ValueError("Deste Bozulmadan Kartları Karıştırabilirsiniz.")
        shuffle(self.kartlar)

    def kartDagit(self,adet):
        kartSayisi = self.kartSayisi()
        adet = min([kartSayisi,adet])
        if kartSayisi == 0:
            raise ValueError("Bütün Kartlar Dağıtıldı.")
            kartlar = self.kartlar[-adet:]
            
            self.kartlar = self.kartlar[:-adet]
            return kartlar

            [1,3,5,6,7]

deste1 = Deste()
deste1.kartlariKaristir()

# sonuc = deste1.kartSayisi()
# deste1.kartlariKaristir()
# deste1.kartDagit(5)

print(deste1.kartDagit(5))
print(deste1.kartSayisi())
print(deste1.kartDagit(3))

print(deste1.kartlar)
# print(sonuc)
