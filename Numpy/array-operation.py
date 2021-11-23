import numpy as np
from numpy.lib.function_base import percentile

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2
result = numbers1 + 10
result = numbers1 - 10
result = numbers1 * numbers2
result = numbers1 / 10

result = np.sin(numbers1)  #sinus alma

result = np.sqrt(numbers1)  #sqrt karakök alma

# result = np.log(numbers1)
# print(result)

mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers1.reshape(2,3)


result = np.vstack((mnumbers1,mnumbers2))

result = numbers1 >= 5
result = numbers1 %2 == 0

print(mnumbers1)
print(result)


