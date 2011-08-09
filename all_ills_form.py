# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from all_ills_form_ui import Ui_all_ills_form
#from new_distributor_form import NewDistributorForm

class AllIllsWindow(QFrame):
	def __init__(self):
		QFrame.__init__(self)
		self.ui = Ui_all_ills_form()
	
		self.ui.setupUi(self)
		self.drawTable()
		QObject.connect(self.ui.close_btn, SIGNAL("clicked()"), self.closeme)
	
	def drawTable(self):
		self.ills = query_session.query(Ill).all()
		self.ui.ills_table.clear()
		self.ui.ills_table.setRowCount(1)
		self.ui.ills_table.setColumnCount(2)
		self.ui.ills_table.setHorizontalHeaderLabels([QString.fromUtf8('Номер'), QString.fromUtf8('Название')])
		
		for ill in self.ills:
			data = []
			data.append(str(ill.id))
			data.append(ill.name)
			for i in range(0,2):	
				tableitem = QTableWidgetItem()
				tableitem.setText(data[i])
				tableitem.font = QFont("Arial", 10)
				tableitem.font.setBold(True)
				tableitem.textcolor = QColor("black")
				self.ui.ills_table.setItem(self.ui.ills_table.rowCount() - 1,i,tableitem)
			self.ui.ills_table.setRowCount(self.ui.ills_table.rowCount()+1)
		self.ui.ills_table.resizeColumnsToContents()

	def closeme(self):
		self.parent().close()