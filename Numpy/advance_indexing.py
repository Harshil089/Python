import numpy as np
filedata=np.genfromtxt('data.txt',delimiter=',').astype('int32')
# print(filedata)
print(np.any(filedata > 50,axis=0))
a=np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]])
