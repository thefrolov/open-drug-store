# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 


# Import the compiled UI module
sys.path.append("ui")
from main_window_ui import Ui_MainWindow

from model import *


from deliver_form import DeliverWindow
from sale_form import SaleWindow
from all_drugs_form import AllDrugsWindow
from all_delivers_form import AllDeliversWindow
from all_sales_form import AllSalesWindow
from all_patients_form import AllPatientsWindow
from all_distributors_form import AllDistributorsWindow
from all_medorg_form import AllMedorgWindow
from all_doctors_form import AllDoctorsWindow
from all_manufacters_form import AllManufactersWindow
from all_ills_form import AllIllsWindow
from all_recipes_form import AllRecipesWindow

# Create a class for our main window
class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.mdiArea.setOption(QMdiArea.DontMaximizeSubWindowOnActivation, True)
	@pyqtSlot(int)
	def show_child_window(self,widget_number):
		if widget_number == 0:
			self.deliver_widget = DeliverWindow()
			self.deliver_widget = self.ui.mdiArea.addSubWindow(self.deliver_widget)
			self.deliver_widget.showMaximized()
		elif widget_number == 1:
			self.sale_widget = SaleWindow()
			self.ui.mdiArea.addSubWindow(self.sale_widget)
			self.sale_widget.showMaximized()
			
		elif widget_number == 2:
			self.drugs_widget = AllDrugsWindow()
			self.ui.mdiArea.addSubWindow(self.drugs_widget)
			self.drugs_widget.showMaximized()
		
		elif widget_number == 3:
			self.delivers_widget = AllDeliversWindow(self.ui.mdiArea)
			self.ui.mdiArea.addSubWindow(self.delivers_widget)
			self.delivers_widget.showMaximized()
		elif widget_number == 4:
			self.sales_widget = AllSalesWindow(self.ui.mdiArea)
			self.ui.mdiArea.addSubWindow(self.sales_widget)
			self.sales_widget.showMaximized()
		elif widget_number == 5:
			self.patients_widget = AllPatientsWindow()
			self.ui.mdiArea.addSubWindow(self.patients_widget)
			self.patients_widget.showMaximized()
		elif widget_number == 6:
			self.distributors_widget = AllDistributorsWindow()
			self.ui.mdiArea.addSubWindow(self.distributors_widget)
			self.distributors_widget.showMaximized()
		elif widget_number == 7:
			self.medorg_widget = AllMedorgWindow()
			self.ui.mdiArea.addSubWindow(self.medorg_widget)
			self.medorg_widget.showMaximized()
		elif widget_number == 8:
			self.doctors_widget = AllDoctorsWindow()
			self.doctors_widget = self.ui.mdiArea.addSubWindow(self.doctors_widget)
			self.doctors_widget.showMaximized()
		elif widget_number == 9:
			self.manufacters_widget = AllManufactersWindow()
			self.manufacters_widget = self.ui.mdiArea.addSubWindow(self.manufacters_widget)
			self.manufacters_widget.showMaximized()
			#QObject.connect(self.manufacters_widget, SIGNAL("closed()"), self.ui.mdiArea.removeSubWindow)
			
		elif widget_number == 10:
			self.ills_widget = AllIllsWindow()
			self.ills_widget= self.ui.mdiArea.addSubWindow(self.ills_widget)
			self.ills_widget.showMaximized()
		elif widget_number == 11:
			self.recipes_widget = AllRecipesWindow()
			self.recipes_widget = self.ui.mdiArea.addSubWindow(self.recipes_widget)
			self.recipes_widget.showMaximized()