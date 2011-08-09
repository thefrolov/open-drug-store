# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from add_drug_form_ui import Ui_add_drug_form
from count_form import CountForm
from new_drug_form import NewDrugForm

class AddDrugForm(QFrame):
	def __init__(self, parent):
		QFrame.__init__(self)
		self.ui = Ui_add_drug_form()
	
		self.ui.setupUi(self)
		QObject.connect(self.ui.filter_text, SIGNAL("textEdited(QString)"), self.drawTable)
		if hasattr(parent, 'deliver'):
			QObject.connect(self.ui.drugsTable, SIGNAL("cellDoubleClicked(int, int)"), self.setDrugForDeliver)
			self.fordeliver = True
		else:
			QObject.connect(self.ui.drugsTable, SIGNAL("cellDoubleClicked(int, int)"), self.setDrugForSale)
			self.fordeliver = False
			
		QObject.connect(self.ui.newDrugBtn, SIGNAL("clicked()"), self.showNewDrugForm)
		
		self.parent = parent
		self.count_form = CountForm(self)
        
		self.drawTable()

	def getDrugs(self, filter):
		if filter:
			drugs = query_session.query(Drug).filter(Drug.name.like('%'+str(filter.toUtf8())+'%'))
			
		else:
			drugs = query_session.query(Drug).all()
		result = []
			
	
	def drawTable(self):
		self.drugs = self.getDrugs(self.ui.filter_text.text())
		self.ui.drugsTable.clear()
		self.ui.drugsTable.setRowCount(0)
		self.ui.drugsTable.setColumnCount(7)
		self.ui.drugsTable.setHorizontalHeaderLabels([QString.fromUtf8('ИД'), QString.fromUtf8('Название препарата'), QString.fromUtf8('Производитель'), QString.fromUtf8('Серийный номер'), QString.fromUtf8('Годен до'), QString.fromUtf8('Цена'),QString.fromUtf8('Количество')])
		for drug in self.drugs:
			if drug.count() > 0 or self.fordeliver:
				self.ui.drugsTable.setRowCount(self.ui.drugsTable.rowCount()+1)
				data = []
				data.append(str(drug.id))
				data.append(QString.fromUtf8(drug.name()))
				data.append(QString.fromUtf8(drug.manufacter.name))
				data.append(str(drug.serial))
				data.append(str(drug.best_before))
				data.append(str(drug.price))
				data.append(str(drug.count()))
				for i in range(0,7):	
					tableitem = QTableWidgetItem()
					tableitem.setText(data[i])
					tableitem.font = QFont("Arial", 10)
					tableitem.font.setBold(True)
					tableitem.textcolor = QColor("black")
					tableitem.setBackgroundColor(QColor('White'))
					self.ui.drugsTable.setItem(self.ui.drugsTable.rowCount() - 1,i,tableitem)
		self.ui.drugsTable.resizeColumnsToContents()
	
	def setDrugForDeliver(self,i,j):
		#self.parent.drug_deliver_map = DrugDeliverMap(self.parent.deliver)
		selected_drug = query_session.query(Drug).filter_by(id=int(self.ui.drugsTable.item(i,0).text())).one()
#		self.parent.drug_deliver_map.drug = selected_drug
		self.m = DrugDeliverMap()
		self.m.drug = selected_drug
		self.count_form.setWindowModality(2)
		self.count_form.show()
	
	
	def setDrugForSale(self,i,j):
		#self.parent.drug_deliver_map = DrugDeliverMap(self.parent.deliver)
		selected_drug = query_session.query(Drug).filter_by(id=int(self.ui.drugsTable.item(i,0).text())).one()
#		self.parent.drug_deliver_map.drug = selected_drug
		self.m = DrugSaleMap()
		self.m.drug = selected_drug
		self.count_form.setWindowModality(2)
		self.count_form.show()
		
		
	def showNewDrugForm(self):
		self.new_drug_form = NewDrugForm()
		self.new_drug_form.setWindowModality(2)
		QObject.connect(self.new_drug_form, SIGNAL("drugCreated()"), self.drawTable)
		self.new_drug_form.show()