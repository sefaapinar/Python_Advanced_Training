


def urunEkle(urunAdi,fiyat,satistaMi,kategori):
    urun = {
        "urunAdi":urunAdi,
        "fiyat":fiyat,
        "satistaMi":satistaMi,
        "kategori":kategori
    }

import json

with open("JSON/urunler.json","w") as file:
    json.dump(urun, file,ensure_ascii=False)

# urunEkle("İphone 12",10023,"True","Elektronik")

def urunleriGetir():
    import json
    with open("JSON/urunler.json") as file:
        urun = json.load(file)

        kategori = ' '.[kategori for kategoriler in urun["kategori"]]

        print(f'ürün adı: {urun["urunAdi"]} fiyat:{urun["fiyat"]} kategoriler:{kategori}')
urunleriGetir()  