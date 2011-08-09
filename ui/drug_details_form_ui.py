# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drug_details_form.ui'
#
# Created: Wed May 18 22:36:35 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DrugDetailsForm(object):
    def setupUi(self, DrugDetailsForm):
        DrugDetailsForm.setObjectName(_fromUtf8("DrugDetailsForm"))
        DrugDetailsForm.resize(590, 334)
        self.gridLayout = QtGui.QGridLayout(DrugDetailsForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.DetailsTable = QtGui.QTableWidget(DrugDetailsForm)
        self.DetailsTable.setObjectName(_fromUtf8("DetailsTable"))
        self.DetailsTable.setColumnCount(0)
        self.DetailsTable.setRowCount(0)
        self.gridLayout.addWidget(self.DetailsTable, 0, 0, 1, 1)

        self.retranslateUi(DrugDetailsForm)
        QtCore.QMetaObject.connectSlotsByName(DrugDetailsForm)

    def retranslateUi(self, DrugDetailsForm):
        DrugDetailsForm.setWindowTitle(QtGui.QApplication.translate("DrugDetailsForm", "Form", None, QtGui.QApplication.UnicodeUTF8))

