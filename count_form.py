# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from count_form_ui import Ui_count_form

class CountForm(QFrame):
	def __init__(self, parent):
		QFrame.__init__(self)
		self.ui = Ui_count_form()
		self.ui.setupUi(self)
		self.parent = parent
		if hasattr(parent.parent, 'deliver'):
			QObject.connect(self.ui.ok_btn, SIGNAL("clicked()"), self.sendCountForDeliver)
		else:
			QObject.connect(self.ui.ok_btn, SIGNAL("clicked()"), self.sendCountForSale)
		
	
	def sendCountForDeliver(self):
		self.parent.m.count = int(self.ui.lineEdit.text())
		self.parent.parent.deliver.maps.append(self.parent.m)
		#session.add(self.parent.parent.drug_deliver_map)
		#session.commit()
		self.emit(SIGNAL("drugAdded()"))
		self.close()



	def sendCountForSale(self):
		if (int(self.ui.lineEdit.text()) > self.parent.m.drug.count()):
			QMessageBox.information(self, QString.fromUtf8('Внимание'), QString.fromUtf8("На складе доступно %d" % self.parent.m.drug.count()), QMessageBox.Ok)
		else:
			self.parent.m.count = int(self.ui.lineEdit.text())
			self.parent.parent.sale.maps.append(self.parent.m)
			#session.add(self.parent.parent.drug_deliver_map)
			#session.commit()
			self.emit(SIGNAL("drugAdded()"))
			self.close()