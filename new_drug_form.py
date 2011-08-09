# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from new_drug_form_ui import Ui_new_drug_form
from count_form import CountForm
from new_manufacter_form import NewManufacterForm

class NewDrugForm(QFrame):
	def __init__(self):
		QFrame.__init__(self)
		self.ui = Ui_new_drug_form()
		self.ui.setupUi(self)
		
		QObject.connect(self.ui.ok_btn, SIGNAL("clicked()"), self.addDrug)
		self.drawManufacterCombo()
		#self.setManufacter(0)
		
		
	def addDrug(self):
		drug = Drug(str(self.ui.drug_name.text().toUtf8()), self.manufacter, str(self.ui.serial_number.text().toUtf8()), _date_from_str(self.ui.best_before.text()), float(self.ui.price.text().toUtf8()))
		s = Session()
		s.add(drug)
		s.commit()
		s.close()
		self.emit(SIGNAL("drugCreated()"))
		self.close()
		
		
	def drawManufacterCombo(self):
		combo = self.ui.manufacter_combo
		items = self.manufacters = query_session.query(Manufacter).all()
		combo.clear()
		for item in items:
			combo.addItem(item.name)
		combo.addItem(QString.fromUtf8('Новый производитель'))
		QObject.connect(self.ui.manufacter_combo, SIGNAL("currentIndexChanged(int)"), self.setManufacter)
		self.setManufacter(0)
	
	
	def setManufacter(self,num):
		c = self.ui.manufacter_combo.count()
		if (num < self.ui.manufacter_combo.count() - 1):
			manufacter = query_session.query(Manufacter).filter_by(name=unicode(self.ui.manufacter_combo.itemText(num))).one()
			self.manufacter = manufacter
		else:
			self.new_manufacter_form = NewManufacterForm(self)
			self.new_manufacter_form.setWindowModality(2)
			self.new_manufacter_form.show()
			QObject.connect(self.new_manufacter_form, SIGNAL("manufacterAdded()"), self.drawManufacterCombo)
