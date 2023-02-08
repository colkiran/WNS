
def outerFun(greet):

    def innerFun(name):
        print(greet, name)

    return innerFun

# curry
outerFun("Welcome")("Sachin")
tamilGrt = outerFun("Vanakam")
hindiGrt = outerFun("Namaskar")

# Dish - simplecurry
tamilGrt("Natraj")
hindiGrt("Sachin")
hindiGrt("Rahul")
hindiGrt("Zaheer")

