def readTxt(filename):
    f = open(filename, "rt")
    for x in f:
        print(x.split(" "))
    