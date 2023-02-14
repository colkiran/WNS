import sys
from sys import path
path.append("C:/Delhi")
for pth in path:
    print(pth)

# print(sys.path)         # environment path for storing modules

from gurgaon.mymodule import Player, greet

print("-" * 40)
greet("Virat Kholi")

print("-" * 40)
ply1 = Player("Yuvraj", 32)
ply1.get_details()

print("-" * 40)
print(dir())

print("-" * 40)
print(sys.executable)