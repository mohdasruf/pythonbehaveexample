def printfile(fileloc):
    with open(fileloc,"r") as f:
        data = f.readlines()
        print(f.read())
        return data
