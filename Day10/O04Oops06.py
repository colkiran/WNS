
class Player:

    team = "India"      # class attribute

    def __init__(self, name, age):
        print("Ctor called........")
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def CreatePlayer(cls, fname, lname, DOB):
        print("Factory......")
        from datetime import datetime
        dyr = DOB.split("/")[-1]
        tyr = datetime.now().year
        age = tyr - int(dyr)
        return cls(f"{fname} {lname}",age)          # calls the Ctor

ply1 = Player("Virat", 33)
ply1.get_details()

print("-" * 40)
ply2 = Player.CreatePlayer("Rohit", "Sharma", "10/03/1988")
ply2.get_details()


