
class Employee:

    def __init__(self, name):
        self.__name = name          # Private Variable
        self.tech = ['C++', 'Dotnet', 'AngularJS', 'ReactJS', "NodeJS"]

    def __str__(self):
        return self.__name + " - " + ", ".join([str(v) for v in self.tech])

emp1 = Employee("Smith")
print(emp1)

print("-" * 40)
# print(emp1.__name)
# print(emp1.__dict__)
emp1._Employee__name  = "Anderson"          # expando
print(emp1)

print("-" * 40)
print(emp1.__dict__)
