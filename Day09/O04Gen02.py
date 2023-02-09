
def fun():
   x = 1
   print("Apple")
   yield x
   x += 9
   print("Orange")
   yield x
   x += 10
   print("Grapes")
   yield x

# print(fun())
res = fun()
print(res)
print(type(res))

print("-" * 40)
print(res.__next__())

print("-" * 40)
print(res.__next__())

print("-" * 40)
print(res.__next__())

# print(next(res))

def get_val():
    for i in range(1, 11):
        yield i

res1 = get_val()
print(next(res1))
print(next(res1))
print(next(res1))
print(next(res1))

for num in get_val():
   print(num, end=" ")
print()