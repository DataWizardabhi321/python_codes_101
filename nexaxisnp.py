import numpy as  np
arr = np.arange(5*5).reshape(5,5)
#promoting  a  2d array  to  5d  array 
arr_5d = arr[np.newaxis, ...,np.newaxis, np.newaxis]
print(arr_5d.shape)