# def toplam():
#     return 10+20

# sonuc = toplam() + 50
# print(sonuc)

def yil():
    import datetime
    return datetime.datetime.now().year
def yasHesapla():
    return yil() - 2000

sonuc = yasHesapla()

def saat():
    import datetime
    return datetime.datetime.now().hour
def selamla():
    if(saat()<12):
        return "İyi Akşamlar"
    else:
        return "İyi geceler"

sonuc = selamla()
print(sonuc)
