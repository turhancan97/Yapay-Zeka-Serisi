# importing
import numpy as np

# numpy basics
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])  # 1*15 vector
print(array.shape)
a = array.reshape(3,5)
print("shape: ",a.shape)
print("dimension: ", a.ndim)
print("data type: ",a.dtype.name)
print("size: ",a.size)
print("type: ",type(a))
array1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])
zeros = np.zeros((3,4))
zeros[0,0] = 5
print(zeros)
np.ones((3,4))
np.empty((2,3))
a = np.arange(10,50,5)
print(a)
a = np.linspace(10,50,20)
print(a)

# %% numpy basic operations

a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)
print(a-b)
print(a**2)
print(np.sin(a))
print(a<2)

# element wise prodcut
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])
print(a*b)

# matrix prodcut
a.dot(b.T)
print(np.exp(a))
a = np.random.random((5,5))
print(a.sum())
print(a.max())
print(a.min())
print(a.sum(axis=0)) # sütunları toplar
print(a.sum(axis=1)) # Satırları toplar
print(np.sqrt(a))
print(np.square(a)) # a**2
print(np.add(a,a))

# %% indexing and slicing

import numpy as np
array = np.array([1,2,3,4,5,6,7])   #  vector dimension = 1
print(array[0])
print(array[0:4])
reverse_array = array[::-1]
print(reverse_array)
array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1[1,1])
print(array1[:,1])
print(array1[1,1:4])
print(array1[-1,:])
print(array1[:,-1])

# %%

# shape manipulation
array = np.array([[1,2,3],[4,5,6],[7,8,9]])

# flatten
a = array.ravel()
array2 = a.reshape(3,3) #resize metodu kalıcı değişiklik yapar. reshape komutu kalıcı değildir. ama yaptıkları şey aynıdır.
arrayT = array2.T
print(arrayT.shape)
array5 = np.array([[1,2],[3,4],[4,5]])
#array5 = np.column_stack((array1,array1))

# %% stacking arrays

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])
# veritical
#array([[1, 2],
#       [3, 4]])
#array([[-1, -2],
#       [-3, -4]])
array3 = np.vstack((array1,array2))
# horizontal
#array([[1, 2],[-1, -2],
#       [3, 4]],[-3, -4]]
array4 = np.hstack((array1,array2))

#%% convert and copy

liste = [1,2,3,4]   # list
array = np.array(liste) #np.array
liste2 = list(array)
a = np.array([1,2,3])
b = a
b[0] = 5
c = a
d =  np.array([1,2,3])
e = d.copy() #.copy() metodu yeni alan sağlar ve yeni değişkenimiz eskisinden hafızada tamamen farklı alanda bulunur.
f = d.copy()