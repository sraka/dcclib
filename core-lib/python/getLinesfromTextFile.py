import os

def getLinesfromTextFile(path=None):
    with open(path,'r') as f:
        fLines = f.readlines()
        print fLines
        return fLines