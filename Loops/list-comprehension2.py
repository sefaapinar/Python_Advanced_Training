# sayilar =[1,4,5,6,4,2,11,54]
# sonuc = []

# for sayi in sayilar:
#     if(sayi%2==0):
#         sonuc.append(sayi)

# sonuc = [sayi for sayi in sayilar if sayi%2==0]
# sonuc = [sayi if sayi%2==0 else "tek sayı" for sayi in sayilar ]
# print(sonuc)

fiyatlar = [1000,2000,344,12312,3333]
vergiler = []

for fiyat in fiyatlar:
    if(fiyat>0):
        vergiler.append(fiyat*1.18)

vergiler = [fiyat*1.18 for fiyat in fiyatlar if fiyat>0]
vergiler =[fiyat*1.18 if fiyat>0 else "vergi hesaplanmadı" for fiyat in fiyatlar]

print(vergiler)


sonuc = []
for x in range(3):
    for y in range(3):
        sonuc.append((x,y))
        
print(sonuc)
