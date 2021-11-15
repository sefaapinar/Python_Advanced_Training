import numpy as np

numbers = np.array([1,2,3,4,5,67,77,34])

result = numbers[6]
result = numbers[-1]
result = numbers[0:3]
result = numbers[3:3]
result = numbers[::]
result = numbers[::-1]
print(result)

numbers2 = np.array([[1,2,3],[3,4,3,2],[3,2,4,3,2]])
print(numbers2)

