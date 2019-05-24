import os
import sys

def lazy_sys_path_append(path):
    import sys
    if path in sys.path:
        print 'Path already present'
    else:
        sys.path.append(str(path))
        print 'Path Added'


def py_getDirFolderList(path):
    ''' 
    Will return the list of all the Folders present in the Directory
    path = Directory
    '''
    filenames = os.listdir(path)
    list = []
    for filename in filenames: 
        if os.path.isdir(os.path.join(os.path.abspath(path ), filename)):
            list.append(filename)
    return list
    
    
    
    