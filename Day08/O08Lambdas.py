
"""
anonymous function with a single expression

lambda var1, var2, var3...: expression
result of the expression will be the return value
"""

def add(x, y):
    return x + y
a = add

print(a(10,20))

print("-" * 40)

b = lambda x, y: x + y
print(b(100, 200))

print((lambda x, y: x + y) (10, 20))


# lambda  - map, filter, reduce

print("map".center(40, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

squares = list(map(lambda x: x ** 2, l1))
print(f"squares :{squares}")

print("-" * 40)

months = ['oct', 'apr', 'aug', 'dec', 'jul', 'feb', 'sep', 'nov', 'mar', 'jan', 'may', 'jun']

print(f"months :{months}")

# sort this list
from calendar import month_name
res_asc = sorted(months, key= list(map(lambda month: month[0:3].lower(), list(month_name))).index)

print(f"Sorted in Ascending :{res_asc}")

print("filter".center(40, "-"))
l2 = list(range(1, 25))
print(f"l2 :{l2}")

res = list(filter(lambda x : x % 3 == 0, l2))
print(f"res :{res}")

print("reduce".center(40, "-"))
from functools import reduce

l1 = [8, 5, 2, 9, 1, 10, 6, 3, 7, 4]

res = reduce(lambda x, y: x if x > y else y, l1)
print(f"res :{res}")

res = reduce(lambda x, y: x + y, l1)
print(f"res :{res}")
