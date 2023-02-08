
class MyNumbers:

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = self.max[3]
        return self

    def __next__(self):
        if self.n <= self.max:
            res =self.max[3]
            self.n += 2
            return res
        else:
            raise StopIteration


myObj = MyNumbers([[1, 2, 3], [4, 5, 6], [7, 8, 9]])



"""
myObj = MyNumbers(10)
iterObj = iter(myObj)

print(next(iterObj))
print(next(iterObj))
print(next(iterObj))
print(next(iterObj))
print(next(iterObj))
# print(next(iterObj))

print("-" * 40)
for i in myObj:
    print(i)

"""