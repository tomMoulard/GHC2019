from tom import *
from input import *
count=0
def output_file(name, res):
    name.write(" ".join(str(x.id) for x in res)+"\n")
    count+=1

def nb_line(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(str(count) + '\n' + content)
