
class Player:

    team = "India"      # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Initialized.......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 35)
ply1.get_details()

print("-" * 40)
ply2 = Player("Sourav", 34)
ply2.get_details()

print("-" * 40)
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

print("-" * 40)
Player.team = "Mumbai Indians"
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

print("-" * 40)
ply2.team = 'Kolkota Knight Riders'
print(f"ply2   :{ply2.team}")
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")

print("-" * 40)
print("ply1 :", ply1.__dict__)
print("ply2 :", ply2.__dict__)

print("-" * 40)
print("player", Player.__dict__)