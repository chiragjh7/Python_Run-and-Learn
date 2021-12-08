import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
# print(newarr)

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr1 = arr1.reshape(2, 3, 2)
print(newarr1)

# flattening the arrays
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
newarr2 = arr2.reshape(-1)
print(newarr2)