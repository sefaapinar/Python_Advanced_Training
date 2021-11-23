import numpy as np

result = np.array(["10","15","30","45","60"])

result = np.arange(5,15)

result = np.arange(5,100,5)

result = np.zeros(10) #0'lardan olusan dizi olusturur.

result = np.ones(15) #1'lerden olusan dizi olusturur.

result = np.linspace(0,100,5) #'her parcayı böler

result = np.random.randint(10,30,5)

result = np.random.randn(10) # -1 ile +1 arasındaki 10 sayıyı getirir.

result = np.random.randint(10,50,15).reshape(3,5) # dizi yapmak.

# result = np.random.randint(10,50,15).reshape(3,5)
# rowTotal = matris.sum(axis = 1)
# colTotal = matris.sum(axis=0)

# print(rowTotal)
# print(colTotal)

print(result)