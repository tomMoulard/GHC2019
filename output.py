from debug import trace
@trace
def output:
    fil = open("data.txt", "w")
    fil.write("Bonjour monde")
    fil.close()
