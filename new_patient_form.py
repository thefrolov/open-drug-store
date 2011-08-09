# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from new_patient_form_ui import Ui_new_patient_form


class NewPatientForm(QFrame):
	def __init__(self):
		QFrame.__init__(self)
		self.ui = Ui_new_patient_form()
		self.ui.setupUi(self)
		QObject.connect(self.ui.ok_btn, SIGNAL("clicked()"), self.addPatient)
		self.setWindowTitle(QString.fromUtf8('Добавление нового пациента'))
	
	def addPatient(self):
		p = Patient()
		p.first_name = str(self.ui.first_name.text().toUtf8())
		p.last_name = str(self.ui.last_name.text().toUtf8())
		p.birth_date= _date_from_str(self.ui.birth_date.text())
		s = Session()
		s.add(p)
		s.commit()
		s.close()
		self.emit(SIGNAL("patientAdded()"))
		self.close()