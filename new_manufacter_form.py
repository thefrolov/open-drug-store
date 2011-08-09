# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from new_manufacter_form_ui import Ui_new_manufacter_form


class NewManufacterForm(QFrame):
	def __init__(self, parent):
		QFrame.__init__(self)
		self.ui = Ui_new_manufacter_form()
		self.ui.setupUi(self)
		self.parent = parent
		self.setWindowTitle(QString.fromUtf8('Добавить нового производителя'))
		QObject.connect(self.ui.ok_btn, SIGNAL("clicked()"), self.addManufacter)
		
	def addManufacter(self):
		manufacter = Manufacter(str(self.ui.manufacter_name.text().toUtf8()), str(self.ui.manufacter_country.text().toUtf8()))
		s = Session()
		s.add(manufacter)
		s.commit()
		s.close()
		self.emit(SIGNAL("manufacterAdded()"))
		self.close()