# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all_ills_form.ui'
#
# Created: Wed May  4 16:12:03 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_all_ills_form(object):
    def setupUi(self, all_ills_form):
        all_ills_form.setObjectName(_fromUtf8("all_ills_form"))
        all_ills_form.resize(626, 329)
        self.gridLayout = QtGui.QGridLayout(all_ills_form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ills_table = QtGui.QTableWidget(all_ills_form)
        self.ills_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.ills_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.ills_table.setObjectName(_fromUtf8("ills_table"))
        self.ills_table.setColumnCount(0)
        self.ills_table.setRowCount(0)
        self.gridLayout.addWidget(self.ills_table, 0, 0, 1, 7)
        self.close_btn = QtGui.QPushButton(all_ills_form)
        self.close_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.close_btn.setObjectName(_fromUtf8("close_btn"))
        self.gridLayout.addWidget(self.close_btn, 1, 6, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.add_distributor_btn = QtGui.QPushButton(all_ills_form)
        self.add_distributor_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.add_distributor_btn.setObjectName(_fromUtf8("add_distributor_btn"))
        self.gridLayout.addWidget(self.add_distributor_btn, 1, 4, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(all_ills_form)
        self.pushButton_3.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.del_ill_btn = QtGui.QPushButton(all_ills_form)
        self.del_ill_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.del_ill_btn.setObjectName(_fromUtf8("del_ill_btn"))
        self.gridLayout.addWidget(self.del_ill_btn, 1, 5, 1, 1)

        self.retranslateUi(all_ills_form)
        QtCore.QObject.connect(self.close_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), all_ills_form.close)
        QtCore.QMetaObject.connectSlotsByName(all_ills_form)

    def retranslateUi(self, all_ills_form):
        all_ills_form.setWindowTitle(QtGui.QApplication.translate("all_ills_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.close_btn.setText(QtGui.QApplication.translate("all_ills_form", "Закрыть", None, QtGui.QApplication.UnicodeUTF8))
        self.add_distributor_btn.setText(QtGui.QApplication.translate("all_ills_form", "Новое заболевание", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("all_ills_form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.del_ill_btn.setText(QtGui.QApplication.translate("all_ills_form", "Удалить", None, QtGui.QApplication.UnicodeUTF8))

