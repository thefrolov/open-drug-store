# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_distributor_form.ui'
#
# Created: Wed Apr 20 10:11:13 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_new_distributor_form(object):
    def setupUi(self, new_distributor_form):
        new_distributor_form.setObjectName("new_distributor_form")
        new_distributor_form.resize(294, 114)
        self.gridLayout = QtGui.QGridLayout(new_distributor_form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(new_distributor_form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.distributor_name = QtGui.QLineEdit(new_distributor_form)
        self.distributor_name.setObjectName("distributor_name")
        self.gridLayout.addWidget(self.distributor_name, 0, 2, 1, 1)
        self.groupBox = QtGui.QGroupBox(new_distributor_form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cancel_btn = QtGui.QPushButton(self.groupBox)
        self.cancel_btn.setObjectName("cancel_btn")
        self.gridLayout_2.addWidget(self.cancel_btn, 0, 0, 1, 1)
        self.ok_btn = QtGui.QPushButton(self.groupBox)
        self.ok_btn.setObjectName("ok_btn")
        self.gridLayout_2.addWidget(self.ok_btn, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 2)

        self.retranslateUi(new_distributor_form)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL("clicked()"), new_distributor_form.close)
        QtCore.QMetaObject.connectSlotsByName(new_distributor_form)

    def retranslateUi(self, new_distributor_form):
        new_distributor_form.setWindowTitle(QtGui.QApplication.translate("new_distributor_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("new_distributor_form", "Название", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("new_distributor_form", "Отмена", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_btn.setText(QtGui.QApplication.translate("new_distributor_form", "ok", None, QtGui.QApplication.UnicodeUTF8))

