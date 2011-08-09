#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys

# Import Qt modules
from PyQt4 import QtGui
from PyQt4.QtCore import *

from main_window import MainWindow
from deliver_form import DeliverWindow
from sale_form import SaleWindow
import utils

def main():
    app = QtGui.QApplication(sys.argv)
    
#    deliver_widget = DeliverWindow()
#    sale_widget = SaleWindow()
    
    mw = MainWindow()
#    mw.windows.append(deliver_widget)
#    mw.windows.append(sale_widget)
    
    mapper = QSignalMapper()
    

    QObject.connect(mw.ui.deliver_action, SIGNAL("activated()"), mapper,SLOT("map()"))
    QObject.connect(mw.ui.sale_action, SIGNAL("activated()"), mapper,SLOT("map()"))
    QObject.connect(mw.ui.all_drugs_action, SIGNAL("activated()"), mapper,SLOT("map()"))
    QObject.connect(mw.ui.all_delivers_action, SIGNAL("activated()"), mapper,SLOT("map()"))
    QObject.connect(mw.ui.all_sales_action, SIGNAL("activated()"), mapper,SLOT("map()"))
    QObject.connect(mw.ui.all_patients_action, SIGNAL("activated()"), mapper,SLOT("map()"))
    QObject.connect(mw.ui.all_distributors_action, SIGNAL("activated()"), mapper,SLOT("map()"))
    QObject.connect(mw.ui.all_medorg_action, SIGNAL("activated()"), mapper,SLOT("map()"))
    QObject.connect(mw.ui.all_doctors_action, SIGNAL("activated()"), mapper,SLOT("map()"))
    QObject.connect(mw.ui.all_manufacters_action, SIGNAL("activated()"), mapper,SLOT("map()"))
    QObject.connect(mw.ui.all_ills_action, SIGNAL("activated()"), mapper,SLOT("map()"))
    QObject.connect(mw.ui.all_recipes_action, SIGNAL("activated()"), mapper,SLOT("map()"))
 
    mapper.setMapping(mw.ui.deliver_action, 0)
    mapper.setMapping(mw.ui.sale_action, 1)
    mapper.setMapping(mw.ui.all_drugs_action, 2)
    mapper.setMapping(mw.ui.all_delivers_action, 3)
    mapper.setMapping(mw.ui.all_sales_action, 4)
    mapper.setMapping(mw.ui.all_patients_action, 5)
    mapper.setMapping(mw.ui.all_distributors_action, 6)
    mapper.setMapping(mw.ui.all_medorg_action, 7)
    mapper.setMapping(mw.ui.all_doctors_action, 8)
    mapper.setMapping(mw.ui.all_manufacters_action, 9)
    mapper.setMapping(mw.ui.all_ills_action, 10)
    mapper.setMapping(mw.ui.all_recipes_action, 11)
 
    QObject.connect(mapper,SIGNAL("mapped(int)"), mw,SLOT("show_child_window(int)"))
    mw.showMaximized()
    os.popen('soffice -invisible "-accept=socket,host=localhost,port=2002;urp;"')
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()