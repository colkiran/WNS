
print('popitem'.center(40, "-"))
stud = {'name': 'Jack', 'class': '7th std', 'age': 12, 'school': 'NPS'}
print(f"stud :{stud}")

res1 = stud.popitem()
print(f"res1 :{res1}")
res2 = stud.popitem()
print(f"res2 :{res2}")

print(f"stud :{stud}")

print("items".center(40, "-"))
# items => keys + values

emp = {
'emp1' : {'name': 'Mike', 'age': 34, 'dept': 'Finance', 'loc': 'che', 'desig' : 'MGR'},
'emp2' : {'name': 'Tina', 'age': 32, 'dept': 'Marketting', 'loc': 'Blr', 'desig' : 'BDM'},
'emp3' : {'name': 'Marshal', 'age': 35, 'dept': 'Procurement', 'loc': 'Hyd', 'desig' : 'GM'}
    }

print(f"emp :{emp}")

print("-" * 40)

print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("-" * 40)

for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k + "=>" + str(v))
    print("-" * 40)

print("update".center(40, "-"))
emp1 = {'name': 'Mike', 'age': 34, 'dept': 'Finance', 'loc': 'che'}
emp2 ={'name': 'Tina', 'age': 32, 'dept': 'Marketting', 'desig' : 'BDM'}

# update the values of emp2 into emp1
print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

emp1.update(emp2)

print("-" * 40)
print(f"emp1 :{emp1}")
# print(f"emp2 :{emp2}")

