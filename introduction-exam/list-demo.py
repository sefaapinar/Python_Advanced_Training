
telefonlar  = ["Samsung S5","Samsung S6","Samsung S7","Samsung S8"]
sonuc = len(telefonlar)

sonuc = telefonlar[0]

telefonlar[0] = "Samsung S9"
sonuc = telefonlar

if "Samsung S6" in telefonlar:
    print("Samsung S6 Liste İçerisinde Var.")

sonuc = telefonlar[-3]

sonuc = telefonlar[0:2]

telefonlar[-2:] = ["Samsung S9","Samsung S10"]
sonuc = telefonlar

print(sonuc)

ogrenciA = ["Sefa","Pınar",2000,[70,60,12]]
ogrenciB = ["Fatih","Jestof",2000,[70,40,12]]
ogrenciC = ["Mehmet","Ar",2000,[70,80,12]]

ogrenciler = [ogrenciA,ogrenciB,ogrenciC]

for ogrenci in ogrenciler:
    print(ogrenci[0])

