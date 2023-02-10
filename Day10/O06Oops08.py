
from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return "{} and {}".format(self.name, self.salary)

    # works for not equal to also
    def __eq__(self, other):
        return self.salary == other.salary

    # works for less than also
    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee("Kevin",45000)
print(emp1)

emp2 = Employee("Mike", 50000)
print(emp2)

print("-" * 40)

if (emp1 != emp2):
    print("{} salary of {} is NOT EQUAL to {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{} salary of {} is  EQUAL to {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))


print("-" * 40)
# print(emp1 > emp2)

if (emp1 < emp2):
    print("{} salary of {} is Greater Than {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{} salary of {} is Greater Than {} salary of {}".format(emp2.name, emp2.salary, emp1.name, emp1.salary))

print("-" * 40)
print(emp1 >= emp2)