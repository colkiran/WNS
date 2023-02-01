
print("Arithmetic Operators".center(40,"-"))
print(f"10 + 3 = {10 + 3}")
print(f"10 - 3 = {10 - 3}")
print(f"10 * 3 = {10 * 3}")
print(f"10 / 3 = {10 / 3}")
print(f"10 // 3 = {10 // 3}")
print(f"10 % 3 = {10 % 3}")
print(f"10 ** 3 = {10 ** 3}")

print("Augmentor".center(40, "-"))
# +=, -=, /=, *=, =
x = 10
print(f"x :{x}")
x += 5
print(f"x :{x}")
x /= 3
print(f"x :{x}")
x *= 5
print(f"x :{x}")

print("Comparison Operator".center(40, "-"))
# ==, >, >=, <, <=, !=
x = 10
y = 5
print(f"x == y :{x == y}")
print(f"x > y  :{x > y}")
print(f"x >= y :{x >= y}")
print(f"x != y :{x != y}")

print("Logical Operators".center(40, "-"))
# and, or, not
print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 1 and 2 == 1 :{1 == 1 and 2 == 1}")
print(f"1 == 1 or 2 == 2  :{1 == 1 or 2 == 2}")
print(f"1 == 2 or 2 == 2 :{1 == 2 or 2 == 2}")
print(f"not(1 == 1 and 2 == 1) :{not(1 == 1 and 2 == 1)}")
print(f"not(1 == 1 or 2 == 2)  :{not(1 == 1 or 2 == 2)}")

print("-" * 40)
print(f"ord('A') :{ord('A')}")      # integer representation of unicode character
print(f"ord('a') :{ord('a')}")
print(f"ord('Z') :{ord('Z')}")
print(f"ord('z') :{ord('z')}")
print("apple" > "orange")
print("apple" < "orange")

print("Bitwise Operators".center(40, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")

print(f"16 >> 1: {16 >> 1}")
print(f"5 >> 1 :{5 >> 1}")
print(~0)
print(~5)

print("-" * 40)
# ternary Operator

a = 18
print("Eligible" if a >= 18 else "Not Eligible")
