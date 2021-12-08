import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.where(arr1 % 2 == 0)
print(y)

arr2 = np.array([6, 7, 8, 9])
# z = np.searchsorted(arr2, 7);
z = np.searchsorted(arr2, 7, side='right');
print(z)

arr3 = np.array([1, 3, 5, 7])
e = np.searchsorted(arr3, [2 ,4, 6])
print(e)