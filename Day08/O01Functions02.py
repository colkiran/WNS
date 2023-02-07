
# function return values

def mul_me(x):
    y = x * x
    return y

res = mul_me(5)
print(f"res : {res}")
print(mul_me(9))

# recursive calls

# find the factorial of a number
# print the fibanocci series for a given number

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

# num = int(input("Enter a number to find its factorial :"))
# print(f"The factorial of {num} is :{fact(num)}")

print("-" * 40)

def fib_recursion(n):
    if n <= 1:
        return n
    else :
        return fib_recursion(n-1) + fib_recursion(n-2)

# num = int(input("Enter the number of iterations :"))
# for i in range(num+1):
#     print(fib_recursion(i), end=" ")
print()

print("-" * 40)

def ArithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = ArithCalc(20, 8)
print(f"res :{res}")
print(type(res))

print("-" * 40)
# document a function using doc string

def fun1():
    "This is a simple function"
    print('Hello')

fun1()
print(fun1.__doc__)

print("-" * 40)

def fun2():
    # this is a comment
    "This is a document string"
    print("Hello")

fun2()
print(fun2.__doc__)

print("-" * 40)

def fun3(x, y):
    """
    function is fun3(x, y)
    ----------------------

    1. function fun3 takes two arguments
    2. if the arguments are of type numbers then it will the numbers and return
    3. if the arguments are of type string then it will concatenate the string and return it
    4. if one argument is number and the other argument is a string then it raises an exception
    """
    return x + y

res1 = fun3(10, 30)
print(f"res1 :{res1}")

res2 = fun3("hello ", "World")
print(f"res2 :{res2}")

# res3 = fun3(10, 'hello')
# print(f"res3 :{res3}")

print("-" * 40)
help(fun3)
