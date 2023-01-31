
player_count = 11
print(type(player_count))               # rtti - runtime type identification
print(f"player_count :{player_count}")  # interpolation

print("-" * 40)
team_rating = 4.6
print(type(team_rating))
print(f"team_rating :{team_rating}")

print("-" * 40)
team_name = "India"
print(type(team_name))
print(f"team_name :{team_name}")

print("-" * 40)
has_won_WC = True
print(type(has_won_WC))
print(f"Has won world cup :{has_won_WC}")

print("-" * 40)
player_count = "Eleven"
print(type(player_count))               # rtti - runtime type identification
print(f"player_count :{player_count}")  # interpolation

print("-" * 40)
print(f"__name__ :{__name__}")      # name of the current section of code

# double underscore name => dunder_name

print("-" * 40)
a, b, c = 1, 2, 3
print(a, b, c)

a = b = c = 180
print(a, b, c)

print("-" * 40)
fname = "Sachin"
lname = "Tendulkar"

print("My name is " + fname + " and I am also known as " + lname)

# interpolation
print(f"My name is {fname} and I am aslo known as {lname}")

print(f"{fname}'s total score in this series is {45 + 120 + 70}")
print(f"{fname}'s average in this series is {round((45 + 120 + 70) / 3, 0)}")

print("-" * 40)
team_name = 'Sahara India'
print(team_name)

team_name = "Sahara's India"
print(team_name)

team_name = 'Sahara\'s India'
print(team_name)
