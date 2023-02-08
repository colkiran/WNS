

def postiveRes(fnc):

    def helper(a, b):
        if a < b:
            a, b = b, a
        print(fnc(a, b))
        print("-" * 40)

    return helper

@postiveRes
def sub(x, y):
    return x - y

sub(10, 20)
sub(30, 20)
sub(20, 50)
sub(500, 750)


