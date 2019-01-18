
class Globals:
    
    def __init__(self):
        self.mainPath = None
        self.outText = None
        self.outPlot = None
        self.scripts = None;
        
    def set(self, mainPath, outText, outPlot):
        self.mainPath = mainPath
        self.outText = outText
        self.outPlot = outPlot
        
    def loadScripts(self):
        if(self.scripts == None):
            self.scripts = ScriptUtils()
        self.scripts.load()
        
        
        
    

ppf_ = Globals()
'''
returns the global variables
'''
def g():
    return ppf_
    

import os
class ScriptUtils:
    
    def __init__(self):
        pass
    
    def load(self):
        dirPath = os.path.join( g().mainPath, 'ppf', 'scripts')
        print(dirPath)
        for file in os.listdir(dirPath):
            print('file', file)
            modPath = 'ppf.scripts.' + file
            print('modPath', modPath)
            module = __import__(modPath)
            print('module', module)
            
            
            
            