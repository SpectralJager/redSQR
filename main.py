from mainwindow import Mainwindow
from PyQt5.QtWidgets import QApplication 
import sys

app = QApplication(sys.argv)
mw = Mainwindow()
mw.show()
sys.exit(app.exec_())
