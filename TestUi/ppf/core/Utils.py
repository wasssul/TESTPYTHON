import os
import time


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
    


class ScriptUtils:
    
    def __init__(self):
        pass
    
    def load(self):
        dirPath = 'ppf/scripts' #os.path.join( g().mainPath, 'ppf', 'scripts')
        scripts = []
        #print(dirPath)
        for file in os.listdir(dirPath):
            if(not file.startswith('__')):
                #print('file', file)
                modPath = 'ppf.scripts.' + file
                #print('modPath', modPath)
                module = __import__(modPath[0:-3])
                script = getattr(getattr(module.scripts, file[0:-3]), file[0:-3])
                scripts.append(script('init comment'))
                #print('script: ', script)
            
    
"""
General utilities
"""        
class GUtils:
    
    def millis(self):
        i = round(time.time() * 1000)
        return i
    
                
            
            