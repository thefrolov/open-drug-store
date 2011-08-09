# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from all_doctors_form_ui import Ui_all_doctors_form
from new_doctor_form import NewDoctorForm

class AllDoctorsWindow(QFrame):
	def __init__(self):
		QFrame.__init__(self)
		self.ui = Ui_all_doctors_form()
	
		self.ui.setupUi(self)
		self.doctors = query_session.query(Doctor).all()
		self.drawTable()
		QObject.connect(self.ui.add_doctor_btn, SIGNAL("clicked()"), self.showNewDoctorForm)
		QObject.connect(self.ui.del_doctor_btn, SIGNAL("clicked()"), self.delDoctor)
		QObject.connect(self.ui.close_btn, SIGNAL("clicked()"), self.closeme)
	
	def drawTable(self):
		self.doctrors = query_session.query(Doctor).all()
		self.ui.doctors_table.clear()
		self.ui.doctors_table.setRowCount(1)
		self.ui.doctors_table.setColumnCount(4)
		self.ui.doctors_table.setHorizontalHeaderLabels([QString.fromUtf8('Номер'), QString.fromUtf8('Фамилия'), QString.fromUtf8('Имя'), QString.fromUtf8('Мед. организация')])
		self.ui.doctors_table.resizeColumnsToContents()
		
		for doctror in self.doctrors:
			data = []
			data.append(str(doctror.id))
			data.append(doctror.last_name)
			data.append(doctror.first_name)
			data.append(doctror.m_organisation.name)
			for i in range(0,4):	
				tableitem = QTableWidgetItem()
				tableitem.setText(data[i])
				tableitem.font = QFont("Arial", 10)
				tableitem.font.setBold(True)
				tableitem.textcolor = QColor("black")
				self.ui.doctors_table.setItem(self.ui.doctors_table.rowCount() - 1,i,tableitem)
			self.ui.doctors_table.setRowCount(self.ui.doctors_table.rowCount()+1)
		self.ui.doctors_table.resizeColumnsToContents()
#				
	def showNewDoctorForm(self):
		self.new_doctor_form = NewDoctorForm()
		QObject.connect(self.new_doctor_form, SIGNAL("doctorAdded()"), self.drawTable)
		self.new_doctor_form.setWindowModality(2)
		self.new_doctor_form.show()
		
		
	def delDoctor(self):
		row = self.ui.doctors_table.currentRow()
		id_for_delete = int(self.ui.doctors_table.item(row, 0).text())
		doctor_for_delete = query_session.query(Doctor).filter_by(id=id_for_delete).one()
		s = Session()
		s.delete(doctor_for_delete)
		s.commit()
		s.close
		self.drawTable()
		
	def closeme(self):
		self.parent().close()