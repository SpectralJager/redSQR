import sys
import random
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QKeyEvent
from PyQt5 import uic


class Startwind(QWidget):
	def __init__(self):
		super().__init__()
		uic.loadUi('startwind.ui',self)
		self.entButton.clicked.connect(self.on_entButton_clicked)
		self.rang = 99
		self.up = int(self.label_8.text())
		self.start()
		
	def start(self):				
		self.num_1 = random.randint(0,self.rang)		
		self.num_2 = random.randint(0,self.rang)
		print(self.num_1,self.num_2)		
		self.label_3.setText(str(self.num_1))
		self.label_4.setText(str(self.num_2))
		
			
	def on_entButton_clicked(self):
		self.res = self.num_1 + self.num_1
		print(self.res)
		if str(self.res) == self.lineEdit.text():
			self.label_8.setText(str(self.up + (self.rang+1)))
			self.up = int(self.label_8.text())
			print('True')
		else:
			self.label_8.setText(str(self.up - (self.rang+1)))
			self.up = int(self.label_8.text())
			print('False')
		self.start()


