

from PyQt5.QtWidgets import QApplication
from ppf.MainGui import MainGui
from ppf.core.Utils import g


#print(g().mainPath)
#g().set(mainPath=os.getcwd())
#g().loadScripts()

#print(g().mainPath)
#sys.path.append('ui')

import os
import sys
app = QApplication(sys.argv)
mainWin = MainGui()

g().set(mainPath=os.getcwd(), outText=mainWin.outText, outPlot=mainWin.outPlot)

mainWin.show()
sys.exit(app.exec_())