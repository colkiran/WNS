
class Player:

    def __init__(self):         # Constructor
        self.name = "Sachin"
        self.age = 30
        print("Player Initialized.......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    def __del__(self):
        print(f"Deleting {self.name}.....")


ply1 = Player()
ply1.get_details()

print("-" * 40)
ply2 = Player()
ply2.name = "Rahul"
ply2.age = 29
ply2.get_details()

print("-" * 40)
del ply1

print("-" * 40)
print(ply2.get_details())
print("Hello World \n" * 3)