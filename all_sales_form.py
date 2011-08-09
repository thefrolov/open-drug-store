# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str
from sale_form import SaleWindow

# Import the compiled UI module
sys.path.append("ui")
from all_sales_form_ui import Ui_all_sales_form
from new_drug_form import NewDrugForm

class AllSalesWindow(QFrame):
	def __init__(self, mdi):
		QFrame.__init__(self)
		self.ui = Ui_all_sales_form()
		
		self.ui.setupUi(self)
		self.mdi = mdi
		self.sales = query_session.query(Sale).all()
		QObject.connect(self.ui.sales_table, SIGNAL("cellDoubleClicked(int, int)"), self.showSaleForm)
		QObject.connect(self.ui.close_btn, SIGNAL("clicked()"), self.closeme)
		self.setWindowTitle(QString.fromUtf8('Список отпускных накладных'))
		self.drawTable()
		
	def drawTable(self):
		#self.drugs = self.getDrugs(self.ui.filter_text.text())
		self.ui.sales_table.clear()
		self.ui.sales_table.setRowCount(1)
		self.ui.sales_table.setColumnCount(5)
		self.ui.sales_table.setHorizontalHeaderLabels([QString.fromUtf8('Номер'), QString.fromUtf8('Получатель'), QString.fromUtf8('Дата'), QString.fromUtf8('Количество позиций'), QString.fromUtf8('Сумма')])
		self.ui.sales_table.resizeColumnsToContents()
		
		for sale in self.sales:
			data = []
			data.append(str(sale.id))
			if (sale.m_organisation_id == None):
				data.append(QString.fromUtf8(repr(sale.getReciever())))
			else:
				data.append(sale.m_organisation.name)
				#data.append(sale.m_organisation.name)
			data.append(sale.create_date.strftime("%d.%m.%Y"))
			data.append(str(len(sale.maps)))
			summ = 0
			for m in sale.maps:
				summ = summ + m.count*m.drug.price
			data.append(str(summ))
			for i in range(0,5):	
				tableitem = QTableWidgetItem()
				tableitem.setText(data[i])
				tableitem.font = QFont("Arial", 10)
				tableitem.font.setBold(True)
				tableitem.textcolor = QColor("black")
				if not sale.accepted:
					tableitem.setBackgroundColor(QColor('Yellow'))
				self.ui.sales_table.setItem(self.ui.sales_table.rowCount() - 1,i,tableitem)
			self.ui.sales_table.setRowCount(self.ui.sales_table.rowCount()+1)
		self.ui.sales_table.resizeColumnsToContents()
		
		
	def showSaleForm(self, row, col):
		saleId = int(self.ui.sales_table.item(row, 0).text())
		sale = query_session.query(Sale).filter_by(id=saleId).one()
		self.sale_widget = self.mdi.addSubWindow(SaleWindow(sale))
		self.sale_widget.show()
		
	def closeme(self):
		self.parent().close()