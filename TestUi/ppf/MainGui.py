

from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QDockWidget)
from PyQt5.QtCore import (Qt)

from ppf.ui.Menu import Menu
from ppf.ui.OutText import OutText
from ppf.core.Utils import g
from ppf.ui.InPlotImage import InPlotImage

        
class MainGui(QMainWindow):
    def __init__(self):
        super(MainGui, self).__init__()
        self.setGeometry(100, 100, 500, 400) 
        self.bottomDock = None
        self.ppfmenu = Menu(self)
        self.outText = OutText(self)
        self.dockBottom('OutText', self.outText.treeView)
        self.outPlot = None
        
        self.inPlot = InPlotImage(self)
        self.setCentralWidget(self.inPlot)
        #self.dockBottom('InPlot', self.inPlot)
        
    def dockBottom(self, txt, widget):
        dock = QDockWidget(txt, self);
        self.addDockWidget(Qt.BottomDockWidgetArea, dock)
        dock.setAllowedAreas(Qt.BottomDockWidgetArea) 
        dock.setWidget(widget)
        if(self.bottomDock != None):
            self.tabifyDockWidget(self.bottomDock, dock)
        self.bottomDock = dock
            
        
    def browseDataset(self):
        options = QFileDialog.Options() | QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open dataset", "", "All Files (*);;Dataset Files (*.arff)", options=options)
        if fileName:
            print(fileName)
            
        print(g().mainPath)
        
        
    def testInPlotImage(self):
        dock = QDockWidget("In plot image", self)
        dock.setAllowedAreas(Qt.BottomDockWidgetArea)
        dock.setWidget(self.inplot)
        
        #self.treeView.setRootIsDecorated(False)
        #self.treeView.setAlternatingRowColors(True)        
        #self.dock.setWidget(self.treeView)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock)
        
