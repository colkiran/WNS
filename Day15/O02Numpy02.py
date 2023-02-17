
import numpy as np

ar1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
print("ar1 :\n", ar1)

print("-" * 40)
ar2 = np.array((10, 20, 30, 40, 50))
print("ar2 :\n", ar2)

print("-" * 40)
ar3 = np.zeros((3, 4), dtype=int)
print("ar3 :\n", ar3)

print("-" * 40)
ar4 = np.full((3, 3), 3, dtype=complex)
print("ar4 :\n", ar4)

print("-" * 40)
ar5 = np.random.random((4, 2))
print("ar5 :\n", ar5)

print("-" * 40)
ar6 = np.arange(0, 50, 5.0)           # range(0, 50, 5)
print('ar6 :\n', ar6)

print("-" * 40)
ar7 = np.linspace(0, 5, 10)
print('ar7 :\n', ar7)

print("-" * 40)
ar8 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("ar8 :\n", ar8)
print(ar8.shape)

ar9 = ar8.reshape(2, 2, 3)
print("ar9 :\n", ar9)

print("-" * 40)
ar10 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("ar10 :\n", ar10)

ar11 = ar10.flatten()
print("ar11 :\n", ar11)


'''
print("-" * 40)
class Player:
    pass

ply1 = Player()
ply2 = Player()
ply3 = Player()
ply4 = Player()
ply5 = Player()

print(isinstance(ply1, object))

objArr = np.array([ply1, ply2, ply3, ply4, ply5])
print("objArr :\n", objArr)
print(type(objArr))

 print(objArr.dtype)
'''