"""
.ravel()->view
.flatten()->copy

"""
import numpy as np
arr2d=np.array([[1,2,3],
       [4,5,6]])
print(arr2d.ravel())
print(arr2d.flatten())