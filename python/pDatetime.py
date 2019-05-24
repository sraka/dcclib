import datetime
from time import gmtime, strftime

'''
import sys
sys.path.append(r'D:\__CS\___HOME_DIR\pipeline\CoreLibrary\modulePythonM')
import xdatetime as xdatetime;reload(xdatetime)

'''
def get_current_date(mode=1):
    '''
        @returns : Current Date
        
    '''
    if mode == 1:
        return datetime.date.today().__str__()
    elif mode == 2:
        return strftime("%Y-%m-%d", gmtime())
    elif mode == 3:
        return datetime.datetime.now().strftime('%Y-%m-%d')
    else:
        raise ValueError('Wrong mode number')
        
        
def get_current_time(mode=1):
    '''
        @returns : Current Time
        
    '''
    if mode == 1:
        return strftime("%H:%M:%S", gmtime())
    elif mode ==2:
        return datetime.datetime.now().strftime('%H:%M:%S')

def get_current_datetime():
    '''
        @returns : Current Date & Time
        
    '''
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')



 