import sys
import random
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import QSettings, QTimer
from collections import defaultdict


ORGANIZATION_NAME = "SJager"
ORGANIZATION_DOMAIN = "None"
APPLICATION_NAME = "redSQR"
SETTING_MODE = 'setting/mode'
SETTING_LVL = 'setting/lvl'


class Mainwindow(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('redSQR.ui',self)
		print('mainwind created')
		self.tabWidget.setCurrentIndex(0)
		self.startButton.clicked.connect(self.startButton_push)
		self.scoreboardButton.clicked.connect(self.scoreboardButton_push)
		self.settingButton.clicked.connect(self.settingButton_push)
		self.quitButton.clicked.connect(self.close)
###########def_button######################
	def startButton_push(self):
		self.tabWidget.setCurrentIndex(1)
		self.Startwind()
		print('Startwind create!')

	def scoreboardButton_push(self):
		self.tabWidget.setCurrentIndex(3)
		
		print('Scoreboard create!')

	def settingButton_push(self):
		self.tabWidget.setCurrentIndex(2)
		self.Settingwind()
		print('Settingwind create!')
###########def_button#####################
###########Startwind######################
	def Startwind(self):
		self.setting = QSettings(ORGANIZATION_NAME,APPLICATION_NAME)
		self.entButton.pressed.connect(self.on_entButton_push) 

		self.mode = self.setting.value(SETTING_MODE)
		self.lvlMode = int(self.setting.value(SETTING_LVL))
		self.rang = 99
		self.rang_2 = 9
		self.score = 50.0
		self.lvl = 1
		self.res = 0
		self.timeMin = 0
		self.timeHour = 3
		self.numRes = 20.0
		self.tr_answ = 0
		self.up = float(self.pointLabel.text())
		self.timer = QTimer()

		print(self.mode,self.lvlMode)
		self.timer.timeout.connect(self.changeTimer)
		self.timer.start(1200)
		self.selectedMode()

	def on_entButton_push(self):		
		print(self.num_1,self.num_2)				
		#print(self.res)
		if str(self.res) == self.lineEdit.text():
			self.pointLabel.setText(str(self.up + (self.score)))
			self.tr_answ += 1
			if self.tr_answ == self.numRes*self.lvl:
				self.score = self.score*1.50
				if self.numRes > 5:
					self.numRes -= 4 
				self.lvl += 1
				self.levelLabel.setText('Level ' + str(self.lvl))
				if (self.lvl%2 == 0) and (self.mode == '3' or self.mode == '4'):
					self.rang *= 10
					self.rang += 9
				else:
					self.rang_2 *= 10
					self.rang_2 += 9
			self.up = float(self.pointLabel.text())
			print('True')
		else:
			self.pointLabel.setText(str(self.up - (self.score)))
			self.up = float(self.pointLabel.text())
			print('False')
		self.lineEdit.setText('')
		print(self.rang,self.rang_2)
		self.selectedMode()
		

	def selectedMode(self):
		print('call selMode')
		if self.mode == '1':
			self.operationLabel.setText('+')
			self.res = self.sumNum()
		elif self.mode == '2':
			self.operationLabel.setText('-')
			self.res = self.subNum()
		elif self.mode == '3':
			self.operationLabel.setText('*')
			self.res = self.multNum()
		elif self.mode == '4':
			self.operationLabel.setText('/')
			self.divNum()
		elif self.mode == '5':
			self.allMode()
		print(self.res)

	def sumNum(self):
		print('sumNum')
		self.num_1 = random.randint(0,self.rang)		
		self.num_2 = random.randint(0,self.rang)
		self.firstNum.setText(str(self.num_1))
		self.secondNum.setText(str(self.num_2))
		return self.num_1 + self.num_2

	def subNum(self):
		print('subNum')
		self.num_1 = random.randint(0,self.rang)		
		self.num_2 = random.randint(0,self.rang)
		self.firstNum.setText(str(self.num_1))
		self.secondNum.setText(str(self.num_2))
		return self.num_1 - self.num_2

	def multNum(self):
		print('multNum')
		self.num_1 = random.randint(0,self.rang)		
		self.num_2 = random.randint(self.rang_2//10,self.rang_2)
		self.firstNum.setText(str(self.num_1))
		self.secondNum.setText(str(self.num_2))
		return self.num_1 * self.num_2

	def divNum(self):
		#print('divNum')
		while True:
			self.num_1 = random.randint(0,self.rang)		
			self.num_2 = random.randint(self.rang_2//10,self.rang_2)
			if self.num_1 == 0 or self.num_2 == 0:
				self.divNum()

			if self.num_1 > self.num_2:
				if (self.num_1 % self.num_2) == 0:
					self.firstNum.setText(str(self.num_1))
					self.secondNum.setText(str(self.num_2))
					self.res = self.num_1 // self.num_2
					return
				else:
					continue
			else: 
				continue
		

	def allMode(self):
		print('allMode')
		mode = random.randint(1,4)
		if mode == 1:
			self.operationLabel.setText('+')
			self.res = self.sumNum()
		elif mode == 2:
			self.operationLabel.setText('-')
			self.res = self.subNum()
		elif mode == 3:
			self.operationLabel.setText('*')
			self.res = self.multNum()
		elif mode == 4:
			self.operationLabel.setText('/')
			self.divNum()

	def changeTimer(self):		
		
		if self.timeMin < 0:
			self.timeHour -= 1
			self.timeMin = 59
		else:
			if self.timeMin < 10:
				time = '   ' + str(self.timeHour) + ':0' + str(self.timeMin)
			else:
				time = '   ' + str(self.timeHour) + ':' + str(self.timeMin)
			self.timeLabel.setText(time)
			self.timeMin -= 1
		if self.timeHour < 0:
			# save record
			#.......
			#return on main paige
			self.close()	
###########Startwind######################
###########Settingwind####################
	def Settingwind(self):
		self.saveSettingButton.clicked.connect(self.on_saveSettingButton_clicked)
		self.setting = QSettings(ORGANIZATION_NAME,APPLICATION_NAME)
		mode = self.setting.value(SETTING_MODE)
		lvl = self.setting.value(SETTING_LVL)
		if mode == '1':
			self.plusButton.setChecked(True)
		elif mode == '2':
			self.minusButton.setChecked(True)
		elif mode == '3':
			self.multiplyButton.setChecked(True)
		elif mode == '4':
			self.divideButton.setChecked(True)
		elif mode == '5':
			self.allButton.setChecked(True)

		if lvl == '1':
			self.easyButton.setChecked(True)
		elif lvl == '2':
			self.normalButton.setChecked(True)
		elif lvl == '3':
			self.hardButton.setChecked(True)

	def on_saveSettingButton_clicked(self):		
		if self.plusButton.isChecked():
			self.setting.setValue(SETTING_MODE, '1')
		elif self.minusButton.isChecked():
			self.setting.setValue(SETTING_MODE, '2')
		elif self.multiplyButton.isChecked():
			self.setting.setValue(SETTING_MODE, '3')
		elif self.divideButton.isChecked():
			self.setting.setValue(SETTING_MODE, '4')
		elif self.allButton.isChecked():
			self.setting.setValue(SETTING_MODE, '5')

		if self.normalButton.isChecked():
			self.setting.setValue(SETTING_LVL,'2')
		elif self.easyButton.isChecked():
			self.setting.setValue(SETTING_LVL,'1')
		elif self.hardButton.isChecked():
			self.setting.setValue(SETTING_LVL,'3')
###########Settingwind####################
###########ScoreBoardwind#################
	