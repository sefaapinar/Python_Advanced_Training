def dosya_kopyala(dosya_ismi,yeni_dosya_ismi):
    with open(dosya_ismi) as file:
        icerik = file.read()

    with open (yeni_dosya_ismi,"w") as new_file:
        new_file.write(icerik)

dosya_kopyala("msg.txt","msg_yeni.txt")


#Dosya Kopyalama Fonksiyonu işlevsel hale getiriniz.



#eski dosyadaki tüm içerikleri yeni dosyaya tersten yazdıralım.

def ters_cevir(dosya_ismi,yeni_dosya_ismi):
    with open(dosya_ismi) as file:
        icerik = file.read()

    with open(yeni_dosya_ismi,"w") as new_file:
        new_file.write(icerik[::-1])

ters_cevir("msg.txt","msg_yeni.txt")



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



def bilgilendir(dosya_ismi):
    with open(dosya_ismi) as file:
        satirlar = file.readlines()

    sonuc = {
        "satir_sayisi":len(satirlar),
        "kelime_sayisi":sum(satir.split(' ') for satir in satirlar),
        "karakter_sayisi":sum(len(satir)for satir in satirlar)


    }

    print(sonuc)