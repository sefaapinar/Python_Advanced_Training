isimler = ["Ahmet","Sefa","Melih","Yasin"]
string = "Hello my name is sefa."
yillar = [2000,1999,1987,1954]
dereceler = [20,5,15,-2,3,0,-6]

#1 ile 100 arasında ki sayıları 12 ye bölünenlerin listesini hazırla.

# sonuc =[i for i in range(1,101) if i%3==0 if i%4==0]
# print(sonuc)

#2 İsimler listesindeki her ismi küçük harfle çevirip tersten yazdırınız.

# sonuc = [i.lower()[::-1] for i in isimler]
# print(sonuc)

#3 Verilen string içindeki rakamları içeren bir liste oluşturunuz.

# sonuc = [i for i in string if i.isdigit()]

#4 Yıllar dizisindeki her doğum yılı için yaş bilgisini içeren liste oluşturunuz.

# import datetime
# simdi = datetime.datetime.now().year
# sonuc = [ simdi-yil for yil in yillar]
# print(sonuc)

#5 Dereceler listesinde bulunan hava sıcaklık bilgisine göre eksi değer için buzlanma tehlikesi verilsin.

sonuc = [i if i>0 else "Buzlanma tehlikesi" for i in dereceler]
print(sonuc)