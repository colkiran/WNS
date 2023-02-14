
FL = open("data.txt", "rb")

pos = FL.seek(100, 0)
print(f"pos :{pos}")

pos = FL.seek(75, 1)
print(f"pos :{pos}")

pos = FL.seek(100, 2)
print(f"pos :{pos}")

pos = FL.seek(0, 2)             # points the EOF
print(f"pos :{pos}")

FL.close()

"""
FL.seek(120, 0)

FL.seek(45, 1)

FL.seek(-85, 1)

FL.seek(200, 2)

FL.seek(-500, 2)

FL.seek(-10, 0)
"""