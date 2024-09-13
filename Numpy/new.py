import numpy
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
# a = np.array([1, 2, 3],dtype='int16')
print(a)
# print("Dimension of A:",a.ndim)
# print("Size of A:",a.shape)
# print("Dataype is:",a.dtype)
# print("Item Size:",a.itemsize)
# print("Total Size:",a.nbytes)
b = np.array([[7,8,9],[5,6,7],[8,9,6]])
print(b)
# print("Dimension of B:",b.ndim)
# print("Size of B:",b.shape)
# print("Dataype is:",b.dtype)
# print("Item Size:",b.itemsize)
print(np.matmul(a,b))
