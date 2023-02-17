
# indexing, slicing

import numpy as np

ar1 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])
print("ar1 :\n", ar1)

print("-" * 40)
ar2 = ar1[:2, :]
print("ar2 :\n", ar2)

print("-" * 40)
ar3 = ar2[:2, ::2]
print("ar3 :\n", ar3)

print("-" * 40)
ar4 = ar1[1, 1:4]
print("ar4 :\n", ar4)

print("-" * 40)
ar5 = ar1[0:2, 2]
print("ar5 :\n", ar5)

print("-" * 40)
ar6 = ar1[1:3, 1:4]
print("ar6 :\n", ar6)

print("-" * 40)
cond = ar1 % 2 == 1
ar8 = ar1[cond]
print("ar8 :\n", ar8)



