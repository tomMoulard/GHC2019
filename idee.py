from debug import *
from input import *
from sys import argv
from random import randrange, shuffle

debug = False


def get_sorted(l):
    m = len(max(l, key = lambda x: len(x.tags)).tags)
    for i in range(4):
        l.sort(key = lambda x: x.tags[i] if (i < len(x.tags)) else "\255")
    #l.sort(key = lambda x: x.tags[1] if len(x.tags) else "")
    
    return l


def merge(a, b):
    for e in a:
        if not e in b:
            b.append(e)
    return b

def get_merged(l):
    res = []
    v = []
    for i in l:
        i.tags.sort()
        for s in i.tags:
            i.rtags += str(sorted(s))
        if i.h:
            res.append(i)
        else:
            v.append(i)
    if v:
        v.sort(key = lambda x: len(x.tags))
        v = get_sorted(v)
    for i in range(0, len(v) // 2):
        img = image()
        a = i
        b = len(v) - 1 - i
        img.id = f"{v[a].id} {v[b].id}"
        img.tags = merge(v[a].tags, v[b].tags)
        img.tags.sort()
        img.h = True
        res.append(img)
    return res

l = input_file(argv[1])
res = get_merged(l)
print(argv[1], len(res))
#res = sorted(l, key=lambda x: x.rtags)

#res.sort(key = lambda x: len(x.tags))

#res = get_sorted(res)

d = {}
tags = []
i = 1

print("COUNTING TAGS")

for e in res:
    for t in e.tags:
        try:
            d[t] += 1
        except:
            d[t] = 1

print("SORT TAGS PER OCCURENCE")

tags = list(d.items())
tags.sort(key = lambda x: x[1])
d = {}

print("STORE TAGS VALUE IN DICT")

print(len(tags))

for t, o in tags:
    d[t] = 1 << i
    i += 1

print("APPLY TAGS VALUE TO IMAGES")

for e in res:
    for t in e.tags:
        e.value |= d[t]

print("SORT IMAGES USING VALUES")

res.sort(key = lambda x: x.value)

print("OUTPUTING...")

s = argv[1].split("/")[-1]
with open("res_" + s, "w+") as f:
    print(len(res), file=f)
    for i in res:
        print(i.id, file=f)
print("DONE !!! \n")
