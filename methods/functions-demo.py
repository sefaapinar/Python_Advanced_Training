# def yazdir(txt,adet):
#     print(txt * adet)
# yazdir('Merhaba\n',5)

#Hesaplama

# def hesapla(kisa,uzun):
#     alan = kisa * uzun
#     cevre = 2 *(kisa+uzun)

#     print(f"Alan: {alan} Çevre: {cevre}")
# hesapla(7,1)

#YAZI TURA AT

# def yaziTuraAt():
#     import random
#     sayi = random.random()

#     if sayi>0.5:
#         return "Tura"
#     else:
#         return "Yazı"
# print(yaziTuraAt())

#Asal Sayiları Bul



def asalSayilariBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2):
        if(sayi1>1):
            for i in range(2,sayi):
                if(sayi% i ==0):
                    break
            else:
              print(sayi)
asalSayilariBul(10,20)