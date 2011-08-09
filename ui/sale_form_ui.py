# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sale_form.ui'
#
# Created: Mon May 23 22:24:04 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_sale_form(object):
    def setupUi(self, sale_form):
        sale_form.setObjectName(_fromUtf8("sale_form"))
        sale_form.setWindowModality(QtCore.Qt.NonModal)
        sale_form.resize(1246, 420)
        sale_form.setFrameShape(QtGui.QFrame.StyledPanel)
        sale_form.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout = QtGui.QGridLayout(sale_form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.bill_number_date = QtGui.QLabel(sale_form)
        self.bill_number_date.setObjectName(_fromUtf8("bill_number_date"))
        self.gridLayout.addWidget(self.bill_number_date, 0, 0, 1, 2)
        self.label = QtGui.QLabel(sale_form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.reciever_combo = QtGui.QComboBox(sale_form)
        self.reciever_combo.setObjectName(_fromUtf8("reciever_combo"))
        self.reciever_combo.addItem(_fromUtf8(""))
        self.reciever_combo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.reciever_combo, 4, 1, 1, 1)
        self.tableWidget = QtGui.QTableWidget(sale_form)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 5, 0, 1, 6)
        self.save_close_btn = QtGui.QPushButton(sale_form)
        self.save_close_btn.setMaximumSize(QtCore.QSize(190, 16777215))
        self.save_close_btn.setObjectName(_fromUtf8("save_close_btn"))
        self.gridLayout.addWidget(self.save_close_btn, 6, 0, 1, 1)
        self.save_btn = QtGui.QPushButton(sale_form)
        self.save_btn.setMaximumSize(QtCore.QSize(190, 16777215))
        self.save_btn.setObjectName(_fromUtf8("save_btn"))
        self.gridLayout.addWidget(self.save_btn, 6, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(sale_form)
        self.pushButton.setMinimumSize(QtCore.QSize(190, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(96, 16777215))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 6, 2, 1, 1)
        self.close_btn = QtGui.QPushButton(sale_form)
        self.close_btn.setMaximumSize(QtCore.QSize(190, 16777215))
        self.close_btn.setObjectName(_fromUtf8("close_btn"))
        self.gridLayout.addWidget(self.close_btn, 6, 3, 1, 1)
        self.label_3 = QtGui.QLabel(sale_form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 6, 5, 1, 1)
        self.reciever_btn = QtGui.QPushButton(sale_form)
        self.reciever_btn.setEnabled(True)
        self.reciever_btn.setAutoFillBackground(False)
        self.reciever_btn.setCheckable(False)
        self.reciever_btn.setChecked(False)
        self.reciever_btn.setObjectName(_fromUtf8("reciever_btn"))
        self.gridLayout.addWidget(self.reciever_btn, 4, 2, 1, 1)
        self.reciever_label = QtGui.QLabel(sale_form)
        self.reciever_label.setText(_fromUtf8(""))
        self.reciever_label.setObjectName(_fromUtf8("reciever_label"))
        self.gridLayout.addWidget(self.reciever_label, 4, 3, 1, 1)
        self.financing_combo = QtGui.QComboBox(sale_form)
        self.financing_combo.setObjectName(_fromUtf8("financing_combo"))
        self.gridLayout.addWidget(self.financing_combo, 4, 5, 1, 1)
        self.label_2 = QtGui.QLabel(sale_form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 4, 1, 1)

        self.retranslateUi(sale_form)
        self.reciever_combo.setCurrentIndex(0)
        QtCore.QObject.connect(self.close_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), sale_form.close)
        QtCore.QMetaObject.connectSlotsByName(sale_form)

    def retranslateUi(self, sale_form):
        sale_form.setWindowTitle(QtGui.QApplication.translate("sale_form", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.bill_number_date.setText(QtGui.QApplication.translate("sale_form", "Накладная №1 от 10.10.10", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("sale_form", "Получатель", None, QtGui.QApplication.UnicodeUTF8))
        self.reciever_combo.setItemText(0, QtGui.QApplication.translate("sale_form", "Пациент", None, QtGui.QApplication.UnicodeUTF8))
        self.reciever_combo.setItemText(1, QtGui.QApplication.translate("sale_form", "Медицинская организация", None, QtGui.QApplication.UnicodeUTF8))
        self.save_close_btn.setText(QtGui.QApplication.translate("sale_form", "Провести накладную", None, QtGui.QApplication.UnicodeUTF8))
        self.save_btn.setText(QtGui.QApplication.translate("sale_form", "Сохранить и не проводить", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("sale_form", "Просто кнопка", None, QtGui.QApplication.UnicodeUTF8))
        self.close_btn.setText(QtGui.QApplication.translate("sale_form", "Закрыть без сохранения", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("sale_form", "Всего лс на сумму 0.00р", None, QtGui.QApplication.UnicodeUTF8))
        self.reciever_btn.setText(QtGui.QApplication.translate("sale_form", "Рецепт", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("sale_form", "Источник финансирования", None, QtGui.QApplication.UnicodeUTF8))

