from input import *
from output import *

def m(l):
    print(l)
    this = l[0]
    while len(l) > 0:
        b = False
        for x in l:
            if b:
                break
            for tag in this.tags:
                if tag in x.tags:
                    print("pushing", x.id, x.tags)
                    output_file(x)
                    l.remove(x)
                    this = x
                    b = True
                    break

m(input_file("provided/a_example.txt"))

fil.close()
