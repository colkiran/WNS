
FL = open("data.txt", "r")           # read is the default mode

# res = FL.read(1500)           # reads the entire contents of the file
# print(res)

# res = FL.readline()             # read one line at a time (line break)
# print(res)

res = FL.readlines(857)
print(res)
#
# for line in res:
#     print(line)
#
# for line in FL.readlines():
#     print(line)


FL.close()