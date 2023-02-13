
class Animal:

    def __init__(self):
        print("Animal Ctor..........")
        self.age = 1

    def eat(self):
        print("Animals eat..........")

class Bird(Animal):

    def __init__(self):             # overriding the parent class constructor
        super().__init__()
        self.weight = '1.08 kgs'
        print("Bird Ctor.......")

    def fly(self):
        print("Birds fly......")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-"  * 40)
print(cuckoo.__dict__)

