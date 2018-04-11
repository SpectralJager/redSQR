import sys
import random
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from PyQt5.QtCore import QSettings
from collections import defaultdict

ORGANIZATION_NAME = "SJager"
APPLICATION_NAME = "redSQR"
SETTING_MODE = 'setting/mode'
SETTING_LVL = 'setting/lvl'

class Startwind(QWidget):
	def __init__(self):
		super().__init__()
		uic.loadUi('startwind.ui',self)
		print('startwind created')
		self.setting = QSettings(ORGANIZATION_NAME,APPLICATION_NAME)
		self.entButton.pressed.connect(self.on_entButton) 

		self.mode = self.setting.value(SETTING_MODE)
		self.lvlMode = int(self.setting.value(SETTING_LVL))
		self.rang = 99
		self.score = 100
		self.lvl = 1
		self.res = 0
		self.up = int(self.label_8.text())
		print(self.mode,self.lvlMode)
		self.selectedMode()
						
			
	def on_entButton(self):		
		print(self.num_1,self.num_2)				
		print(self.res)
		if str(self.res) == self.lineEdit.text():
			self.label_8.setText(str(self.up + (self.score)))
			self.up = int(self.label_8.text())
			print('True')
		else:
			self.label_8.setText(str(self.up - (self.score)))
			self.up = int(self.label_8.text())
			print('False')
		self.lineEdit.setText('')
		self.selectedMode()
		

	def selectedMode(self):
		print('call selMode')
		if self.mode == '1':
			self.res = self.sumNum()
		elif self.mode == '2':
			self.res = self.subNum()
		elif self.mode == '3':
			self.res = self.multNum()
		elif self.mode == '4':
			self.res = self.divNum()
		elif self.mode == '5':
			self.allMode()

	def sumNum(self):
		print('sumNum')
		self.num_1 = random.randint(0,self.rang)		
		self.num_2 = random.randint(0,self.rang)
		self.label_5.setText('+')
		self.label_3.setText(str(self.num_1))
		self.label_4.setText(str(self.num_2))
		return self.num_1 + self.num_2

	def subNum(self):
		print('subNum')
		self.num_1 = random.randint(0,self.rang)		
		self.num_2 = random.randint(0,self.rang)
		self.label_5.setText('-')
		self.label_3.setText(str(self.num_1))
		self.label_4.setText(str(self.num_2))
		return self.num_1 - self.num_2

	def multNum(self):
		print('multNum')
		self.num_1 = random.randint(0,self.rang)		
		self.num_2 = random.randint(0,self.rang)
		self.label_5.setText('*')
		self.label_3.setText(str(self.num_1))
		self.label_4.setText(str(self.num_2))
		return self.num_1 * self.num_2

	def divNum(self):
		print('divNum')
		self.num_1 = random.randint(0,self.rang)		
		self.num_2 = random.randint(0,self.rang)
		if self.num_1 == 0 or self.num_2 == 0:
			self.divNum()
		self.label_5.setText('/')
		self.label_3.setText(str(self.num_1))
		self.label_4.setText(str(self.num_2))
		return self.num_1 / self.num_2

	def allMode(self):
		print('allMode')
		mode = random.randint(1,4)
		if mode == 1:
			self.res = self.sumNum()
		elif mode == 2:
			self.res = self.subNum()
		elif mode == 3:
			self.res = self.multNum()
		elif mode == 4:
			self.res = self.divNum()
		


