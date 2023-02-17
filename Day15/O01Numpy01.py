
from sys import getsizeof
import numpy as np

arr = list(range(1, 10000))

nparr = np.array(range(1, 10000))

print("Array       :", getsizeof(arr))
print("Numpy Array :", getsizeof(nparr))

print("-" * 40)

ar1 = np.array([1, 2, 3, 4, 5])

print(f"ar1 :{ar1}")
print(type(ar1))

print("-" * 40)
print("array dimension :",ar1.ndim)

print("array datatype  :", ar1.dtype)

print("array shape     :", ar1.shape)

print("Array size      :", ar1.size)

print("-" * 40)

ar2 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

print("ar2 \n", ar2)
print(type(ar2))

print("-" * 40)

print("array dimension :",ar2.ndim)

print("array datatype  :", ar2.dtype)

print("array shape     :", ar2.shape)

print("Array size      :", ar2.size)
