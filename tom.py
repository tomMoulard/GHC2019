from input import image

def min(l):
    this = l[0]
    while l.length() > 0:
        b = False
        for x in l:
            if b:
                break
            for tag in this.tags:
                if tag in x.tags:
                    print("pushing", x.id)
                    l.remove(x)
                    this = x
                    b = True

min(input_file)
