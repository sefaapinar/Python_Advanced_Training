# (1 - sonsuz) aralığındaki her sayının karesini getiren fonksyionu yazın.


#fibonacci serisini hem normal fonksiyon hemde generator fonksiyonu ile oluşturalum.

# def sonsuz_sayi_uret():
#     sayi = 0
#     while True:
#         yield sayi
#         sayi +=1

# generator = sonsuz_sayi_uret()
# print(next(sonsuz_sayi_uret()))

# for i in generator:
#     print(i)



# def fib_list(max):
#     sayilar = []
#     a,b = 0,1
#     while len(sayilar) < max:
#         sayilar.append(b)
#         a,b = b,a+b
#     return sayilar

# # print(fib_list(1000))

# def fib_generator(max):
#     a,b = 0,1
#     count = 0
#     while len(count)<max:
#         a,b = b,a+b
#         yield b
#         count +=1

# for i in fib_list(10):
#     print(i)

# import sys  #Boyut açısından görmek

# liste = [i*2 for i in range(10000)]
# print(sys.getsizeof(liste))

# gen = (i**2 for i in range(10000))
# print(sys.getsizeof(gen))
        
import time

gen_start_time = time.time()
print(i**2 for i in range(10000))
gen_stop = time.time()-gen_start_time
print(gen_stop) 