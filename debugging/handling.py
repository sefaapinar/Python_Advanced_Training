while True:


    try:
        x = int(input('x: '))
        y = int(input('y: '))                             # HATA OLMASI GEREKEN KODLAR HER ZAMAN TRY İÇERİSİNDE OLUR.
        print(x/y)
    except (ZeroDivisionError,ValueError) as e:
        print('Hata LÜTFEN TEKRAR DENEYİNİZ.')
        print(e)
    except ValueError:
        print('X ve Y Sayısal bir veri olmaılıdır.')
    except:
        print("Bilinmeyen bir hata oluştu.")
    else:
        break
