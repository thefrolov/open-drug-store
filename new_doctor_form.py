# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from new_doctor_form_ui import Ui_new_doctor_form


class NewDoctorForm(QFrame):
	def __init__(self):
		QFrame.__init__(self)
		self.ui = Ui_new_doctor_form()
		self.ui.setupUi(self)
		QObject.connect(self.ui.ok_btn, SIGNAL("clicked()"), self.addDoctor)
		self.setWindowTitle(QString.fromUtf8('Новый врач'))
		self.ui.m_org_combo.clear()
		
		m_orgs = query_session.query(M_organisation).all()
		for item in m_orgs:
			self.ui.m_org_combo.addItem(item.name)
	
	
	def addDoctor(self):
		doc = Doctor(self.ui.first_name.text(), self.ui.last_name.text())
		doc.m_organisation = query_session.query(M_organisation).filter_by(name=str(self.ui.m_org_combo.currentText().toUtf8())).one()
		s = Session()
		s.add(doc)
		s.commit()
		s.close()
		self.emit(SIGNAL("doctorAdded()"))
		self.close()