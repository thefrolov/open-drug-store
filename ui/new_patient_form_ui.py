# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_patient_form.ui'
#
# Created: Fri Apr 22 16:14:38 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_new_patient_form(object):
    def setupUi(self, new_patient_form):
        new_patient_form.setObjectName("new_patient_form")
        new_patient_form.resize(494, 167)
        self.gridLayout = QtGui.QGridLayout(new_patient_form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(new_patient_form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.first_name = QtGui.QLineEdit(new_patient_form)
        self.first_name.setObjectName("first_name")
        self.gridLayout.addWidget(self.first_name, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(new_patient_form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.last_name = QtGui.QLineEdit(new_patient_form)
        self.last_name.setObjectName("last_name")
        self.gridLayout.addWidget(self.last_name, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(new_patient_form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.birth_date = QtGui.QLineEdit(new_patient_form)
        self.birth_date.setObjectName("birth_date")
        self.gridLayout.addWidget(self.birth_date, 2, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(new_patient_form)
        self.groupBox.setObjectName("groupBox")
        self.ok_btn = QtGui.QPushButton(self.groupBox)
        self.ok_btn.setGeometry(QtCore.QRect(250, 10, 98, 27))
        self.ok_btn.setObjectName("ok_btn")
        self.cancel_btn = QtGui.QPushButton(self.groupBox)
        self.cancel_btn.setGeometry(QtCore.QRect(140, 10, 98, 27))
        self.cancel_btn.setObjectName("cancel_btn")
        self.gridLayout.addWidget(self.groupBox, 3, 1, 1, 1)

        self.retranslateUi(new_patient_form)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL("clicked()"), new_patient_form.close)
        QtCore.QMetaObject.connectSlotsByName(new_patient_form)

    def retranslateUi(self, new_patient_form):
        new_patient_form.setWindowTitle(QtGui.QApplication.translate("new_patient_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("new_patient_form", "Имя", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("new_patient_form", "Фамилия", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("new_patient_form", "Дата рождения", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("new_patient_form", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_btn.setText(QtGui.QApplication.translate("new_patient_form", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("new_patient_form", "Отмена", None, QtGui.QApplication.UnicodeUTF8))

