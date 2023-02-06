# -*- coding: utf-8 -*-

import pymysql
from datetime import date

import sys
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(569, 327)
        self.name = QPlainTextEdit(Form)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(278, 10, 281, 41))
        font = QFont()
        font.setPointSize(12)
        self.name.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 10, 251, 41))
        font1 = QFont()
        font1.setPointSize(9)
        self.label.setFont(font1)
        self.name_org = QPlainTextEdit(Form)
        self.name_org.setObjectName(u"name_org")
        self.name_org.setGeometry(QRect(279, 90, 281, 41))
        self.name_org.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 251, 41))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 170, 251, 41))
        self.label_3.setFont(font1)
        self.locate = QPlainTextEdit(Form)
        self.locate.setObjectName(u"locate")
        self.locate.setGeometry(QRect(280, 170, 281, 41))
        font2 = QFont()
        font2.setPointSize(10)
        self.locate.setFont(font2)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 250, 221, 61))
        self.pushButton.setFont(font2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0435\u0437\u0434", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u043e\u0440\u0435\u0432\u043d\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0442\u043e\u0440\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041c\u0435\u0441\u0442\u043e \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi


class AddRaceWidget(QMainWindow, Ui_Form):  # окно добавления данных о заезде
    def __init__(self, a=None, f_i=None):
        super().__init__(a)
        self.setupUi(self)
        self.p = {}
        self.f_i = f_i
        if f_i is not None:
            self.pushButton.clicked.connect(self.ee)
            self.pushButton.setText('Отредактировать')
            self.setWindowTitle('Редактирование записи')
            # self.get()

        else:
            self.pushButton.clicked.connect(self.insert)

    # def get(self):
    #     i = []
    #     connection = pymysql.connect(
    #         host='VH293.spaceweb.ru.',
    #         port=3306,
    #         user='savateevdm',
    #         password='LJJ1C&xG3GW1Z53H',
    #         database='savateevdm',
    #         cursorclass=pymysql.cursors.DictCursor
    #     )
    #
    #     with connection.cursor() as cursor:
    #         select_all_rows = "SELECT * FROM `data`"
    #         cursor.execute(select_all_rows)
    #         res = cursor.fetchall()
    #     connection.close()
    #     cursor.close()
    #
    #     for i in res:
    #         res = list(i.values())
    #         i.append(res)
    #     print(i)
    #
    #     self.name.setPlainText(i[1])
    #     self.name_org.setPlainText(str(i[2]))
    #     self.locate.setPlainText(str(i[4]))

    def insert(self):
        connection = pymysql.connect(
            host='VH293.spaceweb.ru.',
            port=3306,
            user='savateevdm',
            password='LJJ1C&xG3GW1Z53H',
            database='savateevdm',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                current_date = date.today()
                insert_query = f'''INSERT INTO `data` (name_of_the_competition, date, name_of_the_organizer, location) VALUES ("{self.name.toPlainText()}", "{current_date}", "{self.name_org.toPlainText()}", "{self.locate.toPlainText()}");'''
                cursor.execute(insert_query)
                connection.commit()
        except ValueError:
            self.statusBar().showMessage("Неверно заполнена форма")
        else:
            self.parent().up_f()
            connection.close()
            cursor.close()

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main1XWyrfn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1222, 711)
        self.exitAction = QAction(MainWindow)
        self.exitAction.setObjectName(u"exitAction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.addFilmButton = QPushButton(self.centralwidget)
        self.addFilmButton.setObjectName(u"addFilmButton")
        self.addFilmButton.setGeometry(QRect(20, 20, 151, 51))
        self.deleteFilmButton = QPushButton(self.centralwidget)
        self.deleteFilmButton.setObjectName(u"deleteFilmButton")
        self.deleteFilmButton.setGeometry(QRect(190, 20, 151, 51))
        self.filmsTable = QTableWidget(self.centralwidget)
        self.filmsTable.setObjectName(u"filmsTable")
        self.filmsTable.setGeometry(QRect(20, 100, 1181, 571))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0441\u0443\u0434\u0435\u0439\u0441\u0442\u0432\u0430", None))
        self.exitAction.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.addFilmButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0435\u0437\u0434", None))
        self.deleteFilmButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u0435\u0437\u0434", None))
    # retranslateUi


class Main(QMainWindow, Ui_MainWindow):  # Вот тут основное окно
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.up_f()
        self.addFilmButton.clicked.connect(self.af)
        self.deleteFilmButton.clicked.connect(self.df)
        self.dialogs = []
        self.exitAction.triggered.connect(self.exit)

    def up_f(self):
        result = []
        connection = pymysql.connect(
            host='VH293.spaceweb.ru.',
            port=3306,
            user='savateevdm',
            password='LJJ1C&xG3GW1Z53H',
            database='savateevdm',
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `data`"
            cursor.execute(select_all_rows)
            res = cursor.fetchall()
        connection.close()
        cursor.close()

        for i in res:
            res = list(i.values())
            result.append(res)
        print(result)

        self.filmsTable.setRowCount(len(result))
        self.filmsTable.setColumnCount(len(result[0]))
        self.filmsTable.setHorizontalHeaderLabels(
            ['ID', 'Наименование соревнования', 'Дата', 'Наименование организатора', 'Место проведения'])

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.filmsTable.setItem(i, j, QTableWidgetItem(str(val)))

    def af(self):
        dialog = AddRaceWidget(self)
        dialog.show()

    def df(self):
        rows = list(set([i.row() for i in self.filmsTable.selectedItems()]))
        ids = [self.filmsTable.item(i, 0).text() for i in rows]
        if not ids:
            self.statusBar().showMessage('Выберите что-нибудь!')
            return

        else:
            self.statusBar().showMessage('')
        q = QMessageBox.question(self, '', 'Вы уверены, что хотите удалить этот элемент?',
                                     QMessageBox.Yes,
                                     QMessageBox.No)
        if q == QMessageBox.Yes:
            connection = pymysql.connect(
                host='VH293.spaceweb.ru.',
                port=3306,
                user='savateevdm',
                password='LJJ1C&xG3GW1Z53H',
                database='savateevdm',
                cursorclass=pymysql.cursors.DictCursor
            )
            print(int(''.join(ids)))

            with connection.cursor() as cursor:
                insert_query = f'''DELETE FROM `data` WHERE id = "{int(''.join(ids))}";'''
                cursor.execute(insert_query)
                connection.commit()
                print('удалена')

            connection.close()
            cursor.close()
            self.up_f()

    def exit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())