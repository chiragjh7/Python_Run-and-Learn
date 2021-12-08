import numpy as np
arr = np.array([1, 2, 3, 4, 5])

# Does'nt changes the array 
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

# changes the array
x = arr.view()
arr[0] = 42
print(arr)
print(x)

