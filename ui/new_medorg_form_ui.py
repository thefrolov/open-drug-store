# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_medorg_form.ui'
#
# Created: Fri Apr 29 15:40:28 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_new_medorg_form(object):
    def setupUi(self, new_medorg_form):
        new_medorg_form.setObjectName("new_medorg_form")
        new_medorg_form.resize(294, 114)
        self.gridLayout = QtGui.QGridLayout(new_medorg_form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(new_medorg_form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.medorg_name = QtGui.QLineEdit(new_medorg_form)
        self.medorg_name.setObjectName("medorg_name")
        self.gridLayout.addWidget(self.medorg_name, 0, 2, 1, 1)
        self.groupBox = QtGui.QGroupBox(new_medorg_form)
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

        self.retranslateUi(new_medorg_form)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL("clicked()"), new_medorg_form.close)
        QtCore.QMetaObject.connectSlotsByName(new_medorg_form)

    def retranslateUi(self, new_medorg_form):
        new_medorg_form.setWindowTitle(QtGui.QApplication.translate("new_medorg_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("new_medorg_form", "Название", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("new_medorg_form", "Отмена", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_btn.setText(QtGui.QApplication.translate("new_medorg_form", "ok", None, QtGui.QApplication.UnicodeUTF8))

