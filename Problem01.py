
from collections import namedtuple

def ArithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y

    nmdTpl = namedtuple("Arithcalc", "sum diff prod quot" )
    arth = nmdTpl(sum=sum, diff=diff, prod=prod, quot= quot)
    return arth

res = ArithCalc(20, 8)
print(f"res :{res}")