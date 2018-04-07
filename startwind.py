import sys
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class Startwind(QWidget):
	def __init__(self):
		super().__init__()
		uic.loadUi('startwind.ui',self)