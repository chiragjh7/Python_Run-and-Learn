import numpy as np
arr = np.array([1, 2, 3])
for x in arr:
    print(x)

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr1:
    print(x)
for x in arr1:
    for y in x:
        print(y)    

#nditer
arr2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr2):
    print(x)        

arr3 = np.array([1, 2, 3])
for x in np.nditer(arr3, flags=['buffered'], op_dtypes=['S']):
    print(x)
#Iterating with different steps
for x in np.nditer(arr2[:,::2]):
    print(x)

for idx, x in np.ndenumerate(arr3):
    print(idx, x)
for idx, x in np.ndenumerate(arr2):
    print(idx, x)            