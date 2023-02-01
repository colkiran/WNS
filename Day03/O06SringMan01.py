
st1 = "hello world"
print(f"st1 :{st1}")
print(type(st1))

print("-" * 40)
# strings are stored like a list or an array
print(f"st1[0] :{st1[0]}")
print(f"st1[6] :{st1[6]}")
print(f"st1[10] :{st1[10]}")

print("-" * 40)
# slicing
print(f"st1[0:5] :{st1[0:5]}")
print(f"st1[6:11] :{st1[6:11]}")

print("-" * 40)
# reverse indexing
print(f"st1[-1] :{st1[-1]}")
print(f"st1[-5] :{st1[-5]}")
print(f"st1[-11] :{st1[-11]}")

# slicing reverse indexing
print("-" * 40)
print(f"st1[-1:-6:-1] :{st1[-1:-6:-1]}")
print(f"st1[-8:-12:-1] :{st1[-7:-12:-1]}")
print(f"st1[-1:-12:-1] :{st1[-1:-12:-1]}")

print("-" * 40)
# strings are immutable
# print(f"st1 :{st1}")
# st1[0] = "H"

# print(dir(st1))

st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print("replace".center(40, "-"))
# single character
print(f"st1 :{st1}")
res = st1.replace("h", "H")
print(f"res :{res}")

res = st1.replace("l", "L", 2)
print(f"res :{res}")

print("-" * 40)

print(f"st2 :{st2}")
res2 = st2.replace("fox", "tiger")
print(f"res2 :{res2}")

res2 = st2.replace("the", "The", 1)
print(f"res2 :{res2}")

print("find".center(40, "-"))
print(f"st1 :{st1}")

pos1 = st1.find("w")
print(f"pos1 :{pos1}")

pos2 = st1.find("l")
print(f"pos2 :{pos2}")

pos3 = st1.find("l", 6)
print(f"pos3 :{pos3}")

pos4 = st1.find("l", st1.find("l", st1.find("l")+1) + 1)
print(f"pos4 :{pos4}")