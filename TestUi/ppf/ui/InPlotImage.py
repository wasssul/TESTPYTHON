# -*- coding: utf-8 -*-

from PyQt5.QtCore import (Qt)
#from PyQt5.QtWidgets import (QTreeView, QDockWidget)
from PyQt5.QtGui import (QPainter, QColor, QFont)
from PyQt5.Qt import QWidget, QPen, QGraphicsScene, QLine, QMainWindow, QAction,\
    QIcon, QToolBar, QComboBox, QPixmap
from ppf.core.Utils import g, GUtils
from PyQt5.QtWidgets import QMenu

class InPlotForm(QMainWindow):
    
    def __init__(self, mainGui):
        super().__init__()
        self.mainGui = mainGui
        self.graphics = InPlotImage(self)
        self.setCentralWidget(self.graphics)
        self.initToolBar()
        #self.graphics.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.graphics.customContextMenuRequested.connect(self.openMenu)
    
    
    #def openMenu(self, position):
    #    action = self.graphics.mode.popMenu.exec_(self.mapToGlobal(position))
  
    def initToolBar(self):
        tb = QToolBar(self)
        self.addToolBar(Qt.LeftToolBarArea, tb)
        tb.actionTriggered[QAction].connect(self.toolAction)
        deleteAction = QAction(QIcon('ppf/ui/icons/delete.png'), 'delete all', self)
        deleteAction.a = lambda: self.graphics.deleteAll()
        tb.addAction(deleteAction)
        
        self.penCombo = QComboBox()
        tb.addWidget(self.penCombo)
        pixmap = QPixmap(20, 20)
        for pen in self.graphics.PENS:
            pixmap.fill(pen.color())
            self.penCombo.addItem(QIcon(pixmap), '')
        self.penCombo.currentIndexChanged.connect( lambda:self.penChanged() )
        
        self.linewidthCombo = QComboBox()
        tb.addWidget(self.linewidthCombo)
        pixmap = QPixmap(20, 20)
        for w in self.graphics.LINEWIDTH:
            qp = QPainter()
            pixmap.fill(Qt.white)
            qp.begin(pixmap)
            qp.fillRect(0, 0, 20, w, Qt.black)
            qp.end()
            self.linewidthCombo.addItem(QIcon(pixmap), '')    
        self.linewidthCombo.currentIndexChanged.connect( lambda:self.linewidthChanged() )
        
        #open = QAction(QIcon("open.bmp"),"open",self)
        #tb.addAction(open)
        #save = QAction(QIcon("save.bmp"),"save",self)
        #tb.addAction(save)
        #tb.actionTriggered[QAction].connect(self.toolbtnpressed)
        #self.setLayout(layout)
        #self.setWindowTitle("toolbar demo")
    def penChanged(self):
        self.graphics.currentPen = self.graphics.PENS[self.penCombo.currentIndex()]
    def linewidthChanged(self):
        self.graphics.currentWidth = self.graphics.LINEWIDTH[self.linewidthCombo.currentIndex()]
        
    def toolAction(self, a):
        g().outText.print('action')
        a.a()


class InPlotImage(QWidget):
    
    #self.mainGui
    #
    def __init__(self, parent):
        super().__init__()
        self.setGeometry(0, 0, 400, 300)
        
        self.parent = parent
        self.shapes = []
        self.PENS = [ QPen(Qt.red), QPen(Qt.green), QPen(Qt.blue), QPen(Qt.black), QPen(Qt.white) ]
        self.LINEWIDTH = [1, 2, 3, 4, 6, 8, 10, 15, 20]
        self.plots = []
        self.currentPen = self.PENS[0];
        self.currentWidth = 2;
        
        self.mode = MouseFollowDrawMode(self) 
        
    def  paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawAll(event, qp)
        qp.end()
    
    def mousePressEvent(self, event):
        #g().outText.print( "mousePressEvent" );
        #g().outText.print('x=' + str(event.pos().x()) + 'y=' + str(event.pos().y()))
        if event.button() == Qt.LeftButton:
            self.mode.mousePress(event.pos().x(), event.pos().y())
            #print('Left')
        else:
            pass
            #print('Right')
            #print(self.mode.popMenu)
            

    def mouseReleaseEvent(self, event):
        #self.text = 'Click'
        #if self.last == "Click":
        #    #QTimer.singleShot(QApplication.instance().doubleClickInterval(), self.performSingleClickAction)
        #else:
        #    # Perform double click action.
        ##   #self.message = "Double Click"
        #    #self.update()
        if event.button() == Qt.LeftButton:
            self.mode.mouseRelease(event.pos().x(), event.pos().y())
            print('Left')
        else:
            print('Right')
            print(self.mode.popMenu)
            #self.graphics.mapToGlobal(event.pos())
            try:
                a = self.mode.popMenu.exec_(self.mapToGlobal(event.pos()))
                a.a()
            except:
                import sys
                print("Unexpected error:", sys.exc_info()[0])
            
        
    
    def mouseMoveEvent(self, event):
        #g().outText.print( "mouseMoveEvent" );
        #g().outText.print('x=' + str(event.pos().x()) + 'y=' + str(event.pos().y()))
        self.mode.mouseMove(event.pos().x(), event.pos().y())
        
    def mouseLeaveEvent(self, event):
        #g().outText.print( "mouseLeaveEvent" );
        #g().outText.print('x=' + str(event.pos().x()) + 'y=' + str(event.pos().y()))
        pass
 
    def mouseDoubleClickEvent(self, event):
        #self.text = 'double click'
        #g().outText.print('double click'); 
        pass
        
    
    def drawAll(self, event, qp):
        for p in self.plots:
            p.draw(qp)
        #self.mode.draw(qp)
        #pen = QPen(QColor(168, 34, 3));
        #pen.setWidth(4);
        #qp.setPen(pen)
        #qp.drawLine(10, 10, 100, 10)
        #qp.setFont(QFont('Decorative', 10))
        #qp.drawText(event.rect(), Qt.AlignCenter, self.text) 
        
    def deleteAll(self):
        self.mode.deleteAll()
    
    
