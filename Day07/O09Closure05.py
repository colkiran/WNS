


def fun(*args):
    print(*args)
    print("-" * 40)


def outerFun(fnc):      # HOF

    def innerFun(*args):
        fnc(*args)

    return innerFun

infun = outerFun(fun)
infun()
infun(1)
infun(1, 2)
infun(1, 2, 3, 4, 5)

print("-" * 40)

def sum(x, y):
    return x + y

def diff(x, y):
    return x - y

def log_detail(fnc):
    loginfo = "Logging into the service"

    def innerFun(*args):
        print(loginfo)
        print(fnc(*args))
        print("-" * 40)

    return innerFun

sumlogger = log_detail(sum)
diflogger = log_detail(diff)

sumlogger(10, 20)
diflogger(40, 15)


