# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_drug_form.ui'
#
# Created: Tue May 24 16:55:01 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_add_drug_form(object):
    def setupUi(self, add_drug_form):
        add_drug_form.setObjectName(_fromUtf8("add_drug_form"))
        add_drug_form.resize(574, 360)
        self.gridLayout = QtGui.QGridLayout(add_drug_form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.drugsTable = QtGui.QTableWidget(add_drug_form)
        self.drugsTable.setObjectName(_fromUtf8("drugsTable"))
        self.drugsTable.setColumnCount(0)
        self.drugsTable.setRowCount(0)
        self.gridLayout.addWidget(self.drugsTable, 0, 0, 1, 3)
        self.label = QtGui.QLabel(add_drug_form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.filter_text = QtGui.QLineEdit(add_drug_form)
        self.filter_text.setObjectName(_fromUtf8("filter_text"))
        self.gridLayout.addWidget(self.filter_text, 1, 1, 1, 1)
        self.newDrugBtn = QtGui.QPushButton(add_drug_form)
        self.newDrugBtn.setObjectName(_fromUtf8("newDrugBtn"))
        self.gridLayout.addWidget(self.newDrugBtn, 1, 2, 1, 1)

        self.retranslateUi(add_drug_form)
        QtCore.QMetaObject.connectSlotsByName(add_drug_form)

    def retranslateUi(self, add_drug_form):
        add_drug_form.setWindowTitle(QtGui.QApplication.translate("add_drug_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.drugsTable.setSortingEnabled(True)
        self.label.setText(QtGui.QApplication.translate("add_drug_form", "Фильтр", None, QtGui.QApplication.UnicodeUTF8))
        self.newDrugBtn.setText(QtGui.QApplication.translate("add_drug_form", "Новое лс", None, QtGui.QApplication.UnicodeUTF8))

