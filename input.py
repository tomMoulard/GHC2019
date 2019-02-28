class image:
    def __init__(self):
        self.h = True
        self.id = 0
        self.tags = []

def input(name):
    res=[]
    f = open(name, "r")
    n = int(f.readline())
    for i in range(n):


