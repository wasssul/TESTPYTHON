

from PyQt5.QtGui import (QIcon, QKeySequence)
from PyQt5.QtWidgets import (QAction)

#from ppf.MainGui import MainGui

class Menu:
    '''
    self.mainGui
    self.fileMenu
    self.openDatasetAction
    '''
    def __init__(self, mainGui):
        self.mainGui = mainGui
        self.createFileMenu()
        self.createScriptMenu()
        self.createHelpMenu()
        
        
    def createFileMenu(self):
        self.fileMenu = self.mainGui.menuBar().addMenu("&File")
        self.openDatasetAction = QAction(QIcon(':/save.png'), "&Open", self.mainGui,
                shortcut=QKeySequence.Open,
                statusTip="Open dataset", triggered=self.mainGui.browseDataset)
        self.fileMenu.addAction(self.openDatasetAction);
          
        
    def createScriptMenu(self):
        pass
        
    def createHelpMenu(self):
        pass
       
        
        