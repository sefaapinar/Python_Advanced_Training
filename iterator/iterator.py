#iterable?
#iterator?

from typing import Iterator


sayilar = [1,2,3,4,5]


iterator = iter(sayilar)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator)) # Eleman Sayısı kadar döner.

while True:
    try:
        elemanBilgisi = next(iterator)
        print(elemanBilgisi)
    except StopIteration:
        break