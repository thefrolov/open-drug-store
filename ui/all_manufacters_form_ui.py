# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all_manufacters_form.ui'
#
# Created: Sat May  7 13:07:46 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_all_manufacters_form(object):
    def setupUi(self, all_manufacters_form):
        all_manufacters_form.setObjectName(_fromUtf8("all_manufacters_form"))
        all_manufacters_form.resize(631, 379)
        self.gridLayout = QtGui.QGridLayout(all_manufacters_form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.manufacters_table = QtGui.QTableWidget(all_manufacters_form)
        self.manufacters_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.manufacters_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.manufacters_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.manufacters_table.setObjectName(_fromUtf8("manufacters_table"))
        self.manufacters_table.setColumnCount(0)
        self.manufacters_table.setRowCount(0)
        self.gridLayout.addWidget(self.manufacters_table, 0, 0, 1, 7)
        self.close_btn = QtGui.QPushButton(all_manufacters_form)
        self.close_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.close_btn.setObjectName(_fromUtf8("close_btn"))
        self.gridLayout.addWidget(self.close_btn, 1, 6, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.del_manufacter_btn = QtGui.QPushButton(all_manufacters_form)
        self.del_manufacter_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.del_manufacter_btn.setObjectName(_fromUtf8("del_manufacter_btn"))
        self.gridLayout.addWidget(self.del_manufacter_btn, 1, 4, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(all_manufacters_form)
        self.pushButton_3.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.add_manufacter_btn = QtGui.QPushButton(all_manufacters_form)
        self.add_manufacter_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.add_manufacter_btn.setObjectName(_fromUtf8("add_manufacter_btn"))
        self.gridLayout.addWidget(self.add_manufacter_btn, 1, 3, 1, 1)

        self.retranslateUi(all_manufacters_form)
        QtCore.QObject.connect(self.close_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), all_manufacters_form.close)
        QtCore.QMetaObject.connectSlotsByName(all_manufacters_form)

    def retranslateUi(self, all_manufacters_form):
        all_manufacters_form.setWindowTitle(QtGui.QApplication.translate("all_manufacters_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.close_btn.setText(QtGui.QApplication.translate("all_manufacters_form", "Закрыть", None, QtGui.QApplication.UnicodeUTF8))
        self.del_manufacter_btn.setText(QtGui.QApplication.translate("all_manufacters_form", "удалить", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("all_manufacters_form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.add_manufacter_btn.setText(QtGui.QApplication.translate("all_manufacters_form", "Новый производитель", None, QtGui.QApplication.UnicodeUTF8))

