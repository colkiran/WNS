
class Player:

    def __init__(self):             # constructor
        print("Player initialized......")

    def get_runs(self):
        print('runs scored.....')

sachin = Player()
sourav = Player()
sachin.__init__()

print("-" * 40)
sachin.get_runs()
sourav.get_runs()
