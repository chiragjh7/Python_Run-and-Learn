import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

# Join two 2-D array along rows(axis = 1)
arr2 = np.array([[1, 2], [3, 4]])
arr3 = np.array([[5, 6], [7, 8]])
arr4 = np.concatenate((arr2, arr3), axis = 1)
print(arr4)

arr5 = np.array([1, 2, 3])
arr6 = np.array([4, 5, 6])
arr7 = np.stack((arr5, arr6), axis = 1)
print(arr7)

# Stack along rows, columns, depths
# arr8 = np.hstack((arr5, arr6))
# arr8 = np.vstack((arr5, arr6))
arr8 = np.dstack((arr5, arr6))
print(arr8)