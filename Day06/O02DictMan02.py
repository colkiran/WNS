
player = {'name': 'Rahul', 'runs': 70, 'age': 31, 'oppn': 'Nzl', 'venue':'Auckland'}
print(f"Player :{player}")

print("-" * 40)
# print(player['year'])
# get

print("Year :", player.get('year', "Invalid Key, Please enter a valid one"))
print("Runs :", player.get('runs', "Invalid Key, Please enter a valid one"))

print("setdefault".center(40, "-"))
# adds only a new key value pair into the dictionary

player = {'name': 'Rahul', 'runs': 70, 'age': 31, 'oppn': 'Nzl', 'venue':'Auckland'}
print(f"Player :{player}")

player.setdefault("runs", 0)
player.setdefault('year', 2005)

print(f"player :{player}")

print("fromkeys".center(40, "-"))

cities = ['blr', 'che', 'del', 'mum', 'kol', 'hyd']

temp1 = dict.fromkeys(cities)
print(f"temp1 :{temp1}")

temp2 = dict.fromkeys(cities, 24)
print(f"temp2 :{temp2}")

print("-" * 40)

player = {'name': 'Rahul', 'runs': 70, 'age': 31, 'oppn': 'Nzl', 'venue':'Auckland'}
print(f"Player :{player}")

k = player.keys()
print(f"k :{k}")
print()

for k in player.keys():
    print(k + "=>" + str(player[k]))

print('values'.center(40, "-"))
player = {'name': 'Rahul', 'runs': 70, 'age': 31, 'oppn': 'Nzl', 'venue':'Auckland'}
print(f"Player :{player}")

v = player.values()
print(f"v :{v}")

print("pop".center(40, "-"))

player = {'name': 'Rahul', 'runs': 70, 'age': 31, 'oppn': 'Nzl', 'venue':'Auckland'}
print(f"Player :{player}")

res = player.pop('runs')
print(f"res :{res}")
print(f"player :{player}")

# res = player.pop('year')

