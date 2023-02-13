
class Animal:

    def __init__(self):
        self.a = 10
        print("Animal Ctor......")

    def eat(self):
        print("Animals eat.......")

    def fun(self):
        print(f"Function fun of Animal Class :{__class__.__name__}")

class Person:

    def __init__(self):
        self.p  = 20
        print("Person Ctor.......")

    def talk(self):
        print("Person talks..........")

    def fun(self):
        print(f"Function fun of Person Class :{__class__.__name__}")

class Girl(Person, Animal):
    def __init__(self):
        super().__init__()                  # calls the parent class
        Animal.__init__(self)
        self.g = 30
        print("Girl Ctor......")


print("-" * 40)
tanya = Girl()
tanya.eat()
tanya.talk()
tanya.fun()

print("-" * 40)
print(tanya.__dict__)
