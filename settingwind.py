import sys
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from PyQt5.QtCore import QSettings

ORGANIZATION_NAME = "SJager"
ORGANIZATION_DOMAIN = "None"
APPLICATION_NAME = "redSQR"
SETTING_MODE = 'setting/mode'
SETTING_LVL = 'setting/lvl'

class Settingwind(QWidget):
	def __init__(self):
		super().__init__()
		uic.loadUi('settingwind.ui',self)
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

	


