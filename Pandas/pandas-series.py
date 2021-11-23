import pandas as pd
import numpy as np

#data

numbers = [10,20,30,40,50]
letters = ['a','b','c','d']
scalar = 5
dict = {'a':10,'b':20,'c':30,'d':40}
random_numbers = np.random.randint(10,100,10)

# pandas_series = pd.Series(numbers)
# pandas_series = pd.Series(letters)
# pandas_series = pd.Series(scalar)
# pandas_series = pd.Series(5,[0,1,2,3])
# # pandas_series = pd.Series(numbers,['a','b','c','d'])
# pandas_series = pd.Series(dict)
# pandas_series = pd.Series(random_numbers)

# pandas_series = pd.Series([20,30,40,50],['a','b','c','d'])


# result = pandas_series['a']
# result = pandas_series[0]

# result = pandas_series.shape
# result = pandas_series.dtype
# result = pandas_series.sum()
# result = pandas_series.max()
# result = pandas_series.min()
# result = pandas_series % 2 ==0
























# print(pandas_series)
# print(result)










opel2020 = pd.Series([20,33,56,10],["Astra","Corsa","İnsignia","Mocha","Mokka"])
opel2021 = pd.Series([70,33,56,10],["Astra","Corsa","İnsignia","Grandland","Mokka"])

total = opel2020 + opel2021
print(total)
