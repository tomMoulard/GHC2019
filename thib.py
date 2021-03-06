from debug import *
from input import *
from sys import argv
from random import randrange
from copy import *

debug = False


def sim(a, b):
    return 1 - diff(a, b)

def diff(a, b):
    s = 0
    for e in a:
        if e in b:
            s += 1
    s /= max((len(a), len(b)))
    return 1 - s

def DENYget_closest(img, l):
    if not l:
        return img
    return l[-1]
    return l[randrange(len(l))]

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

def NOPEget_closest(img, l):
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

def get_sorted(l):
    if not l:
        return l
    res = []
    e = l[0]
    for i in l:
        res.append(e)
        l.remove(e)
        e = get_closest(res[-1], l)
    res.append(e)
    l.remove(e)
    #res.append(get_closest(res[-1], l))
    return res

def merge(a, b):
    for e in a:
        if not e in b:
            b.append(e)
    return b



def get_merged(l):
    res = []
    v = []
    for i in l:
        if i.h:
            res.append(i)
        else:
            v.append(i)
    #v.sort(key = lambda a: len(a.tags))
    #if v:
    #    v = get_sorted(v)
    for i in range(0, len(v) // 2):
        img = image()
        img.id = f"{v[i].id} {v[-(i + 1)].id}"
        img.tags = merge(v[i].tags, v[i+1].tags)
        img.h = True
        res.append(img)
    return res

l = input_file(argv[1])
l = get_merged(l)
print(len(l))

res = []

scope = 201

for i in range(0, len(l), scope):
    print("\r", 100 * i / len(l), i,  end='                                 ')
    if i + scope > len(l):
        d = l[i:]
        if d:
            res += get_sorted(deepcopy(d))
    else:
        res += get_sorted(deepcopy(l[i:i+scope]))
print()

s = argv[1].split("/")[-1]
with open("res_" + s + ".txt", "w+") as f:
    print(len(l), file=f)
    for i in res:
        #print(i.h, i.tags)
        print(i.id, file=f)

