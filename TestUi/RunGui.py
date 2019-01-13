

from PyQt5.QtWidgets import QApplication

from ppf.MainGui import MainGui


import sys


#sys.path.append('ui')

app = QApplication(sys.argv)
mainWin = MainGui()
mainWin.show()
sys.exit(app.exec_())