import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from adoutwind import Aboutwind
from settingwind import Settingwind
from startwind import Startwind 

class Mainwindow(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('mainwindow.ui',self)
		self.pushButton.clicked.connect(self.on_pushButton_clicked)
		self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
		self.pushButton_3.clicked.connect(self.on_pushButton_3_clicked)
		self.pushButton_4.clicked.connect(self.close)

	def on_pushButton_clicked(self):
		self.stw = Startwind()
		print('call startwind')
		self.stw.show()
		#self.close()

	def on_pushButton_2_clicked(self):
		sttw = Settingwind()
		sttw.show()

	def on_pushButton_3_clicked(self):
		abw = Aboutwind()
		abw.show()

