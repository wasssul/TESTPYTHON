# -*- coding: utf-8 -*-

from PyQt5.QtCore import (Qt)
from PyQt5.QtWidgets import (QTreeView, QDockWidget)
from PyQt5.QtGui import (QStandardItemModel, QStandardItem)
from _operator import add
from PyQt5.Qt import QMainWindow, QAction, QIcon, QToolBar, QSize

class OutText(QMainWindow):
    
    #self.mainGui
    #self.treeView
    #self.dock
    
    def __init__(self, mainGui):
        super().__init__()
        self.mainGui = mainGui
        self.treeView = QTreeView(self)
        #self.treeView.setRootIsDecorated(False)
        self.treeView.setAlternatingRowColors(True)      
        self.treeModel = self.createModel()
        self.treeView.setModel(self.treeModel)
        self.setCentralWidget(self.treeView)
        self.initToolBar()
        #self.test()
        
    
    def initToolBar(self):
        tb = QToolBar(self)
        self.addToolBar(Qt.LeftToolBarArea, tb)
        tb.setIconSize( QSize(12, 12) )
        tb.actionTriggered[QAction].connect(self.toolAction)
        #tb.setToolButtonStyle()
        #tbStyle = tb.toolButtonStyle()
        #tb.setToolButtonStyle(tbStyle)
        deleteAction = QAction(QIcon("ppf/ui/icons/delete.png"), "delete all", self)
        deleteAction.a = lambda: self.treeModel.removeRows(0, self.treeModel.rowCount())
        #model = QStandardItemModel()
        #model.
        tb.addAction(deleteAction)
        
    #def clearAll(self):
            
        
    def toolAction(self, a):
        a.a()
        
    def test(self):
        row = QStandardItem('Test')
        self.treeModel.appendRow(row)
        #row = self.add("Test 0-1", "Test 0-2")
        
        for i in range(5):
            r = QStandardItem('row %d' % i)
            #row.appendRow
            row.appendRow([r, QStandardItem('message %d' % i)])
            ind = self.treeModel.indexFromItem(r) 
            rowNumber = ind.row()
            #self.treeModel.setData(self.treeModel.index(rowNumber+i+1, 1), )
        
        
        
    def add(self, name, message):
        row = QStandardItem(name)
        #row.appendRow
        self.treeModel.appendRow(row)
        ind = self.treeModel.indexFromItem(row) 
        rowNumber = ind.row()
        self.treeModel.setData(self.treeModel.index(rowNumber, 1), message)
        return self.treeModel.itemFromIndex(ind)
    
    def print(self, message):
        self.add('print', message)
        
    def createModel(self):
        model = QStandardItemModel(0, 2, self.treeView)
        model.setHeaderData(0, Qt.Horizontal, "Unit")
        model.setHeaderData(1, Qt.Horizontal, "Text")
        
        return model
 
        
        
        
        