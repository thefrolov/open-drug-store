# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from new_medorg_form_ui import Ui_new_medorg_form


class NewMedorgForm(QFrame):
	def __init__(self):
		QFrame.__init__(self)
		self.ui = Ui_new_medorg_form()
		self.ui.setupUi(self)
		QObject.connect(self.ui.ok_btn, SIGNAL("clicked()"), self.addMedorg)
		self.setWindowTitle(QString.fromUtf8('Добавление медицинской организации'))
		
	def addMedorg(self):
		mo = M_organisation()
		mo.name = str(self.ui.medorg_name.text().toUtf8())
		s = Session()
		s.add(mo)
		s.commit()
		s.close()
		self.emit(SIGNAL("medorgAdded()"))
		self.close()