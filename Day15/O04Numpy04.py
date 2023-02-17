
import numpy as np

arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("arr1 :\n", arr1)

print("-" * 40)
arr2 = arr1 + 1
print("arr2 :\n", arr2)

print("-" * 40)
arr3 = arr1 - 1
print("arr3 :\n", arr3)

print("-" * 40)
arr4 = arr1 * 5
print("arr4 :\n", arr4)

print("-" * 40)
arr5 = arr1 ** 2
print("arr5 :\n", arr5)

print("-" * 40)
arr1 *= 2
print("arr1 :\n", arr1)

print("-" * 40)
arr6 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])

print("arr6 :\n", arr6)
print("Transpose :\n",  arr6.T)

print("-" * 40)

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[4, 5],
              [6, 7]])

print("a :\n", a)
print("b :\n", b)

print("-" * 40)
print("Adding two arrays :\n", a + b)

print("-" * 40)
print("Subtracting two arrays :\n", a - b)

print("-" * 40)
print("Multiplying two arrays :\n", a * b)

print("-" * 40)
print("Dividing two arrays :\n", a / b)

print("-" * 40)
print("a :\n", a)
print("b :\n", b)

print("-" * 40)
print("Multiply the matrix :\n", a.dot(b))

# print("-" * 40)
#
# print("a :\n", a)
# b = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])
#
# print("b :\n", b)
#
# print(a * b)
