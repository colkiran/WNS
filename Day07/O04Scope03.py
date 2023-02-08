
# nested functions

def outerFun():
    greet = "Hello World"

    def innerFun():
        nonlocal greet
        greet = "Greetings Mr. Sachin"
        print(f"Inside :{greet}")

    # outerfun Code
    innerFun()
    print(f"After :{greet}")

outerFun()
