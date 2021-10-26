# sayilar = [1,2,3,4,5]


# iterator = iter(sayilar)
# s = "Hi"

# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator)) # Eleman Sayısı kadar döner.

# def my_for(iterable,func):
#     iterator = iter(iterable)
#     while True:
#         try:
#             elemanBilgisi = next(iterator)
#             func(elemanBilgisi)
#         except StopIteration:
#             break

# my_for(sayilar,print)
# my_for(s,print)

# def kareal(x):
#     print(x*x)

# my_for(iterator,kareal)

class Counter:
    def __init__(self,start,stop) -> None:
        self.start=start
        self.stop =stop

    def __iter__(self):
        return self

    
    def __next__(self):
        if self.start<=self.stop:
            x = self.start
            self.start +=1
            return x
        else:
            raise StopIteration
# iter(Counter(10,20))
# for i in Counter(10,20):
#     print(i)

iterator = iter(Counter(20,30))


while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
    
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
