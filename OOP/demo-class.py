class Pet:
  
    def __init__(self,isim,cins) -> None:
          
        self.cinsler = ["Kedi","Kaplumbağ","Köpek","Kuş"]
        if cins not in Pet.cinsler:
            raise ValueError(f"{cins} bir evcil hayvan değildir.")
        self.isim = isim
        self.cins = cins


    def set_cşns(self,cins):
        self.cinsler = ["Kedi","Kaplumbağ","Köpek","Kuş"]
        if cins not in Pet.cinsler:
            raise ValueError(f"{cins} bir evcil hayvan değildir.")
        self.isim = isim
        self.cins = cins





boncuk = Pet("Boncuk","Köpek")

mavis = Pet("Mavis","ASLAN")

Pet.cinsler.append("Balık")

print(Pet.cinsler)
print(boncuk)