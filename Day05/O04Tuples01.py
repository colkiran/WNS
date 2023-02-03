
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 40)
t2 = (1, 2, 3, 4, 'five')
print(f"t2 :{t2}")
print(type(t2))

print("-" * 40)
t3 = tuple(range(1, 6))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 40)
t4 = 1,
print(f"t4 :{t4}")
print(type(t4))

print("-" * 40)
t5 = 1, 2, 3, 4, 5
print(f"t5 :{t5}")
print(type(t5))

t1 = tuple(range(1, 6))
print(f"t1 .{t1}")

lst1 = list(t1)
print(f"lst1 :{lst1}")
print(type(lst1))
lst1.extend([6, 7, 8, 9, 10])
print(f"lst1 :{lst1}")
t1 = tuple(lst1)
print(f"t1 :{t1}")
print(type(t1))

print("-" * 40)
# print(dir(t1))

# count
t2 = (1, 2, 3, 1, 2, 3, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 2 ,1)
print(f"t2 :{t2}")
print(f"1 :{t2.count(1)}")
print(f"2 :{t2.count(2)}")
print(f"3 :{t2.count(3)}")

print("-" * 40)
# index
print("3 :", t2.index(3))
print("3 :", t2.index(3, t2.index(3)+1))
print("3 :", t2.index(3, t2.index(3, t2.index(3)+1)+1))

print("-" * 40)
t1= (1, 2, 3, 4, 5)
print(t1[3])
# t1[3] = 44