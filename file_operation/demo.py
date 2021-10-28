#1- Kullanıcıdan aldığı ürün bilgisini urunler.txt dosyasına kayıt eden fonksiyonu yazınız.

def urun_ekle(ad,fiyat):
    with open("urunler.txt","a",encoding="UTF-8") as file:
        file.write(f"ad: {ad} fiyat: {fiyat}")

urun_ekle("Samsung s10",5000)
urun_ekle("Samsung S11",12000)


#2-Dosya ismi, eski kelime ve yeni kelime parametrelerini alarak dosyada bir güncelleme yapan fonksiyon.

def bul_ve_degistir(dosya_ismi,eski_kelime,yeni_kelime):
    with open(dosya_ismi,"r+") as file:
        text = file.read()
        yeni_text = text.replace(eski_kelime,yeni_kelime)
        file.seek(0)
        file.write(yeni_text)

bul_ve_degistir("urunler.txt","s10","s9")