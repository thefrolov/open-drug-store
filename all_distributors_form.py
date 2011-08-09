# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from all_distributors_form_ui import Ui_all_distributors_form
from new_distributor_form import NewDistributorForm

class AllDistributorsWindow(QFrame):
	def __init__(self):
		QFrame.__init__(self)
		self.ui = Ui_all_distributors_form()
	
		self.ui.setupUi(self)
		self.drawTable()
		QObject.connect(self.ui.add_distributor_btn, SIGNAL("clicked()"), self.showNewDistributorForm)
		QObject.connect(self.ui.del_distributor_btn, SIGNAL("clicked()"), self.delDistributor)
	
	def drawTable(self):
		self.distributors = query_session.query(Distributor).all()
		self.ui.distributors_table.clear()
		self.ui.distributors_table.setRowCount(1)
		self.ui.distributors_table.setColumnCount(2)
		self.ui.distributors_table.setHorizontalHeaderLabels([QString.fromUtf8('Номер'), QString.fromUtf8('Название')])
		
		for distributor in self.distributors:
			data = []
			data.append(str(distributor.id))
			data.append(distributor.name)
			for i in range(0,2):	
				tableitem = QTableWidgetItem()
				tableitem.setText(data[i])
				tableitem.font = QFont("Arial", 10)
				tableitem.font.setBold(True)
				tableitem.textcolor = QColor("black")
				self.ui.distributors_table.setItem(self.ui.distributors_table.rowCount() - 1,i,tableitem)
			self.ui.distributors_table.setRowCount(self.ui.distributors_table.rowCount()+1)
		self.ui.distributors_table.resizeColumnsToContents()
				
	def showNewDistributorForm(self):
		self.new_distributor_form = NewDistributorForm(self)
		QObject.connect(self.new_distributor_form, SIGNAL("distributorAdded()"), self.drawTable)
		self.new_distributor_form.setWindowModality(2)
		self.new_distributor_form.show()
		
	def delDistributor(self):
		row = self.ui.distributors_table.currentRow()
		id_for_delete = int(self.ui.distributors_table.item(row, 0).text())
		distributor_for_delete = query_session.query(Distributor).filter_by(id=id_for_delete).one()
		s = Session()
		s.delete(distributor_for_delete)
		s.commit()
		s.close
		self.drawTable()