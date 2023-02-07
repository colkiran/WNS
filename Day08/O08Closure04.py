
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(name):
            from emojis import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + name)
            print(emojized)

        return innerMostFun

    return innerFun

KanGrt = outerFun("Namaskara")
TigerKgrt = KanGrt("tiger")
TigerKgrt("Prabhakar")


"""
outerFun("Welcome")("------>")("Sachin")

engGrt = outerFun("Welcome")
hindGrt = outerFun("Namaskar")

singlArwEgrt = engGrt("----->")
dblArwEgrt = engGrt("=====>>")
singlArwHgrt = hindGrt("----->")
dblArwHgrt = hindGrt("=====>>")

singlArwEgrt("Virat")
dblArwHgrt("Axar Patel")
"""