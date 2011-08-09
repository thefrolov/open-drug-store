# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_doctor_form.ui'
#
# Created: Wed May  4 10:47:37 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_new_doctor_form(object):
    def setupUi(self, new_doctor_form):
        new_doctor_form.setObjectName("new_doctor_form")
        new_doctor_form.resize(494, 167)
        self.gridLayout = QtGui.QGridLayout(new_doctor_form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(new_doctor_form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.first_name = QtGui.QLineEdit(new_doctor_form)
        self.first_name.setObjectName("first_name")
        self.gridLayout.addWidget(self.first_name, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(new_doctor_form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.last_name = QtGui.QLineEdit(new_doctor_form)
        self.last_name.setObjectName("last_name")
        self.gridLayout.addWidget(self.last_name, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(new_doctor_form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.m_org_combo = QtGui.QComboBox(new_doctor_form)
        self.m_org_combo.setObjectName("m_org_combo")
        self.gridLayout.addWidget(self.m_org_combo, 2, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(new_doctor_form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.ok_btn = QtGui.QPushButton(self.groupBox)
        self.ok_btn.setGeometry(QtCore.QRect(210, 10, 98, 27))
        self.ok_btn.setObjectName("ok_btn")
        self.cancel_btn = QtGui.QPushButton(self.groupBox)
        self.cancel_btn.setGeometry(QtCore.QRect(90, 10, 98, 27))
        self.cancel_btn.setObjectName("cancel_btn")
        self.gridLayout.addWidget(self.groupBox, 3, 1, 1, 1)

        self.retranslateUi(new_doctor_form)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL("clicked()"), new_doctor_form.close)
        QtCore.QMetaObject.connectSlotsByName(new_doctor_form)

    def retranslateUi(self, new_doctor_form):
        new_doctor_form.setWindowTitle(QtGui.QApplication.translate("new_doctor_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("new_doctor_form", "Имя", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("new_doctor_form", "Фамилия", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("new_doctor_form", "Мед. организация", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_btn.setText(QtGui.QApplication.translate("new_doctor_form", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("new_doctor_form", "Отмена", None, QtGui.QApplication.UnicodeUTF8))

