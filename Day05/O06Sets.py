
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 40)
s2 = {1, 'one', 'two', 3, 'four', 5, 'six', 7, 8.5, 9.0, 10.6, 11 + 0j, True, False}
print(F"s2 :{s2}")
print(type(s2))

print("-" * 40)
s1 = {1, 2, 3}
print(f"s1 :{s1}")
s1.add(1)
s1.add(4)
s1.add(2)
s1.add(3)
s1.add(5)
print(f"s1 :{s1}")
s1.update([1, 2, 3])
s1.update([6, 7, 8])
s1.update([5, 6, 7])
s1.update([8, 9, 10])
print(f's1 :{s1}')

# print(dir(s1))
# pop
res = s1.pop()
print(f"res :{res}")

res = s1.pop()
print(f"res :{res}")

print(f"s1 :{s1}")

# remove
s1.remove(8)
s1.remove(5)
print(f"s1 :{s1}")
# s1.remove(1)

# discard
s1.discard(4)
s1.discard(10)
print(f"s1 :{s1}")
s1.discard(1)

print("-" * 40)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 40)
print(f"A Union B :{A | B}")
print(f"B Union A :{B.union(A)}")

print("-" * 40)
print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print("-" * 40)
print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print("-" * 40)
print(f"A symmetricdifference B :{A ^ B}")
print(f"B Symmetricdifference A :{B.symmetric_difference(A)}")



# Frozensets - they are immutable
A = frozenset([1, 2, 3, 4, 5])
print(f"A :{A}")
print(type(A))
