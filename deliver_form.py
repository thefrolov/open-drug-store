# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str
from datetime import date
# Import the compiled UI module
sys.path.append("ui")
from deliver_form_ui import Ui_deliver_form
from add_drug_form import AddDrugForm
from new_distributor_form import NewDistributorForm
from new_financing_form import NewFinancingForm
from time import strftime

from appy.pod.renderer import Renderer
from os import popen, path
class DeliverWindow(QFrame):
	
	def initForm(self):
		QFrame.__init__(self)
		self.ui = Ui_deliver_form()
		self.ui.setupUi(self)
		
		self.ui.distributor_combo.setEditable(False)
		self.drawDistributorCombo()
		self.drawFinancingCombo()
		QObject.connect(self.ui.tableWidget, SIGNAL("cellDoubleClicked(int, int)"), self.showAddDrugForm)
		QObject.connect(self.ui.save_close_btn, SIGNAL("clicked()"), self.saveAcceptDeliver)
		QObject.connect(self.ui.save_btn, SIGNAL("clicked()"), self.saveDeliver)
		QObject.connect(self.ui.print_bill_btn, SIGNAL("clicked()"), self.createReport)
		QObject.connect(self.ui.close_btn, SIGNAL("clicked()"), self.closeme)
	
	def initNewDeliver(self):
		self.deliver = Deliver()
		self.deliver.create_date = date.today()
		self.ui.bill_number_date.setText(QString.fromUtf8(repr(self.deliver)))
		self.ui.deliver_date.setText(QString.fromUtf8(self.deliver.create_date.strftime("%d.%m.%Y")))
		self.drawTable()
		
		
	def __init__(self,deliver=None):
		self.initForm()
		if deliver == None:
			self.initNewDeliver()
		else:
			self.deliver = deliver
			self.ui.bill_number_date.setText(QString.fromUtf8(repr(self.deliver)))
			self.ui.deliver_date.setText(self.deliver.deliver_date.strftime("%d.%m.%Y"))
			self.ui.distributor_combo.setCurrentIndex(self.ui.distributor_combo.findText(self.deliver.distributor.name))
			self.ui.financing_combo.setCurrentIndex(self.ui.financing_combo.findText(self.deliver.financing.name))
			self.drawTable()
			
			if self.deliver.accepted:
				self.ui.save_btn.setDisabled(True)
				self.ui.save_close_btn.setDisabled(True)
				self.ui.distributor_combo.setDisabled(True)
				self.ui.financing_combo.setDisabled(True)
				self.ui.deliver_date.setDisabled(True)
	def drawTable(self):
		self.ui.tableWidget.clear()
		self.ui.tableWidget.setRowCount(1)
		self.ui.tableWidget.setColumnCount(7)
		self.ui.tableWidget.setHorizontalHeaderLabels([QString.fromUtf8('ИД'), QString.fromUtf8('Название препарата'), QString.fromUtf8('Производитель'), QString.fromUtf8('Серийный номер'), QString.fromUtf8('Годен до'), QString.fromUtf8('Цена'),QString.fromUtf8('Количество')])
		self.summ = 0
		for m in self.deliver.maps:
			if not m.count == 0:
				data = []
				data.append(str(m.drug.id))
				data.append(QString.fromUtf8(m.drug.name()))
				data.append(m.drug.manufacter.name)
				data.append(str(m.drug.serial))
				data.append(m.drug.best_before.strftime("%d.%m.%Y"))
				data.append(str(m.drug.price))
				data.append(str(m.count))
			
				self.summ = self.summ + m.count*m.drug.price
				for i in range(0,7):	
					tableitem = QTableWidgetItem()
					tableitem.setText(data[i])
					tableitem.font = QFont("Arial", 10)
					tableitem.font.setBold(True)
					tableitem.textcolor = QColor("black")
					tableitem.setBackgroundColor(QColor('White'))
					self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1,i,tableitem)
				self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount()+1)
			else:
				self.deliver.maps.remove(m)
		self.ui.label_3.setText(QString.fromUtf8("Всего лс на сумму " + str(self.summ) + "р."))
		self.ui.tableWidget.resizeColumnsToContents()		

	def drawDistributorCombo(self):
		distributors = query_session.query(Distributor).all()
		self.ui.distributor_combo.clear()		
		for item in distributors:
			self.ui.distributor_combo.addItem(item.name)
		
		self.ui.distributor_combo.addItem(QString.fromUtf8('Новый поставщик'))
		QObject.connect(self.ui.distributor_combo, SIGNAL("currentIndexChanged(int)"), self.setDistributor)
		self.setDistributor(0)
		
	def drawFinancingCombo(self):
		fin = query_session.query(Financing).all()
		self.ui.financing_combo.clear()
		
		for item in fin:
			self.ui.financing_combo.addItem(item.name)
		
		self.ui.financing_combo.addItem(QString.fromUtf8('Новый источник финансирования'))
		QObject.connect(self.ui.financing_combo, SIGNAL("currentIndexChanged(int)"), self.setFinancing)
		self.setFinancing(0)


	def showAddDrugForm(self, row, col):
		if row == self.ui.tableWidget.rowCount() - 1:
			self.add_drug_form = AddDrugForm(self)
			self.add_drug_form.setWindowModality(2)
			QObject.connect(self.add_drug_form.count_form, SIGNAL("drugAdded()"), self.drawTable)
			self.add_drug_form.showMaximized()
			

	def saveAcceptDeliver(self):
		self.deliver.accepted = True
		self.saveDeliver()
		
	def saveDeliver(self):
		self.deliver.deliver_date = _date_from_str(self.ui.deliver_date.text())
		self.deliver.distributor = self.distributor
		self.deliver.financing = self.financing
		s = Session()
		s.add(self.deliver)
		s.commit()
		s.close()
		
		self.parent().close()
	
	
	def setDistributor(self,num):
		if (num < self.ui.distributor_combo.count() - 1):
			distributor = query_session.query(Distributor).filter_by(name=unicode(self.ui.distributor_combo.itemText(num))).one()
			self.distributor = distributor
		else:
			self.new_distributor_form = NewDistributorForm(self)
			self.new_distributor_form.setWindowModality(2)
			QObject.connect(self.new_distributor_form, SIGNAL("distributorAdded()"), self.drawTable)
			QObject.connect(self.new_distributor_form, SIGNAL("distributorAdded()"), self.drawDistributorCombo)	
			self.new_distributor_form.show()
	
	def setFinancing(self,num):
		if (num < self.ui.financing_combo.count() - 1):
			financing = query_session.query(Financing).filter_by(name=unicode(self.ui.financing_combo.itemText(num))).one()
			self.financing = financing
		else:
			self.new_financing_form = NewFinancingForm(self)
			self.new_financing_form.setWindowModality(2)
			QObject.connect(self.new_financing_form, SIGNAL("financingAdded()"), self.drawTable)
			QObject.connect(self.new_financing_form, SIGNAL("financingAdded()"), self.drawFinancingCombo)	
			self.new_financing_form.show()
			
	
	def createReport(self):
		fileName = '%sdeliver%d.pdf' % ('reports/', self.deliver.id)
		if path.exists(fileName):
			os.popen('evince %s' % fileName)
		else:
			opts = {'deliver': self.deliver}
			renderer = Renderer('appy/templates/deliver.odt', opts, fileName)
			renderer.run()
			
		os.popen('evince %s' % fileName)
		
	def closeme(self):
		self.parent().close()