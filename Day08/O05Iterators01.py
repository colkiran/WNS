
lst = [1, 2, 3, 4, 5]
print(f"lst :{lst}")
print(type(lst))

print("-" * 40)
iterObj = lst.__iter__()
# print(dir(iterObj))         # __iter__ and __next__
print(f"iterObj :{iterObj}")

v1 = iterObj.__next__()
print(f"v1 :{v1}")

v2 = iterObj.__next__()
print(f"v2 :{v2}")

v3 = iterObj.__next__()
print(f"v3 :{v3}")

v4 = iterObj.__next__()
print(f"v4 :{v4}")

v5 = iterObj.__next__()
print(f"v5 :{v5}")

# v6 = iterObj.__next__()
# print(f"v6 :{v6}")

print("-" * 40)
for i in lst:
    print(i, end=" ")
print()

