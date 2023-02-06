
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'Sachin'), ('age', 32), ('runs', 140), ('oppn', 'Aus'), ('Venue', 'Perth')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(player='Sachin', age=34, runs=85, oppn='SA', venue="Dublin")
print (f"d4 :{d4}")
print(type(d4))

print("-" * 40)
player = {'name': 'Sachin', 'age': 34, 'runs': 132, 'oppn': 'England', 'venue': 'Lords'}
print(f"player:{player}")

player['age'] = 32
player['runs'] = 150
player['year'] = 2001
player['team'] = 'Sahara India'
print(f"Player :{player}")

print("-" * 40)
for a in player:                # extract all the keys
    print(a , "=>" ,player[a])

print("-" * 40)
# del player['year']
player['year'] = ""
del player['venue']

print(f"player :{player}")


print("-" * 40)
d2 = {3: 'c', 5: 'e', 1:'a', 2:'b', 4:'d'}
print(f"d2 :{d2}")
l = []
for a in d2:
    l.append(int(a))
l.sort()
print(f"l :{l}")

for i in l:
    print(i, "=>", d2[i])

print("-" * 40)
player = {'name': 'Sachin', 'age': 34, 'runs': [132, 10, 65, 89, 5], 'oppn': 'England', 'venue': 'Lords'}
print(f"player:{player}")

print(f"Runs :{player['runs']}")

# del player['runs']
player['runs'].clear()

print(f"Player :{player}")

# print("-" * 40)
# print(dir(player))
