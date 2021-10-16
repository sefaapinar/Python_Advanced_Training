import db 

def urunEkle(urunAdı,fiyat):
    db.urunler.append({
        "id":len(db.urunler) + 1,
        "urunAdi": urunAdı,
        "fiyat":fiyat
    })

def urunGuncelle(id,urunAdı,fiyat):
    for urun in db.urunler:
        if(urun["id"] == id):
            urun["urunAdi"] = urunAdı
            urun["fiyat"] = fiyat
            break

def urunleriGetir():
    for urun in db.urunler:
        print(f"id {urun['id']} ürün adı: {urun['urunAdi']} fiyat: {['fiyat']}")