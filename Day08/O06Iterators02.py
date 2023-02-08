
letters = ['a', 'b', 'c', 'd', 'e']
iterObj = letters.__iter__()

while True:
    try:
        elem = next(iterObj)
        print(elem, end=" ")
    except StopIteration:
        break

print()
print("-" * 40)

st = "Hello World"
for x in st:
    print(x, end=" ")
print()

