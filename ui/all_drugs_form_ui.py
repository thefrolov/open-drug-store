# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all_drugs_form.ui'
#
# Created: Wed May  4 16:06:39 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_all_drugs_form(object):
    def setupUi(self, all_drugs_form):
        all_drugs_form.setObjectName(_fromUtf8("all_drugs_form"))
        all_drugs_form.setWindowModality(QtCore.Qt.NonModal)
        all_drugs_form.resize(965, 515)
        all_drugs_form.setFrameShape(QtGui.QFrame.StyledPanel)
        all_drugs_form.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout_2 = QtGui.QGridLayout(all_drugs_form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(all_drugs_form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 1)
        self.tableWidget = QtGui.QTableWidget(all_drugs_form)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 4)
        self.new_drug_btn = QtGui.QPushButton(all_drugs_form)
        self.new_drug_btn.setObjectName(_fromUtf8("new_drug_btn"))
        self.gridLayout.addWidget(self.new_drug_btn, 2, 0, 1, 1)
        self.close_btn = QtGui.QPushButton(all_drugs_form)
        self.close_btn.setMinimumSize(QtCore.QSize(200, 0))
        self.close_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.close_btn.setObjectName(_fromUtf8("close_btn"))
        self.gridLayout.addWidget(self.close_btn, 2, 2, 1, 1)
        self.del_drug_btn = QtGui.QPushButton(all_drugs_form)
        self.del_drug_btn.setObjectName(_fromUtf8("del_drug_btn"))
        self.gridLayout.addWidget(self.del_drug_btn, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(all_drugs_form)
        QtCore.QObject.connect(self.close_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), all_drugs_form.close)
        QtCore.QMetaObject.connectSlotsByName(all_drugs_form)

    def retranslateUi(self, all_drugs_form):
        all_drugs_form.setWindowTitle(QtGui.QApplication.translate("all_drugs_form", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("all_drugs_form", "Всего лс на сумму 0.00р", None, QtGui.QApplication.UnicodeUTF8))
        self.new_drug_btn.setText(QtGui.QApplication.translate("all_drugs_form", "Новое лс", None, QtGui.QApplication.UnicodeUTF8))
        self.close_btn.setText(QtGui.QApplication.translate("all_drugs_form", "Закрыть", None, QtGui.QApplication.UnicodeUTF8))
        self.del_drug_btn.setText(QtGui.QApplication.translate("all_drugs_form", "Удалить лс", None, QtGui.QApplication.UnicodeUTF8))

