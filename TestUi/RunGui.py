

from PyQt5.QtWidgets import QApplication
from ppf.MainGui import MainGui
from ppf.core.Utils import g
import os

print(g().mainPath)
g().set(mainPath=os.getcwd())
#g().loadScripts()

print(g().mainPath)
#sys.path.append('ui')

import sys
app = QApplication(sys.argv)
mainWin = MainGui()
mainWin.show()
sys.exit(app.exec_())