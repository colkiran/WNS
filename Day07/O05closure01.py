
def outerFun(info):
    inf = "Mr." + info

    def innerFun():
        print(info)
        print(inf)

    innerFun()

outerFun("Sachin")