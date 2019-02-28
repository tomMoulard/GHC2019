fil = open("data.txt", "a")
count=0
def output_file(res):
    fil.write(" ".join(str(x) for x in res))
