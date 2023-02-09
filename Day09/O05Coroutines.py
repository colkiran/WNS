def get_name(surname):
    print(f"surname is {surname}")
    while True:
        name = yield
        print(f"recieved {name}")
        if surname in name:
            print("Surname matched....", name)

corou = get_name("pillai")
corou.__next__()

corou.send("Sachin Tendulkar")
print("-" * 40)

corou.send("virat kholi")
print("-" * 40)

corou.send("Rahul Dravid")
print("-" * 40)

corou.send("Dhanraj pillai")
print("-" * 40)