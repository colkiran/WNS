
# coversions
print('conversions'.center(40, "-"))
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("The number {num} {num} {num}".format(num=36))
print("The number {num} {num:f} {num:b}".format(num=36))
print("The number {num:10} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=3634535645))

print("-" * 40)
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

from math import pi, e
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

# alignment
print("-" * 40)
print("{:10.2f}".format(pi))
print("{:<15} Tendulkar".format("Sachin"))          # left align
print("{:^15} Tendulkar".format("Sachin"))          # center align
print("{:>15} Tendulkar".format("Sachin"))          # right align
print("{:10.2f} Sachin".format(pi))
print("{:<10.2f} Sachin".format(pi))
print("{:^10.2f} Sachin".format(pi))
print("{:010.2f} Sachin".format(pi))

print("-" * 40)
print("One Googol is {}".format(10 ** 100))
print("One Googol is {:,}".format(10 ** 100))

print("{:-^40}".format("Python Training"))
print("Python Training".center(40,"-"))

print("-" * 40)
print("{0} \t {1}".format(pi, e))
print("{0:.2} \t {1:.2}".format(pi, e))
print("{0:.3} \t {1:.3}".format(pi, e))
print("{0:-.3} \t {1:-.3}".format(-pi, -e))
print("{0:+.3} \t {1:+.3}".format(pi, e))

print("-" * 40)
print("{:b}".format(10))
print("{:#b}".format(10))

