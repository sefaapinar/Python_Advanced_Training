sayilar = [1,3,5,66,64,213,411]
harfler = ['a','b','c']
isimler = ['Sefa','Fatih','Mehmet']

sonuc = min(harfler)
sonuc = min(sayilar)
sonuc = min(harfler)

sonuc = max(harfler)
sonuc = max(sayilar)

sonuc = max(isimler, key = lambda n: len(n))

print(sonuc)