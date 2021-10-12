def selamlama(isim,mesaj):
    print(f"{mesaj} {isim}")

selamlama("Sefa","Günaydın")
selamlama("Sefa","İyi Günler")

def usAlma(taban,us):
    return taban **us
sonuc = usAlma(2,3)
print(sonuc)


def toplam(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def islem(a,b,fn):
    return fn(a,b)

sonuc = islem(1,3,cikarma)

print(sonuc)