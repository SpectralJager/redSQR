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
		print('mainwind created')
		self.stwind.pressed.connect(self.on_stwind_clicked)
		self.pushButton_2.pressed.connect(self.on_pushButton_2_clicked)
		self.pushButton_3.pressed.connect(self.on_pushButton_3_clicked)
		self.pushButton_4.pressed.connect(self.close)

	def on_stwind_clicked(self):
		self.stw = Startwind()
		print('call startwind')
		self.stw.show()
		self.close()

	def on_pushButton_2_clicked(self):
		self.sttw = Settingwind()
		print('call sttw')
		self.sttw.show()

	def on_pushButton_3_clicked(self):
		self.abw = Aboutwind()
		print('call abw')
		self.abw.show()

