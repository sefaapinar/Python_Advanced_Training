#1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
#"random modülü için pyhton random şeklinde arama yapın."
## "100 üzerinden puanlama yapalım." her soru 20 puan.
## hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplanır.

from math import tanh
import random

sayi = random.randint(1,10)
hak = 5
sayac =0
while hak > 0:
    hak-=1
    sayac +=1
    tahmin = int(input('tahmin: '))
    
    if sayi == tahmin:
        print(f"Tebrikler {sayac}.defa da Bildiniz. Toplam Puanınız:{100 -(20)*(sayac-1)}")
        break
    elif sayi>tahmin:
        print('Yukarı')
    else:
        print('Aşağı')
    if hak == 0:
        print(f"Hakkınız bitti. Tutulan sayı: {sayi}")
