import numpy as np
# a=np.array([[1,2,3],[4,5,6]])
# b=np.array([[2,2],[4,4],[6,6]])
a=np.ones((2,3),dtype='int16')
b=np.full((3,2),2)
c=np.identity(3)
# c=np.array([[8,-8,2],[4,-3,-2],[3,-4,1]],dtype='int16')
print(np.matmul(a,b))
print(np.linalg.det(c))#determinant
print(np.linalg.eig(c))
