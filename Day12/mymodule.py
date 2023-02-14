
gname = "Sourav Ganguly"

sports = ['cricket', 'football', 'hockey', 'basketball', 'tennis', 'badmiton', 'swimming']

runs = {'test': 12400, 'ODI': 14230, 'T20': 1200}

def greet(gnm):
    print(f"Greeting Mr.{gnm}, Welcome the event.......")

class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"The name is {self.name}\nAge is {self.age}")

print("-" * 40)
print(__name__)

if __name__ == '__main__':
    ply1 = Player('Messi', 35)
    ply1.get_details()
