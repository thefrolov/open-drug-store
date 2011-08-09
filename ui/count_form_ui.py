# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'count_form.ui'
#
# Created: Wed Mar 30 15:51:05 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_count_form(object):
    def setupUi(self, count_form):
        count_form.setObjectName("count_form")
        count_form.resize(157, 108)
        self.verticalLayout = QtGui.QVBoxLayout(count_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(count_form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(count_form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.ok_btn = QtGui.QPushButton(count_form)
        self.ok_btn.setObjectName("ok_btn")
        self.verticalLayout.addWidget(self.ok_btn)

        self.retranslateUi(count_form)
        QtCore.QMetaObject.connectSlotsByName(count_form)

    def retranslateUi(self, count_form):
        count_form.setWindowTitle(QtGui.QApplication.translate("count_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("count_form", "Количество", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_btn.setText(QtGui.QApplication.translate("count_form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

