from debug import *
from input import *
from sys import argv
from random import randrange

debug = False


@trace
def sim(a, b):
    return 1 - diff(a, b)

@trace
def diff(a, b):
    s = 0
    for e in a:
        if e in b:
            s += 1
    s /= max((len(a), len(b)))
    return 1 - s

@trace
def NOPEget_closest(img, l):
    if not l:
        return img
    return l[-1]
    return l[randrange(len(l))]

@trace
def get_closest(img, l):
    if not l:
        return img
    res = l[0]
    di = diff(img.tags, l[0].tags)
    for i in l[1:]:
        d = diff(img.tags, i.tags)
        if d < di:
            di = d
            res = i
    return res

@trace
def get_sorted(l):
    res = []
    e = l[0]
    for i in l:
        if not i.visited:
            i.visited= True
            res.append(e)
            l.remove(e)
            e = get_closest(res[-1], l)
    res.append(e)
    l.remove(e)
    #res.append(get_closest(res[-1], l))
    return res

@trace
def merge(a, b):
    for e in a:
        if not e in b:
            b.append(e)
    return b

@trace
def get_merged(l):
    res = []
    v = []
    for i in l:
        if i.h:
            res.append(i)
        else:
            v.append(i)
    for i in range(0, len(v), 2):
        img = image()
        img.id = f"{v[i].id} {v[i+1].id}"
        img.tags = merge(v[i].tags, v[i+1].tags)
        img.h = True
        res.append(img)
    return res

l = input_file(argv[1])

s = argv[1].split("/")[-1]
with open("res_" + s + ".txt", "w+") as f:
    l = get_merged(l)
    tmp = len(l) // 1000
    for x  in range(1000):
        ll= get_sorted(l[tmp * x:tmp * (x + 1)])
        print(len(ll), file=f)
        for i in ll:
            print(i.h, i.tags)
            print(i.id, file=f)

