
class Product:

    def __init__(self):
        # self.__price = price
        print("hello....")

    @property
    def price(self):
        print("Getter called............")
        return self.__price

    @price.setter
    def price(self, val):
        print(f"Setter called.............{val}")
        self.__price = val

    @price.deleter
    def price(self):
        print("Deleter called..............")
        self.__price = 0

coke = Product()

# print(coke.price)

coke.price = 100
print(coke.price)

del coke.price
print(coke.price)