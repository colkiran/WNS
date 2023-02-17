
import numpy as np

x = np.array([[1, 2],
              [3, 4]])

y = np.array([[5, 6],
              [7, 8]])

print("x :\n", x)
print("y :\n", y)

print("-" * 40)
print("Vertical Stacking :\n",  np.vstack((x, y)))

print("-" * 40)
print("Horizontal Stacking :\n",  np.hstack((x, y)))

print("-" * 40)
print("Concatenating :\n", np.concatenate((x, y)))

print("-" * 40)

z = np.array([[1, 3, 5, 7, 9, 11],
              [2, 4, 6, 8, 10, 12]])

print("z :\n", z)

print("-" * 40)
print("H-split :\n", np.hsplit(z, 3))

print("-" * 40)
print("V-split :\n", np.vsplit(z, 2))


'''
# z = np.copy(x)                # deep copy
z = x                           # shallow copy
print("z :\n",z)

z *= 2
print("z After :\n",z)
print("x After :\n",x)

'''