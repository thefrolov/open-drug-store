# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from all_medorg_form_ui import Ui_all_medorg_form
from new_medorg_form import NewMedorgForm

class AllMedorgWindow(QFrame):
	def __init__(self):
		QFrame.__init__(self)
		self.ui = Ui_all_medorg_form()
	
		self.ui.setupUi(self)
		self.drawTable()
		QObject.connect(self.ui.add_medorg_btn, SIGNAL("clicked()"), self.showNewMedorgForm)
		QObject.connect(self.ui.del_medorg_btn, SIGNAL("clicked()"), self.delMedorg)
	
	def drawTable(self):
		self.mos = query_session.query(M_organisation).all()
		self.ui.medorg_table.clear()
		self.ui.medorg_table.setRowCount(1)
		self.ui.medorg_table.setColumnCount(2)
		self.ui.medorg_table.setHorizontalHeaderLabels([QString.fromUtf8('Номер'), QString.fromUtf8('Название')])
		
		for mo in self.mos:
			data = []
			data.append(str(mo.id))
			data.append(mo.name)
			for i in range(0,2):	
				tableitem = QTableWidgetItem()
				tableitem.setText(data[i])
				tableitem.font = QFont("Arial", 10)
				tableitem.font.setBold(True)
				tableitem.textcolor = QColor("black")
				self.ui.medorg_table.setItem(self.ui.medorg_table.rowCount() - 1,i,tableitem)
			self.ui.medorg_table.setRowCount(self.ui.medorg_table.rowCount()+1)
		self.ui.medorg_table.resizeColumnsToContents()

				
	def showNewMedorgForm(self):
		self.new_medorg_form = NewMedorgForm(self)
		QObject.connect(self.new_medorg_form, SIGNAL("medorgAdded()"), self.drawTable)
		self.new_medorg_form.setWindowModality(2)
		self.new_medorg_form.show()
		
		
	def delMedorg(self):
		row = self.ui.medorg_table.currentRow()
		id_for_delete = int(self.ui.medorg_table.item(row, 0).text())
		medorg_for_delete = query_session.query(M_organisation).filter_by(id=id_for_delete).one()
		s = Session()
		s.delete(medorg_for_delete)
		s.commit()
		s.close
		self.drawTable()