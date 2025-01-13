import numpy as np

arr = np.array([1, 2, 2, 3, 4, 4, 5])

# Unique values
unique_vals = np.unique(arr)
print(unique_vals)  # Output: [1 2 3 4 5]

# Filtering
filtered = arr[arr > 2]
print(filtered)  # Output: [3 4 4 5]
