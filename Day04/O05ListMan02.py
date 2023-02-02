
# remove elements from the list = pop, remove

print("{:-^40}".format("pop"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(7)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop(-2)
print(f"res :{res}")
print(f"l1 :{l1}")

print("Remove".center(40, "-"))
l1 = [1, 2, 3, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1 ,1, 1, 1, 1 ,1, 1, 1]

print(f"l1 :{l1}")

l1.remove(1)
print(f"l1 :{l1}")

l1.remove(3)
print(f"l1 :{l1}")

while l1.count(1):
    l1.remove(1)

print(f"l1 :{l1}")
