def toplam (*args):
    print(type(args))
    sonuc = 0 

    for i in args:
        sonuc +=i
    return sonuc

print(toplam(10,20,30))