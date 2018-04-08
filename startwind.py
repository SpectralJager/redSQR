import sys
import random
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic


class Startwind(QWidget):
	def __init__(self):
		super().__init__()
		uic.loadUi('startwind.ui',self)
		print('startwind created')
		self.entButton.pressed.connect(self.on_entButton)
		self.rang = 99
		self.up = int(self.label_8.text())
		self.res = self.sumNum()				
			
	def on_entButton(self):		
		print(self.num_1,self.num_2)				
		print(self.res)
		if str(self.res) == self.lineEdit.text():
			self.label_8.setText(str(self.up + (self.rang+1)))
			self.up = int(self.label_8.text())
			print('True')
		else:
			self.label_8.setText(str(self.up - (self.rang+1)))
			self.up = int(self.label_8.text())
			print('False')
		self.res = self.sumNum()

	def sumNum(self):
		self.num_1 = random.randint(0,self.rang)		
		self.num_2 = random.randint(0,self.rang)
		self.label_3.setText(str(self.num_1))
		self.label_4.setText(str(self.num_2))
		return self.num_1 + self.num_2


