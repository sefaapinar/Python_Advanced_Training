sayilar = [12,44,55,66,13]
sonuc = sum(sayilar)
sonuc = sum(sayilar,10)
print(sonuc)

urunler = [
    {"title":"iphone x", "price":123213},
    {"title":"iphone 5", "price":127813},
    {"title":"iphone 6", "price":177213}
]

toplamFiyat = sum([urun["price"] for urun in urunler])

urunAdeti = len([urun for urun in urunler if urun ["price"]>0])



sonuc = round(10,4)

print(toplamFiyat)
print(sonuc)