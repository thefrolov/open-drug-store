# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all_doctors_form.ui'
#
# Created: Wed May  4 15:55:28 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_all_doctors_form(object):
    def setupUi(self, all_doctors_form):
        all_doctors_form.setObjectName(_fromUtf8("all_doctors_form"))
        all_doctors_form.resize(631, 379)
        self.gridLayout = QtGui.QGridLayout(all_doctors_form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.doctors_table = QtGui.QTableWidget(all_doctors_form)
        self.doctors_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.doctors_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.doctors_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.doctors_table.setObjectName(_fromUtf8("doctors_table"))
        self.doctors_table.setColumnCount(0)
        self.doctors_table.setRowCount(0)
        self.gridLayout.addWidget(self.doctors_table, 0, 0, 1, 7)
        self.close_btn = QtGui.QPushButton(all_doctors_form)
        self.close_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.close_btn.setObjectName(_fromUtf8("close_btn"))
        self.gridLayout.addWidget(self.close_btn, 1, 6, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.del_doctor_btn = QtGui.QPushButton(all_doctors_form)
        self.del_doctor_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.del_doctor_btn.setObjectName(_fromUtf8("del_doctor_btn"))
        self.gridLayout.addWidget(self.del_doctor_btn, 1, 4, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(all_doctors_form)
        self.pushButton_3.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.add_doctor_btn = QtGui.QPushButton(all_doctors_form)
        self.add_doctor_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.add_doctor_btn.setObjectName(_fromUtf8("add_doctor_btn"))
        self.gridLayout.addWidget(self.add_doctor_btn, 1, 3, 1, 1)

        self.retranslateUi(all_doctors_form)
        QtCore.QObject.connect(self.close_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), all_doctors_form.close)
        QtCore.QMetaObject.connectSlotsByName(all_doctors_form)

    def retranslateUi(self, all_doctors_form):
        all_doctors_form.setWindowTitle(QtGui.QApplication.translate("all_doctors_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.close_btn.setText(QtGui.QApplication.translate("all_doctors_form", "Закрыть", None, QtGui.QApplication.UnicodeUTF8))
        self.del_doctor_btn.setText(QtGui.QApplication.translate("all_doctors_form", "удалить", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("all_doctors_form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.add_doctor_btn.setText(QtGui.QApplication.translate("all_doctors_form", "Новый врач", None, QtGui.QApplication.UnicodeUTF8))

