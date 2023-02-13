
class Animal:
    def __init__(self):
        print("Animal Ctor.............")
        self._name = "Tiger"            # protected
        self.__age = "5 yrs"            # private

    def get_details(self):
        print(f"Name is {self._name}\nAge is {self.__age}")

class Bird(Animal):

    def get_details(self):
        print(f"Name is {self._name}")

cuckoo = Bird()
cuckoo.get_details()