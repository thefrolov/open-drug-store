# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from all_delivers_form_ui import Ui_all_delivers_form
from new_drug_form import NewDrugForm
from deliver_form import DeliverWindow

class AllDeliversWindow(QFrame):
	def __init__(self,mdi):
		QFrame.__init__(self)
		self.ui = Ui_all_delivers_form()
	
		self.ui.setupUi(self)
		self.delivers = query_session.query(Deliver).all()
		self.drawTable()
		self.mdi = mdi
		QObject.connect(self.ui.delivers_table, SIGNAL("cellDoubleClicked(int, int)"), self.showDeliverForm)
		QObject.connect(self.ui.close_btn, SIGNAL("clicked()"), self.closeme)
		self.setWindowTitle(QString.fromUtf8('Список приходных накладных'))
	def drawTable(self):
		#self.drugs = self.getDrugs(self.ui.filter_text.text())
		self.ui.delivers_table.clear()
		self.ui.delivers_table.setRowCount(1)
		self.ui.delivers_table.setColumnCount(5)
		self.ui.delivers_table.setHorizontalHeaderLabels([QString.fromUtf8('Номер'), QString.fromUtf8('Поставщик'), QString.fromUtf8('Дата'), QString.fromUtf8('Количество позиций'), QString.fromUtf8('Сумма')])
		self.ui.delivers_table.resizeColumnsToContents()
		
		for deliver in self.delivers:
			data = []
			data.append(str(deliver.id))
			data.append(deliver.distributor.name)
			data.append(str(deliver.create_date))
			data.append(str(len(deliver.maps)))
			summ = 0
			for m in deliver.maps:
				summ = summ + m.count*m.drug.price
			data.append(str(summ))
			for i in range(0,5):	
				tableitem = QTableWidgetItem()
				tableitem.setText(data[i])
				tableitem.font = QFont("Arial", 10)
				tableitem.font.setBold(True)
				tableitem.textcolor = QColor("black")
				if not deliver.accepted:
					tableitem.setBackgroundColor(QColor('Yellow'))
				self.ui.delivers_table.setItem(self.ui.delivers_table.rowCount() - 1,i,tableitem)
			self.ui.delivers_table.setRowCount(self.ui.delivers_table.rowCount()+1)
		self.ui.delivers_table.resizeColumnsToContents()
		
	def showDeliverForm(self, row, col):
		deliverId = int(self.ui.delivers_table.item(row, 0).text())
		deliver = query_session.query(Deliver).filter_by(id=deliverId).one()
		self.deliver_widget = DeliverWindow(deliver)
		self.deliver_widget = self.mdi.addSubWindow(self.deliver_widget)
		self.deliver_widget.showMaximized()
		self.mdi.setActiveSubWindow(self.deliver_widget)
	
	
	def closeme(self):
		self.parent().close()
