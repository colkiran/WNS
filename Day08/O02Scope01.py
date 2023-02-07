
glbX = 100

def fun(n):             # local variable
    global glbX
    glbX = 500
    print(f"inside :{glbX}")
    print(f"n :{n}")

print(f"Before :{glbX}")
fun(10)
print(f"After :{glbX}")


