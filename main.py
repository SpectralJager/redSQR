from mainwindow import Mainwindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication 
import sys

ORGANIZATION_NAME = "SJager"
ORGANIZATION_DOMAIN = "None"
APPLICATION_NAME = "redSQR"

QCoreApplication.setOrganizationName(ORGANIZATION_NAME)
QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
QCoreApplication.setApplicationName(APPLICATION_NAME)

app = QApplication(sys.argv)
mw = Mainwindow()
mw.show()
sys.exit(app.exec_())
