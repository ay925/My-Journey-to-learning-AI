import numpy as np
arr2d=np.array([[1,2,3],
       [4,5,6]])
newarr2d=np.insert(arr2d,1,[2,3,4],axis=0)
print(newarr2d)