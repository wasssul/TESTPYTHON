

from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QDockWidget)

from ppf.ui.Menu import Menu
from ppf.ui.OutText import OutText


        
class MainGui(QMainWindow):
    def __init__(self):
        super(MainGui, self).__init__()
        self.setGeometry(100, 100, 500, 400)
        self.ppfmenu = Menu(self)
        self.outText = OutText(self)
        
    def browseDataset(self):
        options = QFileDialog.Options() | QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open dataset", "", "All Files (*);;Dataset Files (*.arff)", options=options)
        if fileName:
            print(fileName)

