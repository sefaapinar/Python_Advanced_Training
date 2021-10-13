liste = ["1","2","3","4","5","10aa","23ab"]

#1. liste elemanları içindeki sayısal değerleri bulunuz.

for x in liste:
    try:
        sonuc = int(x)
        print(sonuc)
    except ValueError:
        continue

#2. Kullanıcı quit degerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz ve aksi takdirde hata mesajı yazınız.

while True:
    sayi = input('Sayı: ')
    if(sayi == 'q'):
        break
    try:
        sonuc = float(sayi)
        print(f'girilen sayı: {sonuc}')
        break
    except ValueError:
        print('Geçersiz Sayı.')
        continue

#3. Dictionary ve key bilgilerini parametre olarak alan get fonksiyonunu yazınız.


urun = {"urunAdi":"samsung s10"}

def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None
print(get(urun,'fiyat'))