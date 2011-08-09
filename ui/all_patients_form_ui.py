# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all_patients_form.ui'
#
# Created: Wed May  4 15:55:58 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_all_patients_form(object):
    def setupUi(self, all_patients_form):
        all_patients_form.setObjectName(_fromUtf8("all_patients_form"))
        all_patients_form.resize(626, 329)
        self.gridLayout = QtGui.QGridLayout(all_patients_form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.patients_table = QtGui.QTableWidget(all_patients_form)
        self.patients_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.patients_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.patients_table.setObjectName(_fromUtf8("patients_table"))
        self.patients_table.setColumnCount(0)
        self.patients_table.setRowCount(0)
        self.gridLayout.addWidget(self.patients_table, 0, 0, 1, 8)
        self.close_btn = QtGui.QPushButton(all_patients_form)
        self.close_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.close_btn.setObjectName(_fromUtf8("close_btn"))
        self.gridLayout.addWidget(self.close_btn, 1, 7, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.del_patient_btn = QtGui.QPushButton(all_patients_form)
        self.del_patient_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.del_patient_btn.setObjectName(_fromUtf8("del_patient_btn"))
        self.gridLayout.addWidget(self.del_patient_btn, 1, 5, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(all_patients_form)
        self.pushButton_3.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 1, 3, 1, 1)
        self.add_patient_btn = QtGui.QPushButton(all_patients_form)
        self.add_patient_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.add_patient_btn.setObjectName(_fromUtf8("add_patient_btn"))
        self.gridLayout.addWidget(self.add_patient_btn, 1, 4, 1, 1)

        self.retranslateUi(all_patients_form)
        QtCore.QObject.connect(self.close_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), all_patients_form.close)
        QtCore.QMetaObject.connectSlotsByName(all_patients_form)

    def retranslateUi(self, all_patients_form):
        all_patients_form.setWindowTitle(QtGui.QApplication.translate("all_patients_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.close_btn.setText(QtGui.QApplication.translate("all_patients_form", "Закрыть", None, QtGui.QApplication.UnicodeUTF8))
        self.del_patient_btn.setText(QtGui.QApplication.translate("all_patients_form", "Удалить", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("all_patients_form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.add_patient_btn.setText(QtGui.QApplication.translate("all_patients_form", "Новый пациент", None, QtGui.QApplication.UnicodeUTF8))

