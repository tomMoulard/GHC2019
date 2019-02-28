from tom import *
from input import *
count=0
def output_file(name, res):
    name.write(" ".join(str(x) for x in res)+"\n")

def bite(file_name, file2):
    f=open(file_name,"r+")
    m(input_file(file2), f)
    print(file2)
