
class Player:                   # pascal casing

    def get_runs(self):
        print("run scored.....")
        print(self.__class__)


sachin = Player()

sachin.get_runs()
print(type(sachin))
print(sachin.__class__)

print("-" * 40)
print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))
