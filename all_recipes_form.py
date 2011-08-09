# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str

# Import the compiled UI module
sys.path.append("ui")
from all_recipes_form_ui import Ui_all_recipes_form

from appy.pod.renderer import Renderer
from os import popen, path
class AllRecipesWindow(QFrame):
	def __init__(self):
		QFrame.__init__(self)
		self.ui = Ui_all_recipes_form()
		self.ui.setupUi(self)
		QObject.connect(self.ui.close_btn, SIGNAL("clicked()"), self.closeme)
		QObject.connect(self.ui.print_report_btn, SIGNAL("clicked()"), self.createReport)
		self.setWindowTitle(QString.fromUtf8('Реестр отпущеных рецептов'))
 		self.drawTable()
 		
	def drawTable(self):
		self.recipes = query_session.query(Recipe).all()
		self.ui.recipes_table.clear()
		self.ui.recipes_table.setRowCount(1)
		self.ui.recipes_table.setColumnCount(5)
		self.ui.recipes_table.setHorizontalHeaderLabels([QString.fromUtf8('Номер'), QString.fromUtf8('Пациент'), QString.fromUtf8('Мед. организация'), QString.fromUtf8('Лечащий врач'), QString.fromUtf8('Заболевание')])
		self.ui.recipes_table.resizeColumnsToContents()
		
		for recipe in self.recipes:
			data = []
			data.append(str(recipe.id))
			data.append(QString.fromUtf8(repr(recipe.patient)))
			data.append(QString.fromUtf8(repr(recipe.m_organisation)))
			data.append(QString.fromUtf8(repr(recipe.doctor)))
			data.append(QString.fromUtf8(repr(recipe.ill)))
			
			for i in range(0,5):	
				tableitem = QTableWidgetItem()
				tableitem.setText(data[i])
				tableitem.font = QFont("Arial", 10)
				tableitem.font.setBold(True)
				tableitem.textcolor = QColor("black")
				self.ui.recipes_table.setItem(self.ui.recipes_table.rowCount() - 1,i,tableitem)
			self.ui.recipes_table.setRowCount(self.ui.recipes_table.rowCount()+1)
		self.ui.recipes_table.resizeColumnsToContents()
		
		
	def createReport(self):
		fileName = '%srecipe.pdf' % ('reports/')
		if path.exists(fileName):
			os.popen('evince %s' % fileName)
		else:
			opts = {'recipes': self.recipes}
			renderer = Renderer('appy/templates/recipes.odt', opts, fileName)
			renderer.run()
			
		os.popen('evince %s' % fileName)
	
	def closeme(self):
		self.parent().close()