
class Animal:
    def  __init__(self):
        print("Animal Ctor......")
        self.a = 1

    def eat(self):
        print("Animals eat......")

class Bird(Animal):

    def __init__(self):
        super().__init__()
        print("Bird Ctor......")
        self.b = 2

    def fly(self):
        print("Birds Fly......")

class Chicken(Bird):
    def __init__(self):
        super().__init__()
        print("Chicken Ctor..........")
        self.c  = 3

    def Cfly(self):
        print("Chickens seldom fly.....")

c = Chicken()
c.eat()
c.fly()
c.Cfly()

print("-" * 40)
print(c.__dict__)
