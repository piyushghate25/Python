import numpy as np

d = np.array([1.234, 5.678, 9.876])

print(np.clip(d,2,8))

'''
The np.clip() function is used to limit the values in an array within a specified range.
Any value in the array that is less than the lower bound is set to the lower bound,
and any value greater than the upper bound is set to the upper bound.
'''