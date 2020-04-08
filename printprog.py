def printfile(fileloc):
    with open(fileloc) as f:
        print(f.read())
        return 100
