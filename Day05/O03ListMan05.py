
values = list(range(10, 31, 10))
print(f"values :{values}")

# unpack the list
a, b, c = values
print(a, b, c, sep=", ")

print("-" * 40)
values = list(range(10, 101, 10))
print(f"values :{values}")

a, b, *c = values            # can accept more than one value
print(a, b, c, sep=", ")
print("-" * 40)

a, *b, c = values
print(a, b, c, sep=", ")
print("-" * 40)

*a, b, c = values
print(a, b, c, sep=", ")
print("-" * 40)

lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

lst3 = [lst1, lst2]
print(len(lst3))
print(f"lst3 :{lst3}")
print("-" * 40)

lst4 = [*lst1, *lst2]
print(len(lst4))
print(f"lst4 :{lst4}")

print("-" * 40)
letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

print("-" * 40)
for letter in letters:
    print(letter, end= " ")
print()

print("-" * 40)
for letter in enumerate(letters):
    print(letter, end=" ")
print()

print("-" * 40)
for letter in enumerate(letters):
    print(letter[0], letter[1])

print("-" * 40)
for index, letter in enumerate(letters):
    print(index, letter)

print("-" * 40)
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"mylist :{mylist}")

print("-" * 40)
for lst in mylist:
    print(lst)

print("-" * 40)
for ind, lst in enumerate(mylist):
    print(ind, lst)

print("-" * 40)
for ind, lst in enumerate(mylist):
    print(f"List({ind})")
    for idx, num in enumerate(lst):
        print(f"\t{idx}\t{num}")

print("-" * 40)
import numpy as np
from sys import getsizeof

lst1 = list(range(1, 1000))
lst2 = np.array(range(1, 1000))

print(f"lst1 :{getsizeof(lst1)}")
print(f"lst2 :{getsizeof(lst2)}")
