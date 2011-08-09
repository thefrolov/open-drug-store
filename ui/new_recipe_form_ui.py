# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_recipe_form.ui'
#
# Created: Sat May  7 14:27:00 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_new_recipe_form(object):
    def setupUi(self, new_recipe_form):
        new_recipe_form.setObjectName(_fromUtf8("new_recipe_form"))
        new_recipe_form.resize(500, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(new_recipe_form.sizePolicy().hasHeightForWidth())
        new_recipe_form.setSizePolicy(sizePolicy)
        new_recipe_form.setMaximumSize(QtCore.QSize(16777215, 300))
        self.gridLayout = QtGui.QGridLayout(new_recipe_form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.recipe_num = QtGui.QLabel(new_recipe_form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recipe_num.sizePolicy().hasHeightForWidth())
        self.recipe_num.setSizePolicy(sizePolicy)
        self.recipe_num.setMinimumSize(QtCore.QSize(0, 30))
        self.recipe_num.setObjectName(_fromUtf8("recipe_num"))
        self.gridLayout.addWidget(self.recipe_num, 0, 0, 1, 2)
        self.label = QtGui.QLabel(new_recipe_form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.patient_combo = QtGui.QComboBox(new_recipe_form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patient_combo.sizePolicy().hasHeightForWidth())
        self.patient_combo.setSizePolicy(sizePolicy)
        self.patient_combo.setEditable(True)
        self.patient_combo.setObjectName(_fromUtf8("patient_combo"))
        self.gridLayout.addWidget(self.patient_combo, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(new_recipe_form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.m_org_combo = QtGui.QComboBox(new_recipe_form)
        self.m_org_combo.setEditable(True)
        self.m_org_combo.setObjectName(_fromUtf8("m_org_combo"))
        self.gridLayout.addWidget(self.m_org_combo, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(new_recipe_form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.doctor_combo = QtGui.QComboBox(new_recipe_form)
        self.doctor_combo.setEditable(True)
        self.doctor_combo.setObjectName(_fromUtf8("doctor_combo"))
        self.gridLayout.addWidget(self.doctor_combo, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(new_recipe_form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.ill_combo = QtGui.QComboBox(new_recipe_form)
        self.ill_combo.setEditable(True)
        self.ill_combo.setObjectName(_fromUtf8("ill_combo"))
        self.gridLayout.addWidget(self.ill_combo, 4, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(new_recipe_form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(137, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.cancel_btn = QtGui.QPushButton(self.groupBox)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.gridLayout_2.addWidget(self.cancel_btn, 0, 1, 1, 1)
        self.ok_btn = QtGui.QPushButton(self.groupBox)
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.gridLayout_2.addWidget(self.ok_btn, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 5, 1, 1, 1)

        self.retranslateUi(new_recipe_form)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), new_recipe_form.close)
        QtCore.QMetaObject.connectSlotsByName(new_recipe_form)

    def retranslateUi(self, new_recipe_form):
        new_recipe_form.setWindowTitle(QtGui.QApplication.translate("new_recipe_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.recipe_num.setText(QtGui.QApplication.translate("new_recipe_form", "num", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("new_recipe_form", "Пациент", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("new_recipe_form", "Мед. организация", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("new_recipe_form", "Лечащий врач", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("new_recipe_form", "Заболевание", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("new_recipe_form", "Отмена", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_btn.setText(QtGui.QApplication.translate("new_recipe_form", "ok", None, QtGui.QApplication.UnicodeUTF8))

