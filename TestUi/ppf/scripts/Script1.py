

class Script1:
    
    
    def __init__(self, obj):
        print('Script 1 __init__')
        self.count = 0
        print(obj)    
        
    def run(self):
        self.count += 1
        print(self.count)
        