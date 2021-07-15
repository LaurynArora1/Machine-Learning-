import numpy as np

var1 = np.array([(2, 4, 6), (1, 3, 5)])
var2 = np.array([(2, 4, 6), (1, 3, 5)])
var3 = var1 + var2
print(var3)
print(var1.itemsize) # to check the size of a single element in the array
print(var2.dtype) # to check the data type of the elements in the array
print(var3.ndim)
print(var2.ndim) # to check the dimension of array
print(var1.size) # no of elements in the array
print(var2.shape)
var3 = var3.reshape(3, 2)
print(var3.ravel())
print(var1.sum(axis=0))
print(var1.sum(axis=1))
print(np.sqrt(var1)) # a matrix with square roots of all the elements
print(np.std(var2)) # standard deviation
print(np.exp(var1)) # exponential
print(np.log(var1)) # logarithmic
