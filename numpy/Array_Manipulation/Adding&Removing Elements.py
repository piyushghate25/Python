import numpy as np

arr = np.array([1, 2, 3])
arr = np.append(arr, [4, 5])
print(arr)  # Output: [1 2 3 4 5]

arr = np.delete(arr, [0, 2])  # Delete indices 0 and 2
print(arr)  # Output: [2 4 5]

