global indent, debug
indent = 0
debug = True


def trace(f):
    def wrap(*args, **kwargs):
        global indent, debug
        if not debug:
            return f(*args, **kwargs)
        print(indent * " ", f.__name__, "entered with", args, kwargs)
        indent += 4
        r = f(*args, **kwargs)
        indent -= 4
        print(indent * " ", f.__name__, "out")
        return r
    return wrap

@trace
def f(i):
    if i:
        return f(i - 1)

def g(i):
    print(f(i))

if __name__ == "__name":
    g(4)
