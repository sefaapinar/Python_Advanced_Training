def selamlama(fn):
    def wrapper():
       print("Hoş geldiniz.")
       fn()
       print("Görüşmek Üzere")
    return wrapper

@selamlama  #Decorator kullanımı
def gunaydın():
    
    print("Benim adım sefa")
 
@selamlama #Decorator kullanımı
def iyigunler():

    print("İyi günler benim adım sefa")


# g = selamlama(gunaydın)
# i = selamlama(iyigunler)
# g()
# i()


gunaydın()

