

import json

class Preferences:
    def __init__(self):
        self.settFile = 'ppf/data/pref/sett.json'
        self.data = {}
        self.onDataLoaded = []
        
    def onLoaded(self, fun):
        self.onDataLoaded.append(fun)
        return len(self.onDataLoaded)
    
    def removeOnLoadByIndex(self, ind):
        del( self.onDataLoaded[ind] )
    
    def removeOnLoadByValue(self, fun):
        self.onDataLoaded.remove(fun)
        
    def getValue(self, key, val):
        if(key in self.data):
            return self.data[key]
        else:
            return val
    
    def load(self):
        try:
            file = open(self.settFile, 'r') 
            self.data = json.load(file) 
            
            for fun in self.onDataLoaded:
                fun(self)
        except:
            pass
            
            
    def save(self):
        try:
            file = open(self.settFile, 'w') 
            json.dump(self.data, file)
        except:
            pass