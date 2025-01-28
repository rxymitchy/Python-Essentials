import numpy as np

a = np.array([1, 2, 3])
print(a)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

c = np.array([4, 5, 6])

# Addition
print(a + c)

# Suctraction
print(a - c)

# Multiplication
print(a * c)

# Division
print(a / c)

# Indexing
print(a[0])
print(a[-1])

# Slicing
print(a[1:4])

#Reshaping
d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# reshape to a 3 * 3 array
f = d.reshape((3, 3))
print(f)