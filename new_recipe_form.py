# -*- coding: utf-8 -*-
import os,sys

# Import Qt modules
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from model import *
from utils import _date_from_str, parseStr

# Import the compiled UI module
sys.path.append("ui")
from new_recipe_form_ui import Ui_new_recipe_form
from new_patient_form import NewPatientForm
from new_medorg_form import NewMedorgForm
from new_doctor_form import NewDoctorForm
#from new_ill_form import NewIllForm

class NewRecipeForm(QFrame):
	def __init__(self,parent):
		QFrame.__init__(self)
		self.ui = Ui_new_recipe_form()
		self.ui.setupUi(self)
		self.parent = parent
		
		self.recipe = Recipe()
		self.setWindowTitle(QString.fromUtf8('Новый рецепт'))
		self.ui.recipe_num.setText(QString.fromUtf8('Рецепт №'+str(self.recipe.id)))
		
		
		
		
		self.drawPatientCombo()
		self.drawMedorgCombo()
		self.drawDoctorCombo()
		self.drawIllCombo()
		
		QObject.connect(self.ui.ok_btn, SIGNAL("clicked()"), self.addRecipe)
		
		QObject.connect(self.ui.patient_combo, SIGNAL("currentIndexChanged(int)"), self.newPatient)
		QObject.connect(self.ui.m_org_combo, SIGNAL("currentIndexChanged(int)"), self.newMedorg)
		QObject.connect(self.ui.doctor_combo, SIGNAL("currentIndexChanged(int)"), self.newDoctor)
		#QObject.connect(self.ui.ill_combo, SIGNAL("currentIndexChanged(int)"), self.newIll)
		
	
	def addRecipe(self):
		firstname, lastname = parseStr(str(self.ui.patient_combo.currentText().toUtf8()),' ')
		patient = query_session.query(Patient).filter_by(first_name=firstname).filter_by(last_name=lastname).one()
		m_organisation = query_session.query(M_organisation).filter_by(name=str(self.ui.m_org_combo.currentText().toUtf8())).one()
		
		firstname, lastname = parseStr(str(self.ui.doctor_combo.currentText().toUtf8()),' ')
		doctor = query_session.query(Doctor).filter_by(first_name=firstname).filter_by(last_name=lastname).one()
		ill = query_session.query(Ill).filter_by(name=str(self.ui.ill_combo.currentText().toUtf8())).one()
		self.recipe.sale = self.parent.sale
		
		self.recipe.patient = patient
		self.recipe.m_organisation = m_organisation
		self.recipe.doctor = doctor
		self.recipe.ill = ill
		self.parent.s.add(self.recipe)
		self.parent.ui.reciever_label.setText(QString.fromUtf8('Рецепт №%i для %s' % (self.recipe.id,repr(self.recipe.patient))))
		self.parent.sale.m_organisation = None
		#self.parent.s.commit()
		#self.parent.s.close()
		#self.emit(SIGNAL("recipeAdded()"))
		self.close()


	def drawCombo(self,combo,items):
		combo.clear()		
		for item in items:
			combo.addItem(QString.fromUtf8(repr(item)))
		
		combo.addItem(QString.fromUtf8('Добавить'))
		combo.setCurrentIndex(0)
		
	
	def drawPatientCombo(self):
		self.patients = query_session.query(Patient).all()
		self.drawCombo(self.ui.patient_combo, self.patients)
		
	def drawMedorgCombo(self):
		self.m_organisations = query_session.query(M_organisation).all()
		self.drawCombo(self.ui.m_org_combo, self.m_organisations)
		
	def drawDoctorCombo(self):
		self.doctors = query_session.query(Doctor).all()
		self.drawCombo(self.ui.doctor_combo, self.doctors)
		
	def drawIllCombo(self):
		self.ills = query_session.query(Ill).all()
		self.drawCombo(self.ui.ill_combo, self.ills)
		
		
	def newPatient(self,num):
		if (num >= self.ui.patient_combo.count() - 1):
			self.new_patient_form = NewPatientForm()
			self.new_patient_form.setWindowModality(2)
			QObject.connect(self.new_patient_form, SIGNAL("patientAdded()"), self.drawPatientCombo)
			self.new_patient_form.show()
			
	def newMedorg(self,num):
		if (num >= self.ui.m_org_combo.count() - 1):
			self.new_medorg_form = NewMedorgForm()
			self.new_medorg_form.setWindowModality(2)
			QObject.connect(self.new_medorg_form, SIGNAL("medorgAdded()"), self.drawMedorgCombo)
			self.new_medorg_form.show()
			
	def newDoctor(self,num):
		if (num >= self.ui.doctor_combo.count() - 1):
			self.new_doctor_form = NewDoctorForm()
			self.new_doctor_form.setWindowModality(2)
			QObject.connect(self.new_doctor_form, SIGNAL("doctorAdded()"), self.drawDoctorCombo)
			self.new_doctor_form.show()
	
#	def newIll(self,num):
#		if (num >= self.ui.ill_combo.count() - 1):
#			self.new_ill_form = NewIllForm()
#			self.new_ill_form .setWindowModality(2)
#			QObject.connect(self.new_ill_form , SIGNAL("illAdded()"), self.drawIllCombo)
#			self.new_doctor_form.show()