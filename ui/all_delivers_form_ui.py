# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all_delivers_form.ui'
#
# Created: Wed Apr 13 14:44:12 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_all_delivers_form(object):
    def setupUi(self, all_delivers_form):
        all_delivers_form.setObjectName("all_delivers_form")
        all_delivers_form.resize(626, 329)
        self.gridLayout = QtGui.QGridLayout(all_delivers_form)
        self.gridLayout.setObjectName("gridLayout")
        self.delivers_table = QtGui.QTableWidget(all_delivers_form)
        self.delivers_table.setObjectName("delivers_table")
        self.delivers_table.setColumnCount(0)
        self.delivers_table.setRowCount(0)
        self.gridLayout.addWidget(self.delivers_table, 0, 0, 1, 6)
        self.close_btn = QtGui.QPushButton(all_delivers_form)
        self.close_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.close_btn.setObjectName("close_btn")
        self.gridLayout.addWidget(self.close_btn, 1, 5, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(all_delivers_form)
        self.pushButton.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 4, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(all_delivers_form)
        self.pushButton_2.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 3, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(all_delivers_form)
        self.pushButton_3.setMinimumSize(QtCore.QSize(40, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)

        self.retranslateUi(all_delivers_form)
        QtCore.QObject.connect(self.close_btn, QtCore.SIGNAL("clicked()"), all_delivers_form.close)
        QtCore.QMetaObject.connectSlotsByName(all_delivers_form)

    def retranslateUi(self, all_delivers_form):
        all_delivers_form.setWindowTitle(QtGui.QApplication.translate("all_delivers_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.close_btn.setText(QtGui.QApplication.translate("all_delivers_form", "Закрыть", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("all_delivers_form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("all_delivers_form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("all_delivers_form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

