from input import *
from output import *

def m(l, f):
    print(l)
    this = l[0]
    while len(l) > 0:
        b = False
        for x in l:
            if b:
                break
            for tag in this.tags:
                if tag in x.tags:
                    output_file(f, [x])
                    l.remove(x)
                    this = x
                    b = True
                    break


