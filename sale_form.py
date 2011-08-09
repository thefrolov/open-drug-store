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
from sale_form_ui import Ui_sale_form
from add_drug_form import AddDrugForm
from new_recipe_form import NewRecipeForm
from new_medorg_form import NewMedorgForm
from time import strftime


class SaleWindow(QFrame):
	def initForm(self):
		QFrame.__init__(self)
		self.ui = Ui_sale_form()
		self.ui.setupUi(self)
		self.s = Session()
		QObject.connect(self.ui.tableWidget, SIGNAL("cellDoubleClicked(int, int)"), self.showAddDrugForm)
		QObject.connect(self.ui.reciever_btn, SIGNAL("clicked()"), self.setReciever)
		QObject.connect(self.ui.reciever_combo, SIGNAL("currentIndexChanged(int)"), self.changeReciever)
		QObject.connect(self.ui.save_close_btn, SIGNAL("clicked()"), self.acceptSale)
		QObject.connect(self.ui.save_btn, SIGNAL("clicked()"), self.saveSale)
		QObject.connect(self.ui.financing_combo, SIGNAL("currentIndexChanged(int)"), self.setFinancing)
		QObject.connect(self.ui.close_btn, SIGNAL("clicked()"), self.closeme)
		
		self.setWindowTitle(QString.fromUtf8('Создание расходной накладной'))
		self.drawFinancingCombo()
		
		self.ui.m_org_combo = QComboBox(self)
		self.ui.gridLayout.addWidget(self.ui.m_org_combo, 4, 2, 1, 1)
		self.ui.m_org_combo.setVisible(False)
		
		QObject.connect(self.ui.m_org_combo, SIGNAL("currentIndexChanged(int)"), self.newMedorg)
	def initNewSale(self):
		self.sale = Sale()
#financing
		self.sale.financing = self.financing
		self.sale.create_date = date.today()
		
	def __init__(self,sale = None):
		self.initForm()
		if sale == None:
			self.initNewSale()
		else:
			self.sale = sale
		self.drawTable()
		self.drawControls()
			
	
	def drawControls(self):
		self.ui.financing_combo.setCurrentIndex(self.ui.financing_combo.findText(self.sale.financing.name))
		self.ui.reciever_label.setText(QString.fromUtf8(repr(self.sale.getReciever())))
		if self.sale.m_organisation == None:
			self.ui.reciever_btn.setVisible(True)
			self.ui.m_org_combo.setVisible(False)
		else:
			self.ui.reciever_btn.setVisible(False)
			self.ui.m_org_combo.setVisible(True)
			self.ui.m_org_combo.setCurrentIndex(2)
			self.drawMedorgCombo()
			self.ui.m_org_combo.setCurrentIndex(self.ui.m_org_combo.findText(self.sale.m_organisation.name))

		self.ui.bill_number_date.setText(QString.fromUtf8(repr(self.sale)))
		self.ui.financing_combo.setDisabled(self.sale.accepted)
		self.ui.reciever_btn.setDisabled(self.sale.accepted)
		self.ui.m_org_combo.setDisabled(self.sale.accepted)
		self.ui.reciever_combo.setDisabled(self.sale.accepted)
		self.ui.save_close_btn.setDisabled(self.sale.accepted)
		self.ui.save_btn.setDisabled(self.sale.accepted)
		
	def drawTable(self):
		self.ui.tableWidget.clear()
		self.ui.tableWidget.setColumnCount(7)
		self.ui.tableWidget.setRowCount(1)
		self.ui.tableWidget.setHorizontalHeaderLabels([QString.fromUtf8('ИД'), QString.fromUtf8('Название препарата'), QString.fromUtf8('Производитель'), QString.fromUtf8('Серийный номер'), QString.fromUtf8('Годен до'), QString.fromUtf8('Цена'),QString.fromUtf8('Количество')])
		self.summ = 0
		for m in self.sale.maps:
			data = []
			data.append(str(m.drug.id))
			data.append(QString.fromUtf8(m.drug.name()))
			data.append(QString.fromUtf8(m.drug.manufacter.name))
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
		self.ui.label_3.setText(QString.fromUtf8("Всего лс на сумму " + str(self.summ) + "р."))
		self.ui.tableWidget.resizeColumnsToContents()
		
	def drawFinancingCombo(self):
		fin = query_session.query(Financing).all()
		self.ui.financing_combo.clear()
		
		for item in fin:
			self.ui.financing_combo.addItem(item.name)
		self.setFinancing(0)
		
	def setFinancing(self,num):
		financing = query_session.query(Financing).filter_by(name=unicode(self.ui.financing_combo.itemText(num))).one()
		self.financing = financing
		print self.financing

	def changeReciever(self, res):
		if (res == 0):
			self.ui.reciever_btn.setText(QString.fromUtf8('Рецепт'))
			self.ui.reciever_btn.setVisible(True)
			self.ui.m_org_combo.setVisible(False)
		elif (res == 1):
			#self.ui.reciever_btn.setText(QString.fromUtf8('Мед. организация'))
			self.ui.m_org_combo.setVisible(True)
			self.ui.reciever_btn.setVisible(False)
			self.drawMedorgCombo()

	def showNewRecipeForm(self):
		self.new_recipe_form = NewRecipeForm(self)
		self.new_recipe_form.setWindowModality(2)
		self.new_recipe_form.show()
		self.ui.reciever_combo.setDisabled(True)

	def showAddDrugForm(self, row, col):
		if row == self.ui.tableWidget.rowCount() - 1:
			self.add_drug_form = AddDrugForm(self)
			self.add_drug_form.setWindowModality(2)
			QObject.connect(self.add_drug_form.count_form, SIGNAL("drugAdded()"), self.drawTable)
			self.add_drug_form.show()
			
			
	def acceptSale(self):
		self.sale.accepted = True
		self.saveSale()
	
	def saveSale(self):
		self.s.add(self.sale)
		self.s.commit()
		self.s.close()
		self.closeme()
		
	def closeme(self):
		self.parent().close()
		
	def setReciever(self):
		if self.ui.reciever_combo.currentIndex() == 0:
			self.showNewRecipeForm()
	
	
	def drawMedorgCombo(self):
		combo = self.ui.m_org_combo
		items = query_session.query(M_organisation).all()
		combo.clear()		
		for item in items:
			combo.addItem(QString.fromUtf8(repr(item)))
		
		combo.addItem(QString.fromUtf8('Добавить'))
		combo.setCurrentIndex(0)
		
	def newMedorg(self,num):
		if (num >= self.ui.m_org_combo.count() - 1) and (self.ui.m_org_combo.count() > 1):
			self.new_medorg_form = NewMedorgForm()
			self.new_medorg_form.setWindowModality(2)
			QObject.connect(self.new_medorg_form, SIGNAL("medorgAdded()"), self.drawMedorgCombo)
			self.new_medorg_form.show()
		else:
			self.sale.m_organisation = query_session.query(M_organisation).filter_by(name=str(self.ui.m_org_combo.currentText().toUtf8())).one()
			#self.sale.recipe = None
		