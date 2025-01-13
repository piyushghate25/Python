import numpy as np 

arr = np.array([[3, 2, 1], [6, 5, 4]])

# Sort each row
sorted_arr = np.sort(arr, axis=1)
print(sorted_arr)
