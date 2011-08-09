# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from all_manufacters_form_ui import Ui_all_manufacters_form
from new_manufacter_form import NewManufacterForm

class AllManufactersWindow(QFrame):
	def __init__(self):
		QFrame.__init__(self)
		self.ui = Ui_all_manufacters_form()
	
		self.ui.setupUi(self)
		#self.manufacters = query_session.query(Manufacter).all()
		self.drawTable()
		QObject.connect(self.ui.add_manufacter_btn, SIGNAL("clicked()"), self.showNewManufacterForm)
		QObject.connect(self.ui.del_manufacter_btn, SIGNAL("clicked()"), self.delManufacter)
	
	def drawTable(self):
		self.manufacters = query_session.query(Manufacter).all()
		self.ui.manufacters_table.clear()
		self.ui.manufacters_table.setRowCount(1)
		self.ui.manufacters_table.setColumnCount(3)
		self.ui.manufacters_table.setHorizontalHeaderLabels([QString.fromUtf8('Номер'), QString.fromUtf8('Название'), QString.fromUtf8('Страна')])
		self.ui.manufacters_table.resizeColumnsToContents()
		
		for manufacter in self.manufacters:
			data = []
			data.append(str(manufacter.id))
			data.append(manufacter.name)
			data.append(manufacter.country)
			for i in range(0,3):	
				tableitem = QTableWidgetItem()
				tableitem.setText(data[i])
				tableitem.font = QFont("Arial", 10)
				tableitem.font.setBold(True)
				tableitem.textcolor = QColor("black")
				self.ui.manufacters_table.setItem(self.ui.manufacters_table.rowCount() - 1,i,tableitem)
			self.ui.manufacters_table.setRowCount(self.ui.manufacters_table.rowCount()+1)
		self.ui.manufacters_table.resizeColumnsToContents()
				
	def showNewManufacterForm(self):
		self.new_manufacter_form = NewManufacterForm(self)
		QObject.connect(self.new_manufacter_form, SIGNAL("manufacterAdded()"), self.drawTable)
		self.new_manufacter_form.setWindowModality(2)
		self.new_manufacter_form.show()
		
		
	def delManufacter(self):
		row = self.ui.manufacters_table.currentRow()
		id_for_delete = int(self.ui.manufacters_table.item(row, 0).text())
		manufacter_for_delete = query_session.query(Manufacter).filter_by(id=id_for_delete).one()
		s = Session()
		s.delete(manufacter_for_delete)
		s.commit()
		s.close
		self.drawTable()