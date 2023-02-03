
print("count".center(40, "-"))
l1 = [1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2,2 ,2 ,2 ,2, 2, 2, 1, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2]

print(f"l1 :{l1}")
print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")
print(f"4 :{l1.count(4)}")

print("Index".center(40, "-"))
l1 = [1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2,2 ,2 ,2 ,2, 2, 2, 1, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2]

print(f"l1 :{l1}")
print("3 :", l1.index(3))
print("3 :", l1.index(3, l1.index(3) + 1))
print("3 :", l1.index(3, l1.index(3, l1.index(3) + 1)+1))

print("copy".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 Before :{l1}")
l2 = l1                 # shallow copy  - it copies the address along with data
print(f"l2 Before :{l2}")
l2.extend([6, 7, 8, 9])
print(f"l2 After :{l2}")
print(f"l1 After :{l1}")

print("=" * 40)
# copy
l3 = [6, 7, 8, 9, 10]
print(f"l3 Before :{l3}")
l4 = l3.copy()              # deep copy - copies only the data
print(f"L4 Before :{l4}")

l4.append(10)
l4.append(11)
l4.append(12)
l4.append(13)
print(f"l4 After :{l4}")
print(f"L3 After :{l3}")

print("=" * 40)
l5 = [10, 20, 30, 40, [1, 2, 3, 4, 5], 50]
print(f"l5 Before :{l5}")
l6 = l5.copy()
print(f"l6 Before :{l6}")

l6[4].extend([6, 7, 8, 9])
print(f"l6 After :{l6}")
print(f"l5 After :{l5}")

print("-" * 40)
from copy import deepcopy
l7 = [1, 2, 3, 4, [11, 22, 33, 44, 55], 5]
print(f"L7 Before :{l7}")
l8 = deepcopy(l7)
print(f"l8 Before :{l8}")

l8[4].extend([66, 77, 88])
print(f"l8 After :{l8}")
print(f"l7 After :{l7}")
