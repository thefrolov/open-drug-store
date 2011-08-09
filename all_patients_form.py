# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from all_patients_form_ui import Ui_all_patients_form
from new_patient_form import NewPatientForm

class AllPatientsWindow(QFrame):
	def __init__(self):
		QFrame.__init__(self)
		self.ui = Ui_all_patients_form()
	
		self.ui.setupUi(self)
		self.patients = query_session.query(Patient).all()
		self.drawTable()
		QObject.connect(self.ui.add_patient_btn, SIGNAL("clicked()"), self.showNewPatientForm)
		QObject.connect(self.ui.del_patient_btn, SIGNAL("clicked()"), self.delPatient)
	
	def drawTable(self):
		self.patients = query_session.query(Patient).all()
		self.ui.patients_table.clear()
		self.ui.patients_table.setRowCount(1)
		self.ui.patients_table.setColumnCount(4)
		self.ui.patients_table.setHorizontalHeaderLabels([QString.fromUtf8('Номер'), QString.fromUtf8('Фамилия'), QString.fromUtf8('Имя'), QString.fromUtf8('Дата рождения')])
		self.ui.patients_table.resizeColumnsToContents()
		
		for patient in self.patients:
			data = []
			data.append(str(patient.id))
			data.append(patient.last_name)
			data.append(patient.first_name)
			data.append(patient.birth_date.strftime("%d.%m.%Y"))
			for i in range(0,4):	
				tableitem = QTableWidgetItem()
				tableitem.setText(data[i])
				tableitem.font = QFont("Arial", 10)
				tableitem.font.setBold(True)
				tableitem.textcolor = QColor("black")
				self.ui.patients_table.setItem(self.ui.patients_table.rowCount() - 1,i,tableitem)
			self.ui.patients_table.setRowCount(self.ui.patients_table.rowCount()+1)
		self.ui.patients_table.resizeColumnsToContents()
				
	def showNewPatientForm(self):
		self.new_patient_form = NewPatientForm()
		QObject.connect(self.new_patient_form, SIGNAL("patientAdded()"), self.drawTable)
		self.new_patient_form.setWindowModality(2)
		self.new_patient_form.show()
		
		
	def delPatient(self):
		row = self.ui.patients_table.currentRow()
		id_for_delete = int(self.ui.patients_table.item(row, 0).text())
		patient_for_delete = query_session.query(Patient).filter_by(id=id_for_delete).one()
		s = Session()
		s.delete(patient_for_delete)
		s.commit()
		s.close
		self.drawTable()