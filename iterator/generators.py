from typing import Generator


def sayi_say(max):
    sayi = 0
    while sayi<=max:
      yield sayi
    sayi +=1

iterator = sayi_say(100)

# iterator = iter(generator)

# print(next(iterator))

# for i in iterator:
#     print(i)

# sonuc =list(iterator)
# print(sonuc)

generator = [i for i in range(1,10)]

print(generator)