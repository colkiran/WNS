
from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self):
        print("Account.....")

    @abstractmethod
    def getBalance(self):
        pass

class Savings(Account):

    def deposit_Amt(self):
        print("Amount deposited successfully.....")

    def getBalance(self):
        print("The balance in the account ending #### is ######.##")

class Current(Account):

    def getBalance(self):
        print("The balance in the account ending #### is ######.##")

sav = Savings()
sav.deposit_Amt()
sav.getBalance()

print("-" * 40)
cur = Current()
cur.getBalance()
