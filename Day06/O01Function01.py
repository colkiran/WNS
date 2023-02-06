
def greet():
    print("Greeting Mr. Sachin Welcome to the event....")

def greetGst(gname):
    print(f"Greeting Mr. {gname}, Welcome to the event......")

# city is default arg and gname is nondefault arg
def greetGstCty(gname, city="Mumbai"):
    print(f"Greetings Mr. {gname} from {city}, Welcome to the event.......")

greet()

print("-" * 40)
greetGst("Sachin")
greetGst("Rahul")

print("-" * 40)
greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print("-" * 40)
def admsn(name, dob, qlf, marks, location, address, gender):
    print(f"name :{name}")
    print(f"DOB :{dob}")
    print(f"Qualification :{qlf}")
    print(f"Marks :{marks}")
    print(f"Location :{location}")
    print(f"address : {address}")
    print(f"gender :{gender}")

admsn(gender = "Male", marks = {'xth': '85%', 'xiith': '92%', 'degree': '79%'}, qlf='Btech', location='Hyd', name='Sachin', dob="12/19/1989", address="lakadi ka phool")

print("-" * 40)
# variable length arguments

def prodAll(*numbers):
    print(numbers)
    prod = 1
    for number in numbers:
        prod *= number
    return prod

res = prodAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 40)

def extracDetails(**details):
    print(details)
    for k, v in details.items():
        print(k, "=>", v)

extracDetails(name="Rahul", age=34, runs=135, oppn='SA', venue='Dublin')
