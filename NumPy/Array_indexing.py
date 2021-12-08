import numpy as np
arr = np.array([1, 2, 3, 4, 5]);
print(arr[0])
print(arr[2] + arr[3], "\n")

arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8 ,9, 10]])
print("2nd element on 1st row: ", arr1[0, 1])

arr2 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]])
print(arr2[0, 1, 2])

arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Last element from 2nd dim: ", arr3[1,-1])
