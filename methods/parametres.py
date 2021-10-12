def selamla(isim):
    return "Merhaba, " + isim

print(selamla("Sefa"))

def toplam(a,b):
    return a+b

sonuc = toplam(10,20)

print(sonuc)

def yasHesapla(dogumYili):
    return 2021 - dogumYili

sonuc = yasHesapla(2000)
print(sonuc)

def emekliligeKacYilKaldi(dogumYili,isim):
    yas = yasHesapla(dogumYili)

    kalanSure = 65-yas

    if kalanSure>0:
        print(f"{isim},emekliliginize {kalanSure} yıl kaldı")
    else:
        print(f"{isim}, zaten{abs(kalanSure)} yıl önce emekli oldunuz")

emekliligeKacYilKaldi(2000,"Sefa")