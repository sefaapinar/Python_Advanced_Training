def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')

    ogrenciAdi = liste [0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1+not2+not3) /3

    if ortalama >=90 and ortalama <=100:
        harf = "AA"
    elif ortalama >=70 and ortalama <=90:
        harf = "BB"
    elif ortalama >=50 and ortalama <=70:
        harf ="CC"
    else:
        harf = "FF Kaldınız."

    return ogrenciAdi +" : " + harf + "\n"

def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding="UTF-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad = input('Öğrenci Adı: ')
    soyad = input('Soyad Adı: ')
    not1 = input('Birinci Sınav: ')
    not2 = input('İkinci Sınav: ')
    not3 = input('Üçüncü Sınav: ')

    with open("sinav_notlari.txt","a",encoding="UTF-8") as file:
        file.write(ad+ 'Sefa'+ soyad+ ':'+not1+','+not2+','+not3+'\n')

    
def notlari_kayit_et():
    with open('sinav_notlari.txt',"r",encoding="UTF-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))


        with open("sonuclar.txt","w",encoding="UTF-8") as file2:
            for i in liste:
                file2.write(i)


while True:
    islem  = input('1- Notları Oku\n2- Not Giriniz\n3- Okunan Notları Kayıt Et.\n4- Çıkış\n')

    if islem =='1':
        ortalamalari_oku()
    elif islem =='2':
        not_gir()
    elif islem =='3':
        notlari_kayit_et()
    else:
        break
