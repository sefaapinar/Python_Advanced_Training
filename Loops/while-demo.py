# sayilar = [4,6,9,10,35,57,89,125,224]

#1: Sayılar listesinde while döngüsü ile ekrana yazdırınız.

# i=0
# while (i<len(sayilar)):
#     print(sayilar[1])
#     i+=1

# while sayilar:
#     print(sayilar.pop(0))

# print(sayilar)

# baslangic = int(input('Baslangic: '))
# bitis = int(input('Bitis: '))
# i=0
# while i<bitis:
#     i+=1
#     if(i%2==1):
#         print(i)

# i = 100

# while (i>0):
#     print(i)
#     i-=1
    
sayilar = []
i = 0
while (i<5):
    sayi = int(input('sayi: '))
    sayilar.append(sayi)
    i+=1
sayilar.sort()
print(sayilar)
