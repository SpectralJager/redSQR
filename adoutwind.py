import sys
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from PyQt5.QtCore import QUrl

SOURCE = 'about.html'

class Aboutwind(QWidget):
	def __init__(self):
		super().__init__()
		uic.loadUi('aboutwind.ui',self)
		self.textBrowser.setSource(QUrl(SOURCE))