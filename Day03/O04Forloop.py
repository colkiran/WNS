
for i in range(10):
    print(i, end=" ")
print()                 # prints a new line (end="\n")

print("-" * 40)

for i in range(1, 10):
    print(i, end=" ")
print()

print("-" * 40)

for i in range(1, 11, 2):
    print(i, end=" ")
print()

print("-" * 40)

for i in range(2, 11, 2):
    print(i, end=" ")
print()

print("-" * 40)

for i in range(10, 0, -1):
    print(i, end=" ")
print()

print("-" * 40)
# continue, break, else

for i in range(1, 26):
    # if i > 20:
    #     break
    if i % 2 == 0:
        continue
    print(i, end= " ")
else:
    print("\ncompleted the iteration")
# print()

