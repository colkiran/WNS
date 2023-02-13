
"""
1. class
2. object
3. isinstance
4. __init__
5. self
6. class attributes / variables
7. class method
8. cls
9. __str__, __eq__, __gt__, total ordering, __add__,....
10. private variables __var
11. __dict__
12. property(),  @property, setter, deleter
"""

class Animal:
    def __init__(self):
        print('Animal Ctor......')
        self.age = 1

    def eat(self):
        print("Animals eat......")

class Bird(Animal):

    def fly(self):
        print("Birds fly.....")

class Fish(Animal):

    def swim(self):
        print("Fishes swim.......")

cuckoo = Bird()
cuckoo.fly()
cuckoo.eat()

print("-" * 40)
dolphin  = Fish()
dolphin.swim()
dolphin.eat()

print("-" * 40)
print(cuckoo.__dict__)
print(dolphin.__dict__)