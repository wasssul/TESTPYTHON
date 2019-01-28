

from PyQt5.QtWidgets import QApplication
from ppf.MainGui import MainGui
from ppf.core.Utils import g, ScriptUtils


#print(g().mainPath)
#g().set(mainPath=os.getcwd())
#g().loadScripts()

#print(g().mainPath)
#sys.path.append('ui')


import os
import sys
import time
from ppf.core.Preferences import Preferences
#i = round(time.time() * 1000)
#print( i )

ScriptUtils().load()
'''

#pref = Preferences()
#pref.save()
pref = Preferences()
pref.load()
#print(pref.data['str'])
#print(pref.data['int'])
#print(pref.data['float'])

app = QApplication(sys.argv)
mainWin = MainGui()

g().set(mainPath=os.getcwd(), outText=mainWin.outText, outPlot=mainWin.outPlot)

mainWin.show()
sys.exit(app.exec_())



'''
