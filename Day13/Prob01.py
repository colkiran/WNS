
FL = open("EMP.csv", "r")

gender = {}
dept = []
desig = []
sal = 0
sal1 = 0
for line in FL.readlines():
    gen = line.split(",")[2]
    ds = line.split(",")[3]
    dp = line.split(",")[4]

    if gen not in gender:
        gender[gen] = 1
    else:
        gender[gen] += 1

    if ds not in desig:
        desig.append(ds)

    if dp not in dept:
        dept.append(dp)

    sal += int(line.split(",")[5])

    if dp == "HR" and  gen == "f":
        sal1 += int(line.split(",")[5])



FL.close()

print(f"gender :{gender}")
print(f"desig  :{desig}")
print(f"dept   :{dept}")
print(f"salary :{sal}")
print(f"HR_Female :{sal1}")
