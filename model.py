# -*- coding: utf-8 -*-

import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker, scoped_session, create_session, backref, relationship, relation
from sqlalchemy import Table, Column, Integer, Float, Unicode, Date, MetaData, Boolean, String
from sqlalchemy.ext.associationproxy import association_proxy

import sys
#from sqlalchemy import *


Base = declarative_base()
engine = create_engine('postgresql+psycopg2://drugstore:drugstore@gonsal.es:30/drugstore', echo=True)

Session = scoped_session(sessionmaker(bind=engine))
		
query_session = Session()
		
		
class GeneralDrug(Base):
	__tablename__ = 'generaldrugs'

	id = Column(Integer, primary_key=True)
	name = Column(Unicode,nullable=False)
	
	def __init__(self,new_name):
		self.id = counters.generaldrugs
		counters.generaldrugs = counters.generaldrugs + 1
		self.name = new_name
		
	def count(self):
		result = 0
		for drug in self.drugs:
			for dmap in drug.delivermaps:
				result = result + dmap.count
			for smap in drug.salemaps:
				result = result - smap.count
		
		return result
	
	def summ(self):
		result = 0
		for drug in self.drugs:
			for dmap in drug.delivermaps:
				result = result + dmap.count*drug.price
			for smap in drug.salemaps:
				result = result - smap.count*drug.price
		
		return result
	
class Drug(Base):
	__tablename__ = 'drugs'
	id = Column(Integer, primary_key=True)
	general_drug_id = Column(Integer, ForeignKey('generaldrugs.id'), nullable=False)
	general_drug = relationship('GeneralDrug', backref=backref('drugs'))
	serial = Column(Unicode, nullable=False)
	manufacter_id = Column(Integer, ForeignKey('manufacters.id'), nullable=False)
	manufacter = relationship('Manufacter', backref=backref('drugs'))
	best_before = Column(Date, nullable=False)
	price = Column(Float, nullable=False)
	
	
	def __init__(self, new_name, manufacter, serial, best_before, price):
		self.id = counters.drugs
		counters.drugs = counters.drugs + 1
		
		gd = query_session.query(GeneralDrug).filter_by(name=new_name)
		if (gd.count() == 0):
			self.general_drug = GeneralDrug(new_name)
		else:
			self.general_drug = gd.one()
		self.manufacter = manufacter
		self.serial = int(serial)
		self.best_before = best_before
		self.price = price
		
	def __repr__(self):
		return '%s' % (self.name())	
		
	def count(self):
		result = 0
		for dmap in self.delivermaps:
			result = result + dmap.count
		for smap in self.salemaps:
			if smap.count:
				result = result - smap.count
		
		return result
		
	def name(self):
		return self.general_drug.name.encode('utf-8')
		

class DrugDeliverMap(Base):
	__tablename__ = 'drug_deliver_map'
	id = Column(Integer, primary_key=True)
	drug_id = Column(Integer, ForeignKey('drugs.id'), nullable=False)
	drug = relationship('Drug', backref=backref('delivermaps'))
	deliver_id = Column(Integer, ForeignKey('delivers.id'), nullable=False)
	count = Column(Integer, nullable=False)



class Deliver(Base):
	__tablename__ = 'delivers'

	id = Column(Integer, primary_key=True)
	create_date = Column(Date, nullable=False)
	deliver_date = Column(Date, nullable=False)
	distributor_id = Column(Integer,ForeignKey('distributors.id'))
	
	financing_id = Column(Integer, ForeignKey("financing.id"))
	financing = relationship('Financing', backref=backref('delivers'))
	
	distributor = relationship('Distributor', backref=backref('delivers'))
	accepted = Column(Boolean,default=False)
	maps = relationship('DrugDeliverMap', backref=backref('delivers'))
	
	
	def __init__(self):
		self.id = counters.delivers
		counters.delivers = counters.delivers + 1
		self.accepted = False
		
	def summ(self):
		summ = 0
		for m in self.maps:
			summ = summ + m.count*m.drug.price
		return summ
		
	def __repr__(self):
		return 'Накладная № ' + str(self.id) + ' от ' + self.create_date.strftime("%d.%m.%Y")
		




