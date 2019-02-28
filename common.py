from input import *

def nb_common(img1, img2):
    s = 0
    for t in img1.tag:
        if t in img2.tag:
            s += 1
    return s
