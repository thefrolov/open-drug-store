# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_financing_form.ui'
#
# Created: Sun May 22 15:39:02 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_new_financing_form(object):
    def setupUi(self, new_financing_form):
        new_financing_form.setObjectName(_fromUtf8("new_financing_form"))
        new_financing_form.resize(294, 114)
        self.gridLayout = QtGui.QGridLayout(new_financing_form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(new_financing_form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.financing_name = QtGui.QLineEdit(new_financing_form)
        self.financing_name.setObjectName(_fromUtf8("financing_name"))
        self.gridLayout.addWidget(self.financing_name, 0, 2, 1, 1)
        self.groupBox = QtGui.QGroupBox(new_financing_form)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.cancel_btn = QtGui.QPushButton(self.groupBox)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.gridLayout_2.addWidget(self.cancel_btn, 0, 0, 1, 1)
        self.ok_btn = QtGui.QPushButton(self.groupBox)
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.gridLayout_2.addWidget(self.ok_btn, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 2)

        self.retranslateUi(new_financing_form)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), new_financing_form.close)
        QtCore.QMetaObject.connectSlotsByName(new_financing_form)

    def retranslateUi(self, new_financing_form):
        new_financing_form.setWindowTitle(QtGui.QApplication.translate("new_financing_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("new_financing_form", "Источник", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("new_financing_form", "Отмена", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_btn.setText(QtGui.QApplication.translate("new_financing_form", "ok", None, QtGui.QApplication.UnicodeUTF8))

