
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.0, 8.2, 9.5, 10+0j, 11+3j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(1, 11))
print(f'l3 :{l3}')
print(type(l3))

print("-" * 40)
# memory allocation
l4 = [1, 2, 3, 'four', 'five', 'six', 7.0, 8.2, 9.5, 10+0j, 11+3j, True, False]
print(f"l4 :{l4}")

# address - id()
print(f"id(l4[0]) :{id(l4[0])}")
print(f"id(l4[1]) :{id(l4[1])}")
print(f"id(l4[2]) :{id(l4[2])}")
print(f"id(l4[3]) :{id(l4[3])}")

print("-" * 40)
# print(dir(l1))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")
l1[3] = 3.5
print(f"l1 :{l1}")

# add new values into a list - append, extend, insert

print("append".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")
l1.append(6)
l1.append('seven')
l1.append('eight')
print(f"l1 :{l1}")

l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")
print(f"l1[8][1:4] :{l1[8][1:4]}")

print("extend".center(40, "-"))
l2 = ['a', 'b', 'c', 'd', 'e']
print(f"l2 :{l2}")

l2.extend(['f', 'g', 'h'])
l2.extend(['i', 'j', 'k'])

print(f"l2 :{l2}")

print("insert".center(40, "-"))
l3 = [1, 2, 3, 4, 5]
print(f"l3 :{l3}")
print(type(l3))

l3.insert(1, 1.5)
l3.insert(3, 2.5)
l3.insert(5, 3.5)
l3.insert(7, 4.5)
print(f"l3 :{l3}")

l3.insert(19, [6, 7, 8, 9])
print(f"l3 :{l3}")
