__ver__ = (' 0.1 ')
__author__ = (' sraka ')


import inspect

print "Module Imported"

class inspectWrapper():
    def __init__(self , modulename):
        
        print 'Class Called'
        print modulename.__name__
        # for key, data in inspect.getmembers(modulename, inspect.isfunction):
        #     print ('{} '.format(key, data))


   
    @staticmethod
    def listFunctions():
        print "AAA"
        for key, data in inspect.getmembers(self.modulename, inspect.isfunction):
            print ('{} '.format(key, data))
    
    def listClass(self):
        for key, data in inspect.getmembers(self.modulename, inspect.isclass):
            print ('{} '.format(key, data))
    
    def listFunctions(self):
        pass

     










