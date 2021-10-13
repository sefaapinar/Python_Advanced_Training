sayilar = [1,2,5,6,8]
str_sayilar = ["1","3","4"]
# kareleri = []

# for sayi in sayilar:
#     kareleri.append(sayi**2)
# print(kareleri)

# def kareAl(sayi):
#     return sayi **2

# sonuc = list(map(lambda sayi:sayi**2, sayilar))
# print(sonuc)

sonuc = list(map(lambda sayi : sayi **2,sayilar))
sonuc = list(map(int, str_sayilar))
print(str_sayilar)