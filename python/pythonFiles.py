import os
import sys

def py_getTxtFileDataAsList(path):
    """
    Gives the list of all the lines in the txt File.
    path = Full path (Dir + FileName)
    """
    if os.path.exists(path):
        with open(path, "r") as f:
            list = []
            for line in f:
                line = line.strip()
                list.append(line)
            return list
    else:
        print "Path Directory Does Not Exists"

def py_getTxtFileInfo(path):
    """
    Get the Info of the data that is present in the txt File
    Total Lines = RESULT
    Total Characters = RESULT
    """
    numLines = numWords = numChars = 0

    with open(path,'r') as f:
        for line in f:
            words = line.split()
            numLines += 1 - line.count(' ')
            numWords += len(words)
            numChars += len(line) - line.count(' ')
    print 'Total Lines =',numLines
    # print 'Words =',numWords
    print 'Total Characters =',numChars

def py_printTxtFileData(path):
    with open (path,'r') as f:
        data = f.read()
        print data