class Sale(Base):
	__tablename__ = 'sales'

	id = Column(Integer, primary_key=True)
	create_date = Column(Date, nullable=False)
	sale_date = Column(Date)
	financing_id = Column(Integer, ForeignKey("financing.id"), nullable=False)
	m_organisation_id = Column(Integer, ForeignKey("m_organisations.id"))
	accepted = Column(Boolean)
	financing = relationship('Financing', backref=backref('sales'))	
	
	m_organisation = relationship('M_organisation', backref=backref('sales'))
	maps = relationship('DrugSaleMap', backref=backref('sales'))
	
	def __init__(self):
		self.id = counters.sales
		counters.sales = counters.sales + 1
		self.accepted = False
	def __repr__(self):
		return 'Накладная № ' + str(self.id) + ' от ' + self.create_date.strftime("%d.%m.%Y")
	
	def getReciever(self):
		if (self.m_organisation != None):
			return self.m_organisation
		else:
			if len(self.recipe) > 0:
				return self.recipe[0].patient
			else:
				return None

class DrugSaleMap(Base):
	__tablename__ = 'drug_sale_map'
	id = Column(Integer, primary_key=True)
	drug_id = Column(Integer, ForeignKey("drugs.id"),nullable=False)
	sale_id = Column(Integer, ForeignKey("sales.id"),nullable=False)
	drug = relationship('Drug', backref=backref('salemaps'))
	count = Column(Integer, nullable=False)
	
	def __init__(self):
		#count = 0
		pass

class Distributor(Base):
	__tablename__ = 'distributors'

	id = Column(Integer, primary_key=True)
	name = Column(Unicode, nullable=False)
	
	def __init__(self,name):
		self.id = counters.distributors
		counters.distributors = counters.distributors + 1
		self.name = str(name.toUtf8())
		
		
class Financing(Base):
	__tablename__ = 'financing'
		
	id = Column(Integer, primary_key=True)
	name = Column(Unicode)
	
	def __init__(self,name):
		self.name = name

class Manufacter(Base):
	__tablename__ = 'manufacters'

	id = Column(Integer, primary_key=True)
	name = Column(Unicode, nullable=False)
	country = Column(Unicode, nullable=False)
		
	def __init__(self,name,country):
		self.id = counters.manufacters
		counters.drugs = counters.manufacters + 1
		self.name = name
		self.country = country



class BadDrug(Base):
	__tablename__ = 'bad_drugs'
	
	id = Column(Integer, primary_key=True)
	drug_id = Column(Integer, ForeignKey("drugs.id"),nullable=False)
	date = Column(Date, nullable=False)
	comment = Column(Unicode, nullable=False)



class MaxDrugPrice(Base):
	__tablename__ = 'max_drug_price'
		
	id = Column(Integer, primary_key=True)
	drug_id = Column(Integer, ForeignKey("drugs.id"),nullable=False)
	max_price = Column(Float, nullable=False)


class Doctor(Base):
	__tablename__ = 'doctors'
		
	id = Column(Integer, primary_key=True)
	first_name = Column(Unicode, nullable=False)
	last_name = Column(Unicode, nullable=False)
	m_organisation_id = Column(Integer, ForeignKey("m_organisations.id"),nullable=False)
	m_organisation = relationship('M_organisation', backref=backref('doctors'))
	
	
	def __init__(self,first_name,last_name):
		self.id = counters.doctors
		counters.doctors = counters.doctors + 1
		self.first_name = str(first_name.toUtf8())
		self.last_name = str(last_name.toUtf8())
		

	def __str__(self):
		return '%s %s' % (self.first_name.encode('utf-8'), self.last_name.encode('utf-8'))
		
	def __repr__(self):
		return '%s %s' % (self.first_name.encode('utf-8'), self.last_name.encode('utf-8'))
		
		

