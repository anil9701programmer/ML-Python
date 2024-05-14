import numpy as np

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [1, 2, 3, 4, 5, 6, 7]

np_array = np.asarray(list1)
print(np_array)
a = np.asarray(list1)
b = np.asarray(list2)

print(a + b)
print(a.shape)
print(a.size)
print(a.ndim)

x = np.array([(1, 2, 3, 4), (5, 6, 7, 8)])
print(x)


y = np.random.random([3, 3])
print(y)

z = np.random.randint(10, 100, [3, 3])
print(z)