
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C++', 'Dotnet', 'AngularJS', 'ReactJS', "NodeJS"]

    def __str__(self):
        return "{} and {}".format(self.name, self.salary)

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)

emp1 = Employee("Ben", 35000)
print(len(emp1))

print([e for e in emp1])