class M_organisation(Base):
	__tablename__ = 'm_organisations'
		
	id = Column(Integer, primary_key=True)
	name = Column(Unicode, nullable=False)
	
	def __init__(self):
		self.id = counters.mos
		counters.mos = counters.mos + 1
			
	def __str__(self):
		return '%s' % self.name.encode('utf-8')
		
	def __repr__(self):
		return '%s' % self.name.encode('utf-8')
		

class Patient(Base):
	__tablename__ = 'patients'
		
	id = Column(Integer, primary_key=True)
	first_name = Column(Unicode, nullable=False)
	last_name = Column(Unicode, nullable=False)
	birth_date= Column(Date, nullable=False)
	
	
	def __init__(self):
		self.id = counters.patients
		counters.patients = counters.patients + 1
		
	def __str__(self):
		return '%s %s' % (self.first_name.encode('utf-8'), self.last_name.encode('utf-8'))
		
	def __repr__(self):
		return '%s %s' % (self.first_name.encode('utf-8'), self.last_name.encode('utf-8'))
		
class Ill(Base):
	__tablename__ = 'ills'
		
	id = Column(Integer, primary_key=True)
	name = Column(Unicode, nullable=False)
	
	def __init__(self):
		self.id = counters.ills
		counters.ills = counters.ills + 1
	
	
	def __str__(self):
		return '%s' % self.name.encode('utf-8')
		
	def __repr__(self):
		return '%s' % self.name.encode('utf-8')
		
class Recipe(Base):
	__tablename__ = 'recipes'
		
	id = Column(Integer, primary_key=True)
	patient_id = Column(Integer, ForeignKey("patients.id"))
	patient = relationship('Patient', backref=backref('recipes'))
	
	m_organisation_id = Column(Integer, ForeignKey("m_organisations.id"))
	m_organisation = relationship('M_organisation', backref=backref('recipes'))
	
	doctor_id = Column(Integer, ForeignKey("doctors.id"))
	doctor = relationship('Doctor', backref=backref('recipes'))
	
	ill_id = Column(Integer, ForeignKey("ills.id"))
	ill = relationship('Ill', backref=backref('recipes'))
	
	sale_id = Column(Integer, ForeignKey("sales.id"))
	sale = relationship('Sale', backref=backref('recipe'))
	
	def __init__(self):
		self.id = counters.recipes
		counters.recipes = counters.recipes + 1
	
#Base.metadata.create_all(engine)



class Counters():
	generaldrugs = 0
	drugs = 0
	delivers = 0
	manufacters = 0
	distributors = 0
	sales = 0
	patients = 0
	mos = 0
	doctors = 0
	ills = 0
	recipes = 0
	def __init__(self):
		a = query_session.query(func.max(Drug.id)).one()
		if not (a[0] == None):
			self.drugs = int(a[0]) + 1
		
		a = query_session.query(func.max(Deliver.id)).one()
		if not (a[0] == None):
			self.delivers = int(a[0]) +1
			
		a = query_session.query(func.max(Manufacter.id)).one()
		if not (a[0] == None):
			self.manufacters = int(a[0]) +1
			
		a = query_session.query(func.max(Distributor.id)).one()
		if not (a[0] == None):
			self.distributors = int(a[0]) +1
			
		a = query_session.query(func.max(Sale.id)).one()
		if not (a[0] == None):
			self.sales = int(a[0]) +1
		
		a = query_session.query(func.max(Patient.id)).one()
		if not (a[0] == None):
			self.patients = int(a[0]) +1
			
		a = query_session.query(func.max(M_organisation.id)).one()
		if not (a[0] == None):
			self.mos = int(a[0]) +1
			
		a = query_session.query(func.max(Doctor.id)).one()
		if not (a[0] == None):
			self.doctors = int(a[0]) +1
			
			
		a = query_session.query(func.max(Ill.id)).one()
		if not (a[0] == None):
			self.ills = int(a[0]) + 1
			
		a = query_session.query(func.max(Recipe.id)).one()
		if not (a[0] == None):
			self.recipes = int(a[0]) + 1
			
		a = query_session.query(func.max(GeneralDrug.id)).one()
		if not (a[0] == None):
			self.generaldrugs = int(a[0]) + 1
			
counters = Counters()
