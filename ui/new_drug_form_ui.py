# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_drug_form.ui'
#
# Created: Sat Apr  9 13:42:59 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_new_drug_form(object):
    def setupUi(self, new_drug_form):
        new_drug_form.setObjectName("new_drug_form")
        new_drug_form.resize(558, 220)
        self.formLayout = QtGui.QFormLayout(new_drug_form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(new_drug_form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.drug_name = QtGui.QLineEdit(new_drug_form)
        self.drug_name.setObjectName("drug_name")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.drug_name)
        self.label_2 = QtGui.QLabel(new_drug_form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.manufacter_combo = QtGui.QComboBox(new_drug_form)
        self.manufacter_combo.setObjectName("manufacter_combo")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.manufacter_combo)
        self.label_3 = QtGui.QLabel(new_drug_form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.serial_number = QtGui.QLineEdit(new_drug_form)
        self.serial_number.setObjectName("serial_number")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.serial_number)
        self.label_4 = QtGui.QLabel(new_drug_form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(new_drug_form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.price = QtGui.QLineEdit(new_drug_form)
        self.price.setObjectName("price")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.price)
        self.groupBox = QtGui.QGroupBox(new_drug_form)
        self.groupBox.setObjectName("groupBox")
        self.ok_btn = QtGui.QPushButton(self.groupBox)
        self.ok_btn.setGeometry(QtCore.QRect(265, 1, 85, 27))
        self.ok_btn.setObjectName("ok_btn")
        self.cancel_btn = QtGui.QPushButton(self.groupBox)
        self.cancel_btn.setGeometry(QtCore.QRect(161, 1, 85, 27))
        self.cancel_btn.setObjectName("cancel_btn")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.groupBox)
        self.best_before = QtGui.QLineEdit(new_drug_form)
        self.best_before.setObjectName("best_before")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.best_before)

        self.retranslateUi(new_drug_form)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL("clicked()"), new_drug_form.close)
        QtCore.QMetaObject.connectSlotsByName(new_drug_form)

    def retranslateUi(self, new_drug_form):
        new_drug_form.setWindowTitle(QtGui.QApplication.translate("new_drug_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("new_drug_form", "Наименование лс", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("new_drug_form", "Производитель", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("new_drug_form", "Серийный номер", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("new_drug_form", "Срок годности", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("new_drug_form", "Цена", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("new_drug_form", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_btn.setText(QtGui.QApplication.translate("new_drug_form", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("new_drug_form", "Отмена", None, QtGui.QApplication.UnicodeUTF8))
        self.best_before.setInputMask(QtGui.QApplication.translate("new_drug_form", "00.00.0000; ", None, QtGui.QApplication.UnicodeUTF8))

