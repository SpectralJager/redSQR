import sys
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class Settingwind(QWidget):
	def __init__(self):
		super().__init__()
		uic.loadUi('settingwind.ui',self)