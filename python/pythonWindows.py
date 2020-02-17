import os
import sys

def sys_path_append(path):
    '''
    Append path in sys only if its not already present
    :param path:
    :return:
    '''
    if path in sys.path:
        print 'Path already present'
    else:
        sys.path.append(str(path))
        print 'Path Added'


def get_folder_list(path):
    ''' 
    Will return the list of all the Folders present in the Directory
    path = Directory
    '''
    filenames = os.listdir(path)
    list = []
    for filename in filenames: 
        if os.path.isdir(os.path.join(os.path.abspath(path), filename)):
            list.append(filename)
    return list
    
    
    
    