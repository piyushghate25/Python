import numpy as np

a  = np.array([[1,2,3],[4,5,6]])

print(np.sum(a)) #sum of all numbers
print(np.sum(a,axis= 0) ) # sum along columns indirectly sum of columns
print(np.sum(a , axis =1)) # sum along rows 
