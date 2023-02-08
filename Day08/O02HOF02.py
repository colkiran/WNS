
def funlogger(fnc):

    def helper():
        print("Logging into a service......")
        fnc()
        print("Logging out of the service.....")

    return helper


def normal_fun():
    print("They call me a normal function......")

print("-" * 40)
funlogger(normal_fun)       # no output

print("-" * 40)
funlogger(normal_fun)()     # direct call to the helper

print("-" * 40)
res_fun = funlogger(normal_fun)
res_fun()

print("-" * 40)
normal_fun = funlogger(normal_fun)
normal_fun()

print("=" * 40)

@funlogger          # decorator (basicfun = funlogger(basicfun))
def basicFun():
    print("They call me basic function......")

basicFun()