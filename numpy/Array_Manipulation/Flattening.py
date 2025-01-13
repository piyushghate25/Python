import numpy as np

arr = np.array([1,2,3,4,5,6])

reshaped = arr.reshape((3,2)) 
print(reshaped)

#Convert a multidimensional array into a 1D arra
flattened = reshaped.flatten()
print(flattened)