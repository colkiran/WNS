
from collections import namedtuple

nmdTpl = namedtuple("Student", "name cls age gender")
stud = nmdTpl(name="Micheal", cls="Xth", age=15, gender="Male")

print("-" * 40)
print(f"stud   :{stud}")
print(f"Name   :{stud.name}")
print(f"Class  :{stud.cls}")
print(f"Age    :{stud.age}")
print(f"Gender :{stud.gender}")

# stud.name = "George"
