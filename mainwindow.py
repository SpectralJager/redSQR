import sys
import random
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import QSettings, QTimer
from collections import defaultdict
from PyQt5.QtGui import QKeyEvent,QPixmap,QPalette,QBrush


ORGANIZATION_NAME = "SJager"
ORGANIZATION_DOMAIN = "None"
APPLICATION_NAME = "redSQR"
SETTING_MODE = 'setting/mode'
SETTING_LVL = 'setting/lvl'


class Mainwindow(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('redSQR.ui',self)

		mainOrigPixmap = QPixmap('./frame1.png')
		palette0 = QPalette()
		palette0.setBrush(self.mainBgLabel.backgroundRole(),QBrush(mainOrigPixmap))
		self.mainBgLabel.setPalette(palette0)

		
		origPixmap = QPixmap('./frame2.png')

		palette = QPalette()
		palette.setBrush(self.bgLabel1.backgroundRole(),QBrush(origPixmap))
		self.bgLabel1.setPalette(palette)

		palette2 = QPalette()
		palette2.setBrush(self.bgLabel2.backgroundRole(),QBrush(origPixmap))
		self.bgLabel2.setPalette(palette2)

		palette3 = QPalette()
		palette3.setBrush(self.bgLabel3.backgroundRole(),QBrush(origPixmap))
		self.bgLabel3.setPalette(palette3)

		palette4 = QPalette()
		palette4.setBrush(self.bgLabel4.backgroundRole(),QBrush(origPixmap))
		self.bgLabel4.setPalette(palette4)


		print('mainwind created')
		self.setting = QSettings(ORGANIZATION_NAME,APPLICATION_NAME)
		self.tabWidget.setCurrentIndex(0)
		self.startButton.clicked.connect(self.startButton_push)
		self.scoreboardButton.clicked.connect(self.scoreboardButton_push)
		self.settingButton.clicked.connect(self.settingButton_push)
		self.quitButton.clicked.connect(self.closeWind)
		self.entButton.pressed.connect(self.on_entButton_push)
		self.timer = QTimer()
		self.timer.timeout.connect(self.changeTimer)

###########def_button######################
	def startButton_push(self):
		print('Startwind create!')
		self.currentIndex = 1
		self.tabWidget.setCurrentIndex(1)
		self.Startwind()
		

	def scoreboardButton_push(self):
		self.currentIndex = 3		
		self.tabWidget.setCurrentIndex(3)
		self.ScoreBoardwind()
		print('Scoreboard create!')

	def settingButton_push(self):
		self.currentIndex = 2
		self.tabWidget.setCurrentIndex(2)
		self.Settingwind()
		print('Settingwind create!')

	def closeWind(self):
		self.currentIndex = 4
		self.close()
###########def_button#####################

###########Startwind######################
	def Startwind(self):
		#self.count+=1
		#print(self.count)
		self.mode = self.setting.value(SETTING_MODE)
		self.lvlMode = int(self.setting.value(SETTING_LVL))
		self.rang = 9
		self.rang_2 = 9
		self.score = 50.0
		self.lvl = 1
		self.res = 0
		self.timeSec = 0
		self.timeMin = 3
		self.numRes = 20.0
		self.tr_answ = 0
		self.pointLabel.setText('0.0')
		self.up = float(self.pointLabel.text())

		print(self.mode,self.lvlMode)
		self.timer.start(1200)

		self.selectedMode()
		return
		
	def on_entButton_push(self):		
		#print(self.num_1,self.num_2)				
		#print(self.res)
		if str(self.res) == self.lineEdit.text():
			self.pointLabel.setText(str(self.up + (self.score)))
			self.tr_answ += 1
			if self.tr_answ == self.numRes:
				self.tr_answ = 0
				self.score = self.score*1.50
				if self.numRes > 5:
					self.numRes -= 4 
				self.lvl += 1
				self.levelLabel.setText('Level ' + str(self.lvl))
				if self.lvl % 2 == 0:
					self.rang *= 10
					self.rang += 9
				elif self.lvl % 2 == 1:
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
		return
		

	def selectedMode(self):
		print('call selMode')
		mode = self.mode
		if self.mode == '5':
			mode = str(random.randint(1,4))
		if mode == '1':
			self.operationLabel.setText('+')
			self.sumNum()
		elif mode == '2':
			self.operationLabel.setText('-')
			self.subNum()
		elif mode == '3':
			self.operationLabel.setText('*')
			self.multNum()
		elif mode == '4':
			self.operationLabel.setText('/')
			self.divNum()
		#print(self.res)
		return

	def sumNum(self):
		print('sumNum')
		self.num_1 = random.randint(self.rang//9,self.rang)		
		self.num_2 = random.randint(self.rang_2//9,self.rang_2)
		self.firstNum.setText(str(self.num_1))
		self.secondNum.setText(str(self.num_2))
		self.res = self.num_1 + self.num_2
		return

	def subNum(self):
		print('subNum')
		self.num_1 = random.randint(self.rang//9,self.rang)		
		self.num_2 = random.randint(self.rang_2//9,self.rang_2)
		self.firstNum.setText(str(self.num_1))
		self.secondNum.setText(str(self.num_2))
		self.res = self.num_1 - self.num_2
		return

	def multNum(self):
		print('multNum')
		while True:
			self.num_1 = random.randint(self.rang//9,self.rang)		
			self.num_2 = random.randint(self.rang_2//9,self.rang_2)
			if self.num_2 <= 2:
				continue
			else:
				self.firstNum.setText(str(self.num_1))
				self.secondNum.setText(str(self.num_2))
				self.res = self.num_1 * self.num_2
				break
		return

	def divNum(self):
		print('divNum')
		while True:
			self.num_1 = random.randint(self.rang//9,self.rang)		
			self.num_2 = random.randint(self.rang_2//9,self.rang_2)
			if self.num_1 == 0 or self.num_2 == 0:
				continue
			elif self.num_1 > self.num_2:
				if (self.num_1 % self.num_2) == 0:
					self.firstNum.setText(str(self.num_1))
					self.secondNum.setText(str(self.num_2))
					self.res = self.num_1 // self.num_2
					break
		return
		
	def changeTimer(self):
		if self.currentIndex != 1:
				self.timer.stop()
				print('false')
				return	
		
		if self.timeSec < 0:
			self.timeMin -= 1
			self.timeSec = 59
		else:
			if self.timeSec < 10:
				time = '   ' + str(self.timeMin) + ':0' + str(self.timeSec)
			else:
				time = '   ' + str(self.timeMin) + ':' + str(self.timeSec)
			self.timeLabel.setText(time)
			self.timeSec -= 1
		if self.timeMin < 0:
			#self.timer.stop()
			print('time out')
			# save record
			self.saveRecord()
			#return on main paige
			self.currentIndex = 0
			self.tabWidget.setCurrentIndex(0)
		return

	def saveRecord(self):
		print('save rec')
		mode = self.mode
		if mode == '5':
			mode = 'all'
		elif mode == '1':
			mode = '+'
		elif mode == '2':
			mode = '-'
		elif mode == '3':
			mode = '*'
		elif mode == '4':
			mode = '/'
		#print(mode,self.pointLabel.text())
		rec_file = open('score.txt','r')
		#print('file open')
		temp = [x for x in rec_file.read().split('\n')]
		rec_file.close()
		#leng = len(temp)
		#print(temp)
		temp = [x.split(' ') for x in temp]
		print(temp)
		#print(1)
		#print(self.pointLabel.text())
		for i in range(0,5):
		#	print(i)
			if temp[i][0] < self.pointLabel.text():
				print('change pos')
				temp.insert(i,[self.pointLabel.text(),mode])
				break  
		print(temp)
		temp2 = []
		for i in range(0,5):
			temp2.append(temp[i][0]+' '+temp[i][1]+'\n')
		print(temp2)
		#print([x for x in temp2])
		rec_file = open('score.txt','w')
		[rec_file.write(x) for x in temp2]
		rec_file.close()
		return

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
	def ScoreBoardwind(self):
		#print('hi')
		rec_file = open('score.txt','r')
		temp = [x for x in rec_file.read().split('\n')]
		rec_file.close()
		#print(temp)
		leng = len(temp)
		temp = [x.split(' ') for x in temp]
		#print(temp)
		for i in range(0,leng):
			if (i+1) == 1:
				self.score1.setText(temp[i][0])
				self.mode1.setText(temp[i][1])
			elif (i+1) == 2:
				self.score2.setText(temp[i][0])
				self.mode2.setText(temp[i][1])
			elif (i+1) == 3:
				self.score3.setText(temp[i][0])
				self.mode3.setText(temp[i][1])
			elif (i+1) == 4:
				self.score4.setText(temp[i][0])
				self.mode4.setText(temp[i][1])
			elif (i+1) == 5:
				self.score5.setText(temp[i][0])
				self.mode5.setText(temp[i][1])