class Line:
    def __init__(self, startX, startY, endX, endY, pen, width):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.pen = pen
        self.width = width
        
    def draw(self, qp):
        #qp = QPainter()
        self.pen.setWidth(self.width)
        qp.setPen(self.pen)
        qp.drawLine(self.startX, self.startY, self.endX, self.endY)
        
class Lines:
    def __init__(self):
        self.lines = []
        
    def draw(self, qp):
        for line in self.lines:
            line.draw(qp)
    
    
class MouseFollowDrawMode:
    def __init__(self, inPlotImage):
        self.inPlotImage = inPlotImage
        self.isMousePressed = False
        self.lines = Lines()
        self.inPlotImage.plots.append(self.lines)
        self.currentX = 0;
        self.currentY = 0;
        self.initPopMenu()
        self.millis = GUtils().millis()
        
        
    # create context menu
    def initPopMenu(self):
        #self.inPlotImage.setContextMenuPolicy(Qt.CustomContextMenu)
        self.popMenu = QMenu(self.inPlotImage)
        a = QAction('test0', self.inPlotImage)
        a.a = lambda: g().outText.print('test0')
        self.popMenu.addAction(a)
        #self.popMenu.addAction(QAction('test1', self.inPlotImage))
        self.popMenu.addSeparator()
        #self.popMenu.addAction(QAction('test2', self.inPlotImage))
        #self.popMenu.actionTriggered[QAction].connect(self.menuAction)

    def menuAction(self, a):
        g().outText.print('action')
        a.a()        

    #def on_context_menu(self, point):
        # show context menu
         
        
    
        
    #def rightClick(self):
    #    self.popMenu.exec_(self.button.mapToGlobal(0,0))
    
    def mouseMove(self, x, y):
        if(self.isMousePressed and (GUtils().millis()-self.millis) > 50 ):
            #g().print('move(' + str(x) + ',' + str(y) + ')')
            self.startAddInBetweenLine(x, y)
            self.millis = GUtils().millis()
            
    
    def mousePress(self, x, y):
        self.isMousePressed = True
        self.startNewLines(x, y)
        self.millis = GUtils().millis()
    
    def mouseRelease(self, x, y):
        self.isMousePressed = False
        self.endLines(x, y)

    def startNewLines(self, x, y):
        self.currentX = x
        self.currentY = y
    
    def startAddInBetweenLine(self, x, y):
        self.lines.lines.append(Line(self.currentX, self.currentY, x, y, self.inPlotImage.currentPen, self.inPlotImage.currentWidth))
        self.currentX = x
        self.currentY = y
        self.inPlotImage.update()
        
    def endLines(self, x, y):    
        self.lines.lines.append(Line(self.currentX, self.currentY, x, y, self.inPlotImage.currentPen, self.inPlotImage.currentWidth))
        self.inPlotImage.update()
        
    def deleteAll(self):
        self.lines.lines.clear()
        self.inPlotImage.update()
'''
class Scene(QGraphicsScene):
    
    pens = [ QPen(Qt.green), QPen(Qt.green, 4) ]
    
    def __init__(self, parent):
        QGraphicsScene.__init__(self, parent)
        self.setSceneRect(-100, -100, 200, 200)
        
    
'''        
        
        