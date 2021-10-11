# sayi = int(input('Sayı giriniz: '))
# if(sayi>0):
#     if(sayi % 2 == 1):
#         print('Girilen sayı pozitiftir.')
#     else:
#         print('Girilen Sayı Negatiftir.')
# else:
#     print('Lütfen Normal bir sayı giriniz.')

#Bir aracım yakıt tipine göre (benzin, dizel) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.

# benzinFiyat= 7.74
# dizelFiyat = 6.89
# toplamYakitUcreti = 0

# ortalamaYakitTuketimi = float(input('100 Km deki ortalama yakıt tüketimi: '))
# gidilecekYol = float(input('Gidilecek yol kaç km: '))
# yakitTipi = input("Yakıt Tipinizi Giriniz : ")

# toplamYakitUcreti = gidilecekYol * (ortalamaYakitTuketimi / 100)

# if(yakitTipi == "benzin"):
#     toplamYakitUcreti = benzinFiyat * toplamYakitUcreti
# elif(yakitTipi== "dizel"):
#     toplamYakitUcreti = dizelFiyat * toplamYakitUcreti
# else:
#     print("Lütfen Doğru Yakıt Türünü Giriniz...")


# if (toplamYakitUcreti !=0):
#     print(toplamYakitUcreti)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# isim = input('isim: ')
# yas = int(input('yas: '))
# egitim = input('egitim: ')

# if(yas >=18):
#     if(egitim == 'lise' or egitim == 'üniversite'):
#         print('Bu durumlarda Ehliyet Alabilirsiniz.')
#     else:
#         print(f'{isim} ehliyet alamazsınız çünkü eğitim durumuz yetersiz.')
# else:
#     print(f'{isim} ehliyet alamazsınız çünkü yaşınız tutmuyor.')

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import datetime

date = input ('Aracınız hangi tarihte trafiğe çıkmıştır ?  (1021/01/04)')
date = date.split('/')
current = datetime.datetime.now()
trafigeCikis= datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
fark = current - trafigeCikis
gun = fark.days

if(gun<=365):
    print("Muayane olmuştur.")
else:
    print("Lütfen aracınızı bir an önce muayene ettiriniz.")
print(current)