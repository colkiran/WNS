
# emulate c style

format = "Welcome %s, what a %s player"
print(f"format :{format}")
values = ("Sachin", "superb")           # tuples
print(f"values :{values}")
print(format % values)

print("Welcome %s, what a %s player" % ("Sachin", "superb"))
print("-" * 40)

format = "Welcome %s, your rating of %.3f, what a %s player"
print(format % ("Sachin", 4, "superb"))
print(format % ("Sachin", 4.8, "superb"))
print(format % ("Sachin", 4.82236423, "superb"))
print(format % ("Sachin", 4.89999999, "superb"))

# emulate unix shell syntax
print("unix style".center(40, "-"))
from string import Template
tmpl = Template("Welcome $name, what a $adj player")
print(tmpl)
print(tmpl.substitute(name = "Sachin", adj = "class"))

print("-" * 40)
# format string from python
print("Welcome {}, what a {} player for {}".format("Sachin", 'superb', "India"))

print("Welcome {0}, what a {1} player for {2}".format("Sachin", 'superb', "India"))

print("Welcome {0}, what a {1} player for {2}".format("India", "Sachin", 'superb'))

print("Welcome {1}, what a {2} player for {0}".format("India", "Sachin", 'superb'))

print("Welcome {pname}, what a {adj} player for {cntry}".format(cntry="India", pname="Sachin", adj='superb'))

print("Welcome {pname}, with a rating of {rating},  player for {cntry}".format(cntry="India", pname="Sachin", rating=4))

print("Welcome {pname}, with a rating of {rating:.3f},  player for {cntry}".format(cntry="India", pname="Sachin", rating=4))

print("Welcome {pname}, with a rating of {rating:.3f},  player for {cntry}".format(cntry="India", pname="Sachin", rating=4.87659))

# interpolation
print("-" * 40)
from math import pi, e
print(f"PI = {pi} and Eulers constant = {e}")

print("-" * 40)
print("PI = {} and Eulers Constant = {}".format(pi, e))
print("PI = {} and Eulers constant = {} and magic number = {}".format(pi,e, 40585))
print("PI = {0} and Eulers constant = {1} and magic number = {magic}".format(pi,e, magic=40585))
print("PI = {magic} and Eulers constant = {} and magic number = {}".format(pi,e, magic=40585))

print("-" * 40)
full_name = ['Sachin', 'Tendulkar']
print(f"full_name :{full_name}")
print("Mr. {name}".format(name=full_name))
print("Mr. {name[0]} {name[1]}".format(name=full_name))

print("-" * 40)
import math
print(__name__)         # __main__
print(math.__name__)

print("{mod.__name__} module gives the value of PI = {mod.pi} and Eulers E = {mod.e}".format(mod=math))





