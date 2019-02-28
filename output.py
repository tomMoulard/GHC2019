from debug import trace
@trace
def output(res):
    fil = open("data.txt", "w")
    fil.write(res)
    fil.close()
