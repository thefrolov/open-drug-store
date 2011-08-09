# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from new_financing_form_ui import Ui_new_financing_form


class NewFinancingForm(QFrame):
	def __init__(self, parent):
		QFrame.__init__(self)
		self.ui = Ui_new_financing_form()
		self.ui.setupUi(self)
		self.parent = parent
		self.setWindowTitle(QString.fromUtf8('Создание источника финансирования'))
		QObject.connect(self.ui.ok_btn, SIGNAL("clicked()"), self.addFinancing)
		
	def addFinancing(self):
		fin = Financing(str(self.ui.financing_name.text().toUtf8()))
		s = Session()
		s.add(fin)
		s.commit()
		s.close()
		self.emit(SIGNAL("financingAdded()"))
		self.close()