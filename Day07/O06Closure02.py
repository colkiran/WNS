
def outerFun(info):         # HOF - Higher Order Function
    inf = "Mr." + info

    def innerFun():
        print(inf)

    return innerFun

infun = outerFun("Sachin")
print("hello world")
print("hello world")
print("hello world")
infun()

print("-" * 40)
outerFun("Sachin")()        # calls innerFun()

print("-" * 40)
print(outerFun.__name__)
print(outerFun("Rahul").__name__)
