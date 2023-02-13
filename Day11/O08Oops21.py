
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Manager's Job......")

class Deverloper(Employee):

    def doJob(self):
        print("Developers Job......")

def BankJob(emp):       # polymorphism
    print("Bank Job Started...........")
    emp.doJob()
    print("Bank Job Ended...........")
    print("-" * 40)

Mike = Manager()
David = Deverloper()

BankJob(Mike)
BankJob(David)
print("=" * 40)

def BankJobs(emps):       # polymorphism
    print("Bank Job Started...........")
    for emp in emps:
        emp.doJob()
    print("Bank Job Ended...........")
    print("-" * 40)

BankJobs([Mike, David])
