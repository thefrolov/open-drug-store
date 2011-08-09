# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from new_distributor_form_ui import Ui_new_distributor_form


class NewDistributorForm(QFrame):
	def __init__(self, parent):
		QFrame.__init__(self)
		self.ui = Ui_new_distributor_form()
		self.ui.setupUi(self)
		self.parent = parent
		self.setWindowTitle(QString.fromUtf8('Добавить нового поставщика'))
		QObject.connect(self.ui.ok_btn, SIGNAL("clicked()"), self.addDistributor)
		
	def addDistributor(self):
		distributor = Distributor(self.ui.distributor_name.text())
		s = Session()
		s.add(distributor)
		s.commit()
		s.close()
		#self.parent.distributors = session.query(Distributor).all()
		#self.parent.drawCombo(self.parent.ui.distributor_combo,self.parent.distributors)
		
		#	убрать вот это ^
		
		self.emit(SIGNAL("distributorAdded()"))
		self.close()