# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all_recipes_form.ui'
#
# Created: Sun May 22 18:28:56 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_all_recipes_form(object):
    def setupUi(self, all_recipes_form):
        all_recipes_form.setObjectName(_fromUtf8("all_recipes_form"))
        all_recipes_form.resize(626, 329)
        self.gridLayout = QtGui.QGridLayout(all_recipes_form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.recipes_table = QtGui.QTableWidget(all_recipes_form)
        self.recipes_table.setObjectName(_fromUtf8("recipes_table"))
        self.recipes_table.setColumnCount(0)
        self.recipes_table.setRowCount(0)
        self.gridLayout.addWidget(self.recipes_table, 0, 0, 1, 6)
        self.close_btn = QtGui.QPushButton(all_recipes_form)
        self.close_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.close_btn.setObjectName(_fromUtf8("close_btn"))
        self.gridLayout.addWidget(self.close_btn, 1, 5, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.print_report_btn = QtGui.QPushButton(all_recipes_form)
        self.print_report_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.print_report_btn.setObjectName(_fromUtf8("print_report_btn"))
        self.gridLayout.addWidget(self.print_report_btn, 1, 4, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(all_recipes_form)
        self.pushButton_2.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 1, 3, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(all_recipes_form)
        self.pushButton_3.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)

        self.retranslateUi(all_recipes_form)
        QtCore.QObject.connect(self.close_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), all_recipes_form.close)
        QtCore.QMetaObject.connectSlotsByName(all_recipes_form)

    def retranslateUi(self, all_recipes_form):
        all_recipes_form.setWindowTitle(QtGui.QApplication.translate("all_recipes_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.close_btn.setText(QtGui.QApplication.translate("all_recipes_form", "Закрыть", None, QtGui.QApplication.UnicodeUTF8))
        self.print_report_btn.setText(QtGui.QApplication.translate("all_recipes_form", "Создать отчет", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("all_recipes_form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("all_recipes_form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

