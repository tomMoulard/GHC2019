from tom import *
from input import *
from output import *


def bite(file2, file_name):
    count=0
    f=open(file_name,"r+")
    m(input_file(file2), f, count)
    print(file2)


bite("./provided/a_example.txt", "e.txt")
bite("./provided/b_lovely_landscapes.txt", "a.txt")
bite("./provided/c_memorable_moments.txt", "b.txt")
bite("./provided/d_pet_pictures.txt", "c.txt")
bite("./provided/e_shiny_selfies.txt", "d.txt")
