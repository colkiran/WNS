
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

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, val):
        self.tech[index] = val

emp1 = Employee("Mark", 35000)

print([e for e in emp1])

emp1.append('Python')

print([e for e in emp1])

x = emp1[4]
print(f"x :{x}")

emp1[4] = "ExtJS"
print([e for e in emp1])
