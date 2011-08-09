# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_manufacter_form.ui'
#
# Created: Mon Apr 11 13:43:29 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_new_manufacter_form(object):
    def setupUi(self, new_manufacter_form):
        new_manufacter_form.setObjectName("new_manufacter_form")
        new_manufacter_form.resize(400, 143)
        self.gridLayout = QtGui.QGridLayout(new_manufacter_form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(new_manufacter_form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.manufacter_name = QtGui.QLineEdit(new_manufacter_form)
        self.manufacter_name.setObjectName("manufacter_name")
        self.gridLayout.addWidget(self.manufacter_name, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(new_manufacter_form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.manufacter_country = QtGui.QLineEdit(new_manufacter_form)
        self.manufacter_country.setObjectName("manufacter_country")
        self.gridLayout.addWidget(self.manufacter_country, 1, 2, 1, 1)
        self.groupBox = QtGui.QGroupBox(new_manufacter_form)
        self.groupBox.setObjectName("groupBox")
        self.ok_btn = QtGui.QPushButton(self.groupBox)
        self.ok_btn.setGeometry(QtCore.QRect(190, 20, 98, 27))
        self.ok_btn.setObjectName("ok_btn")
        self.cancel_btn = QtGui.QPushButton(self.groupBox)
        self.cancel_btn.setGeometry(QtCore.QRect(80, 20, 98, 27))
        self.cancel_btn.setObjectName("cancel_btn")
        self.gridLayout.addWidget(self.groupBox, 2, 1, 1, 2)

        self.retranslateUi(new_manufacter_form)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL("clicked()"), new_manufacter_form.close)
        QtCore.QMetaObject.connectSlotsByName(new_manufacter_form)

    def retranslateUi(self, new_manufacter_form):
        new_manufacter_form.setWindowTitle(QtGui.QApplication.translate("new_manufacter_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("new_manufacter_form", "Название", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("new_manufacter_form", "Страна", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("new_manufacter_form", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_btn.setText(QtGui.QApplication.translate("new_manufacter_form", "ok", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("new_manufacter_form", "Отмена", None, QtGui.QApplication.UnicodeUTF8))

