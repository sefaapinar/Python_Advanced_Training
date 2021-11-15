import numpy as np

#Numpy -Veri analizi Kütüphanesi
#python list



py_list = [1,2,3,4,5,6,7,8,9]


#numpy array 

np_arry = np.array([1,2,3,4])

print(type(py_list))
print(type(np_arry))


py_multi = [[1,2,3,],[23,44,5,],[5,7,8]]
np_multi = np_arry.reshape(3,3)


print(py_multi)
print(np_multi)

print(np_arry.ndim)
print(np_multi.ndim)

print(np_arry.shape)
print(np_multi.shape)