liste = [10,4,7,9,70]

sayilar = []

for i in liste:
    i*=2
    sayilar.append(i)

sayilar =[i*i for i in range(10)]

# #[expression for item in list]

# sayilar =[i*2 for i in liste]

isim = "Ahmet"
isimler = ["Ahmet","Ali","Çınar","Deniz"]

# sonuc = [str(sayi)for sayi in liste]
# sonuc = [c.upper() for c in isim]
sonuc = [name.lower() for name in isimler]


print(sonuc)

