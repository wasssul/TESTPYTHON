

class Script1:
    
    
    def __init__(self):
        print('Script 1 __init__')
        self.count = 0
        
    def run(self):
        print(self.count)
        self.count += 1
        