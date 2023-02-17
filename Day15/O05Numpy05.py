
import numpy as np

arr1 = np.array([[3, 1, 2],
                 [6, 5, 4],
                 [9, 7, 8]])
print("arr1 :\n", arr1)

print("-" * 40)
print("Array sorting elements :\n",  -np.sort(-arr1, axis=None))

print("-" * 40)
print("Array sorting row wise :\n", np.sort(arr1, axis=1))

print("-" * 40)
arr1 = np.array([[9, 7, 8],
                 [3, 1, 2],
                 [6, 5, 4]])
print("Array sorting column wise :\n", np.sort(arr1, axis=0, kind="mergesort"))

print("-" * 40)

dtypes = [('name', 'U10'), ('year_of_birth', int), ("avg_mrks", float)]

values = [('James', 1999, 8.5), ('Mary', 2003, 7.9), ('Steve', 2002, 9.3),
          ('Tina', 2002, 9.5), ('Bob', 2004, 8.9)]

stud = np.array(values, dtype=dtypes)
print("stud :\n", stud)

print("-" * 40)
# sort by name
print("Name :\n", np.sort(stud, order='name')[::-1])

print("-" * 40)
# sort by name
print("YOB :\n", np.sort(stud, order='year_of_birth'))

print("-" * 40)
# sort by name
print("Marks :\n", np.sort(stud, order='avg_mrks'))
