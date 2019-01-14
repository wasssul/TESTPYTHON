# -*- coding: utf-8 -*-

from PyQt5.QtCore import (Qt)
from PyQt5.QtWidgets import (QTreeView, QDockWidget)
from PyQt5.QtGui import (QStandardItemModel, QStandardItem, QPainter, QColor,
    QFont)
from PyQt5.Qt import QWidget

class InPlotImage(QWidget):
    
    #self.mainGui
    #
    
    def __init__(self, mainGui):
        super().__init__()
        self.mainGui = mainGui
        self.text = 'Hello world'
        self.setGeometry(0, 0, 400, 300)
        
    def  paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()
        
        
    
    def drawText(self, event, qp):
      
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text) 
    
    
    
        
        
        