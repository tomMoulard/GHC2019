class image:
    def __init__(self):
        self.h = True
        self.id = 0
        self.tags = []

def input_file(name):
    res=[]
    f = open(name, "r")
    n = int(f.readline())
    for i in range(n):
        l=f.readline().split()
        new=image()
        if l[0]=="V":
            new.h=False
        new.id = i;
        new.tags = l[2:]
        res+=[new]
    return res
