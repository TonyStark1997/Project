import numpy as np

a = np.arange(15).reshape(3,5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)

b = np.array([1,2,3,4,5])
print(b)

c = np.empty((2,3))
print(c)

d = a**2
print(d)

e = np.random.random((2,3))
print(e)
