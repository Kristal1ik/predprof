# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table2_not666yBvjzN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PyQt5 import uic
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        uic.loadUi('true.ui', self)


        self.retranslateUi(MainWindow)



        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self..setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi
class Main(QMainWindow, Ui_MainWindow):  # Вот тут основное окно
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())