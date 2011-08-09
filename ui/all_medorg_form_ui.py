# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all_medorg_form.ui'
#
# Created: Wed May  4 15:55:44 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_all_medorg_form(object):
    def setupUi(self, all_medorg_form):
        all_medorg_form.setObjectName(_fromUtf8("all_medorg_form"))
        all_medorg_form.resize(626, 329)
        self.gridLayout = QtGui.QGridLayout(all_medorg_form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.medorg_table = QtGui.QTableWidget(all_medorg_form)
        self.medorg_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.medorg_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.medorg_table.setObjectName(_fromUtf8("medorg_table"))
        self.medorg_table.setColumnCount(0)
        self.medorg_table.setRowCount(0)
        self.gridLayout.addWidget(self.medorg_table, 0, 0, 1, 7)
        self.close_btn = QtGui.QPushButton(all_medorg_form)
        self.close_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.close_btn.setObjectName(_fromUtf8("close_btn"))
        self.gridLayout.addWidget(self.close_btn, 1, 6, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.del_medorg_btn = QtGui.QPushButton(all_medorg_form)
        self.del_medorg_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.del_medorg_btn.setObjectName(_fromUtf8("del_medorg_btn"))
        self.gridLayout.addWidget(self.del_medorg_btn, 1, 4, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(all_medorg_form)
        self.pushButton_3.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.add_medorg_btn = QtGui.QPushButton(all_medorg_form)
        self.add_medorg_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.add_medorg_btn.setObjectName(_fromUtf8("add_medorg_btn"))
        self.gridLayout.addWidget(self.add_medorg_btn, 1, 3, 1, 1)

        self.retranslateUi(all_medorg_form)
        QtCore.QObject.connect(self.close_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), all_medorg_form.close)
        QtCore.QMetaObject.connectSlotsByName(all_medorg_form)

    def retranslateUi(self, all_medorg_form):
        all_medorg_form.setWindowTitle(QtGui.QApplication.translate("all_medorg_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.close_btn.setText(QtGui.QApplication.translate("all_medorg_form", "Закрыть", None, QtGui.QApplication.UnicodeUTF8))
        self.del_medorg_btn.setText(QtGui.QApplication.translate("all_medorg_form", "Удалить", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("all_medorg_form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.add_medorg_btn.setText(QtGui.QApplication.translate("all_medorg_form", "Новая мо", None, QtGui.QApplication.UnicodeUTF8))

