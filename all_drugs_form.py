# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from all_drugs_form_ui import Ui_all_drugs_form
from new_drug_form import NewDrugForm
from drug_details_form_ui import Ui_DrugDetailsForm

class AllDrugsWindow(QFrame):
	def __init__(self):
		QFrame.__init__(self)
		self.ui = Ui_all_drugs_form()
	
		self.ui.setupUi(self)	
		
		QObject.connect(self.ui.new_drug_btn, SIGNAL("clicked()"), self.showNewDrugForm)
		QObject.connect(self.ui.del_drug_btn, SIGNAL("clicked()"), self.delDrug)
		QObject.connect(self.ui.tableWidget, SIGNAL("cellDoubleClicked(int, int)"), self.showDetails)
		QObject.connect(self.ui.close_btn, SIGNAL("clicked()"), self.closeme)
		
		self.drugs = self.getDrugs(0)
		self.drawTable()
		self.setWindowTitle(QString.fromUtf8('Склад'))
	def getDrugs(self, name_filter):
		if name_filter:
			return query_session.query(Drug).filter_by(name = name_filter)
			#Session.close()
		else:
			return query_session.query(Drug)
			#Session.close()
			
	
	def drawTable(self):
		self.drugs = query_session.query(GeneralDrug).all()
		self.ui.tableWidget.clear()
		self.ui.tableWidget.setRowCount(0)
		self.ui.tableWidget.setColumnCount(4)
		self.ui.tableWidget.setHorizontalHeaderLabels([QString.fromUtf8('ИД'), QString.fromUtf8('Название препарата'), QString.fromUtf8('Количество'), QString.fromUtf8('Сумма')])
		self.summ = 0
		for drug in self.drugs:
			self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount()+1)
			data = []
			data.append(str(drug.id))
			data.append(drug.name)
			data.append(str(drug.count()))
			data.append(str(drug.summ()))
			self.summ = self.summ + drug.summ()
			for i in range(0,4):	
				tableitem = QTableWidgetItem()
				tableitem.setText(data[i])
				tableitem.font = QFont("Arial", 10)
				tableitem.font.setBold(True)
				tableitem.textcolor = QColor("black")
				tableitem.setBackgroundColor(QColor('White'))
				self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1,i,tableitem)
		self.ui.tableWidget.resizeColumnsToContents()	
		self.ui.label_3.setText(QString.fromUtf8("Всего лс на сумму " + str(self.summ) + "р."))	
				
	def showNewDrugForm(self):
		self.new_drug_form = NewDrugForm()
		self.new_drug_form.setWindowModality(2)
		#QObject.connect(self.new_drug_form, SIGNAL("drugCreated()"), self.drawTable)
		self.new_drug_form.show()
		
		
		
	def delDrug(self):
		row = self.ui.tableWidget.currentRow()
		id_for_delete = int(self.ui.tableWidget.item(row, 0).text())
		drug_for_delete = query_session.query(Drug).filter_by(id=id_for_delete).one()
		s = Session()
		s.delete(drug_for_delete)
		s.commit()
		s.close
		self.drawTable()
	
	def showDetails(self,i,j):
		self.t = QTableWidget(self)
		self.t.setRowCount(4)
		self.t.setColumnCount(4)
		self.ui.tableWidget.setCellWidget(i, j, self.t)
		
		
	def closeme(self):
		self.parent().close()
