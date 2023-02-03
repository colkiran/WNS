
"""
sort        - sort the original list
sorted      - sort the list and returns a copy of it, the original list remains              the same
reverse or reversed
"""

l1 = [7, 5, 2, 9, 1, 10, 3, 6, 4, 8]
print(f"l1 Before :{l1}")

asc_res = sorted(l1)
print(f"Ascending Order :{asc_res}")

desc_res = sorted(l1, reverse=True)
print(f"Descending Order :{desc_res}")

print("-" * 40)

l1 = [7, 'zebra', 'apple',  5, 'yellow', 'blue', 2, 'xray', 'cat', 9, 'pink', 'red', 1, 'violet', 'green', 10, 'dog', 'magenta', 3, 'egg', 'frog', 6, 4, 8,
      1024, 187, 12, 2133, 29, 253]
print(f"l1 Before :{l1}")

print("-" * 40)
res = sorted(l1, key=ascii)
print(f"res :{res}")

print("=" * 40)

cities = ['thiruvananthapuram', 'bangalore', 'mumbai', 'delhi', 'vishakapatnam', 'pune', 'kanyakumari', 'hyderabad', 'mysore', 'ooty', 'coimbatore']

print(f"cities :{cities}")
print("-" * 40)

res = sorted(cities,key=len)
print(f"res :{res}")

print("=" * 40)

months = ['oct', 'apr', 'aug', 'dec', 'jul', 'feb', 'sep', 'nov', 'mar', 'jan', 'may', 'jun']

# sort these months according to the canlendar
"""
def sort_list(x):
    priorities = {"jan":1, "feb":2, "mar":3, "apr":4, "may":5, "jun":6, "jul":7, "aug":8, "sep":9, "oct":10, "nov":11, "dec":12 }
    return priorities[x]

print(sorted(months ,key=sort_list))
"""
from calendar import month_name
# print(list(month_name))
l = []
for month in list(month_name):
    l.append(month[0:3].lower())

def sort_list(mon):
    if mon in l:
        return l.index(mon)

print(sorted(months ,key=sort_list))

print("-" * 40)
l1 = [7, 5, 2, 9, 1, 10, 3, 6, 4, 8]
print(f"l1 Before :{l1}")
res = list(reversed(l1))

print(f"res :{res}")

l1.clear()
print(f"l1 :{l1}")