

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return "{} and {}".format(self.name, self.salary)

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary


emp1 = Employee("David", 20000)
emp2 = Employee("John", 30000)

print(f"Add : {emp1 + emp2}")
print(f"Sub : {emp2 - emp1}")
print(f"Mul : {emp1 * emp2}")
print(f"Div : {emp1 / emp2}")
print(f"Floor :{emp2 // emp1}")