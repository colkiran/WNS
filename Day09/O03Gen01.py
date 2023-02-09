
print(sum([x ** 2 for x in range(11)]))          # comprehension
print(sum((x ** 2 for x in range(11))))          # generator

from sys import getsizeof
val1 = [x ** 2 for x in range(10000)]
print("comprehension size of list :", getsizeof(val1))

val2 = (x ** 2 for x in range(10000))
print("generator size of list     :", getsizeof(val2))

val3 = (x  for x in range(10))
for num in val3:
    print(num, end=" ")
print()
