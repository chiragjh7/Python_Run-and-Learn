import numpy as np
dim_0 = np.array(4)
dim_1 = np.array([1, 2, 3, 4, 5])
dim_2 = np.array([[1, 2, 3], [4, 5, 6]])
dim_3 = np.array([[[1, 2, 3], [4, 5, 6], [1,2 ,3], [4, 5, 6]]])
print(dim_0)
print(dim_1)
print(dim_2)
print(dim_3)
print(dim_0.ndim);
print(dim_1.ndim);
print(dim_2.ndim);
print(dim_3.ndim);

# Higher Dimensions
arr = np.array([1, 2, 3, 4, 5], ndmin=5)
print(arr)
print("Number of dimensions: ", arr.ndim);