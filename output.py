from tom import *
from input import *
count=0
def output_file(name, res):
    name.write(" ".join(str(x) for x in res)+"\n")
    count+=1

def bite(file_name, file2):
    f=open(file_name,"r+")
    m(input_file(file2), f)
    print(file2)


def nb_line(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(str(count) + '\n' + content)
