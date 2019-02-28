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

fil = open("a_data.txt", "r+")
print("provided/a_example.txt")
m(input_file("provided/a_example.txt"))
fil.close()

fil = open("b_data.txt", "r+")
print("b_lovely_landscapes.txt")
m(input_file("provided/b_lovely_landscapes.txt"))
fil.close()

fil = open("c_data.txt", "r+")
print("c_memorable_moments.txt")
m(input_file("provided/c_memorable_moments.txt"))
fil.close()

fil = open("d_data.txt", "r+")
print("d_pet_pictures.txt")
m(input_file("provided/d_pet_pictures.txt"))
fil.close()

fil = open("e_data.txt", "r+")
print("e_shiny_selfies.txt")
m(input_file("provided/e_shiny_selfies.txt"))
fil.close()
