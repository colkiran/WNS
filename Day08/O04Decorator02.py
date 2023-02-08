
def doubleMesh(fnc):
    def helper(*args):
        print("-" * 40)
        fnc(*args)              # callback
        print("#" * 40)
    return helper


def startSingle(fnc):
    def helper(*args):
        print("*" * 40)
        fnc(*args)
        print("_" * 40)
    return helper


@startSingle
@doubleMesh
def fun1(x, y):
    print(f"fun2 called......{x}{y}")

fun1(10, 20)
