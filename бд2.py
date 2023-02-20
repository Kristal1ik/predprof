# -*- coding: utf-8 -*-

import pymysql
import PyQt5
from datetime import date
import http.client
import json
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import pyqtgraph as pg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from PyQt5.QtWidgets import QApplication, QWidget



class Temp_data:
    ip_1 = ""
    ip_2 = ""
    id = 0
class Canvas(FigureCanvas):
    def __init__(self, x, y):
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=200)
        super().__init__(fig)
        self.ax.plot(x, y)
        self.ax.set(xlabel='время (с)', ylabel='угол, \u00B0',
                    title='График заезда')
        self.setWindowTitle("График зависимости угла от времени")
        self.ax.grid()
class Canvas2(FigureCanvas):
    def __init__(self, x1, y1, x2, y2):
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=200)
        super().__init__(fig)
        self.ax.plot(x1, y1)
        self.ax.plot(x2, y2)

        self.ax.set(xlabel='время (с)', ylabel='угол, \u00B0',
                    title='График заезда')
        self.setWindowTitle("График зависимости угла от времени")
        self.ax.grid()

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
        Form.setWindowTitle(QCoreApplication.translate("Form",
                                                       u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c соревнование",
                                                       None))
        self.label.setText(QCoreApplication.translate("Form",
                                                      u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u043e\u0440\u0435\u0432\u043d\u043e\u0432\u0430\u043d\u0438\u044f",
                                                      None))
        self.label_2.setText(QCoreApplication.translate("Form",
                                                        u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0442\u043e\u0440\u0430",
                                                        None))
        self.label_3.setText(QCoreApplication.translate("Form",
                                                        u"\u041c\u0435\u0441\u0442\u043e \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f",
                                                        None))
        self.pushButton.setText(
            QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi


class Ui_Form_Race(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(569, 583)
        self.name_race = QPlainTextEdit(Form)
        self.name_race.setGeometry(QRect(280, 10, 281, 41))
        font = QFont()
        font.setPointSize(12)
        self.name_race.setFont(font)
        self.name_race.setObjectName("name_race")
        self.label = QLabel(Form)
        self.label.setGeometry(QRect(9, 10, 251, 41))
        font = QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.type_race = QLabel(Form)
        self.type_race.setGeometry(QRect(10, 90, 251, 41))
        font = QFont()
        font.setPointSize(9)
        self.type_race.setFont(font)
        self.type_race.setObjectName("type_race")
        self.label_3 = QLabel(Form)
        self.label_3.setGeometry(QRect(10, 170, 251, 41))
        font = QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pilot_1 = QPlainTextEdit(Form)
        self.pilot_1.setGeometry(QRect(280, 170, 281, 41))
        font = QFont()
        font.setPointSize(10)
        self.pilot_1.setFont(font)
        self.pilot_1.setObjectName("pilot_1")
        self.pushButton = QPushButton(Form)
        self.pushButton.setGeometry(QRect(340, 510, 221, 61))
        font = QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        lst = ['qualifying (квалификация)', 'top 32(1 / 16)', 'top 16(1 / 8)', 'top 8(четвертьфинал)',
               'semifinal(полуфинал)',
               'battle for 3rd place (заезд за 3 место)',
               'final (финал)']
        self.comboBox = QComboBox(Form)
        self.comboBox.setGeometry(QRect(280, 100, 281, 41))
        self.comboBox.setObjectName("comboBox")
        for i in range(len(lst)):
            self.comboBox.addItem(lst[i])

        self.label_4 = QLabel(Form)
        self.label_4.setGeometry(QRect(10, 250, 251, 41))
        font = QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pilot2 = QPlainTextEdit(Form)
        self.pilot2.setGeometry(QRect(280, 250, 281, 41))
        font = QFont()
        font.setPointSize(10)
        self.pilot2.setFont(font)
        self.pilot2.setObjectName("pilot2")
        self.label_5 = QLabel(Form)
        self.label_5.setGeometry(QRect(10, 330, 251, 41))
        font = QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.ip_2 = QPlainTextEdit(Form)
        self.ip_2.setGeometry(QRect(280, 410, 281, 41))
        font = QFont()
        font.setPointSize(10)
        self.ip_2.setFont(font)
        self.ip_2.setObjectName("ip_2")
        self.ip_1 = QPlainTextEdit(Form)
        self.ip_1.setGeometry(QRect(280, 330, 281, 41))
        font = QFont()
        font.setPointSize(10)
        self.ip_1.setFont(font)
        self.ip_1.setObjectName("ip_1")
        self.label_6 = QLabel(Form)
        self.label_6.setGeometry(QRect(10, 410, 251, 41))
        font = QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить заезд"))
        self.label.setText(_translate("Form", "id Соревнования"))
        self.type_race.setText(_translate("Form", "Тип заезда"))
        self.label_3.setText(_translate("Form", "Номер пилота 1"))
        self.pushButton.setText(_translate("Form", "Добавить"))
        self.label_4.setText(_translate("Form", "Номер пилота 2"))
        self.label_5.setText(_translate("Form", "ip пилота 1"))
        self.label_6.setText(_translate("Form", "ip пилота 2"))


# вид окна с соревнованиями
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1222, 711)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QRect(0, 0, 1291, 711))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.deleteFilmButton = QPushButton(self.tab)
        self.deleteFilmButton.setGeometry(QRect(230, 10, 200, 51))
        self.deleteFilmButton.setObjectName("deleteFilmButton")
        self.addFilmButton = QPushButton(self.tab)
        self.addFilmButton.setGeometry(QRect(20, 10, 200, 51))
        self.addFilmButton.setObjectName("addFilmButton")
        self.filmsTable = QTableWidget(self.tab)
        self.filmsTable.setGeometry(QRect(20, 80, 1181, 571))
        self.filmsTable.setObjectName("filmsTable")
        self.filmsTable.setColumnCount(0)
        self.filmsTable.setRowCount(0)
        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.addFilmButton_2 = QPushButton(self.tab_2)
        self.addFilmButton_2.setGeometry(QRect(20, 10, 200, 51))
        self.addFilmButton_2.setObjectName("addFilmButton_2")
        self.startButton_3 = QPushButton(self.tab_2)
        self.startButton_3.setGeometry(QRect(230, 10, 200, 51))
        self.startButton_3.setObjectName("startButton_3")
        self.finishButton_4 = QPushButton(self.tab_2)
        self.finishButton_4.setGeometry(QRect(440, 10, 200, 51))
        self.finishButton_4.setObjectName("finishButton_4")
        self.deleteFilmButton_5 = QPushButton(self.tab_2)
        self.deleteFilmButton_5.setGeometry(QRect(650, 10, 200, 51))
        self.deleteFilmButton_5.setObjectName("deleteFilmButton_5")
        self.filmsTable_5 = QTableWidget(self.tab_2)
        self.filmsTable_5.setGeometry(QRect(20, 80, 1181, 571))
        self.filmsTable_5.setObjectName("filmsTable_5")
        self.filmsTable_5.setColumnCount(0)
        self.filmsTable_5.setRowCount(0)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.exitAction = QAction(MainWindow)
        self.exitAction.setObjectName("exitAction")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow",
                                             "\u0421\u0438\u0441\u0442\u0435\u043c\u0430 \u0441\u0443\u0434\u0435\u0439\u0441\u0442\u0432\u0430"))
        self.deleteFilmButton_5.setText(
            _translate("MainWindow", "\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u0435\u0437\u0434"))
        self.addFilmButton_2.setText(
            _translate("MainWindow", "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0435\u0437\u0434"))
        self.startButton_3.setText(
            _translate("MainWindow", "\u041d\u0430\u0440\u0438\u0441\u043e\u0432\u0430\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a"))
        self.finishButton_4.setText(_translate("MainWindow",
                                               "\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u0437\u0430\u0435\u0437\u0434"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  _translate("MainWindow", "\u0417\u0430\u0435\u0437\u0434\u044b"))
        self.addFilmButton.setText(_translate("MainWindow",
                                              "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u0440\u0435\u0432\u043d\u043e\u0432\u0430\u043d\u0438\u0435"))
        self.deleteFilmButton.setText(_translate("MainWindow",
                                                 "\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u043e\u0440\u0435\u0432\u043d\u043e\u0432\u0430\u043d\u0438\u0435"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow",
                                                                               "\u0421\u043e\u0440\u0435\u0432\u043d\u043e\u0432\u0430\u043d\u0438\u044f"))
        self.exitAction.setText(_translate("MainWindow", "Выход"))

    # retranslateUi


class Plot(QtWidgets.QMainWindow):
    def __init__(self):
        super(Plot, self).__init__()
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.graphWidget.setBackground('b')
        self.pen = pg.mkPen(color=(255, 0, 0), width=5, style=QtCore.Qt.SolidLine)


    def plot(self, arr):
        self.graphWidget.plot(arr[0], arr[1], pen=self.pen)

class AddRaceWidget(QMainWindow, Ui_Form):  # окно добавления данных о соревновании
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


class AddRaceWidget2(QMainWindow, Ui_Form_Race):  # окно добавления данных о заезде
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

    def start(self, ip):
        if ip == "":
            return
        client = http.client.HTTPConnection(ip)
        client.connect()
        client.request('GET', 'start')
        print(client.getresponse().read().decode('UTF-8'))

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
                insert_query = f'''INSERT INTO `race` (competition_id, participant_id, start, finish, telemetry, race_type) VALUES ("{self.name_race.toPlainText()}","{self.pilot_1.toPlainText()}", "{""}", "{""}", "{{}}", "{self.comboBox.currentText()}");'''
                print(insert_query)
                cursor.execute(insert_query)
                connection.commit()
                Temp_data.ip_1 = self.ip_1.toPlainText()
                Temp_data.ip_2 = self.ip_2.toPlainText()
                Temp_data.id = self.name_race.toPlainText()
                self.start(Temp_data.ip_1)
                self.start(Temp_data.ip_2)
        except ValueError:
            self.statusBar().showMessage("Неверно заполнена форма")
        else:
            self.parent().up_f2()
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


class Main(QMainWindow, Ui_MainWindow):  # Вот тут основное окно
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.up_f()
        self.addFilmButton.clicked.connect(self.af)
        self.deleteFilmButton.clicked.connect(self.df)
        self.dialogs = []
        self.exitAction.triggered.connect(self.exit)
        self.up_f2()
        self.addFilmButton_2.clicked.connect(self.af2)
        self.deleteFilmButton_5.clicked.connect(self.df2)
        self.startButton_3.clicked.connect(self.plot)
        self.finishButton_4.clicked.connect(self.finish)

    # def start(self):
    #     client = http.client.HTTPConnection(self.ip)
    #     client.connect()
    #     client.request('GET', 'start')
    #     t = client.getresponse().read().decode('UTF-8')
    #
    def plot(self):
        selected = self.filmsTable_5.selectedItems()
        if len(selected) > 1:
            self.statusBar().showMessage("Выбрано больше 2-х пилотов")
        elif len(selected) == 1:
            row = selected[0].row()
            t = list((json.loads(self.filmsTable_5.item(row, 4).text())).items())
            if len(t) == 1:
                t = np.array(t[0][1]).transpose()
                chart = Canvas(t[0], t[1])
                chart.show()
                # dialog = Plot()
                # dialog.plot(t)
            else:
                t1 = np.array(t[0][1]).transpose()
                t2 = np.array(t[1][1]).transpose()
                chart = Canvas2(t1[0], t1[1], t2[0], t2[1])

                chart.show()
                # dialog = Plot()
                # dialog.plot(t1)
                # dialog.plot(t2)


        else:
            self.statusBar().showMessage("Ничего не выбрано")


    def finish(self, ip):

        if Temp_data.ip_2 != "":
            self.saveData3(Temp_data.id, self.get_data(Temp_data.ip_2), self.get_data(Temp_data.ip_2))
        else:
            t = self.get_data(Temp_data.ip_1)
            t["Telemetry"] = "{\"" + str(t["ParticipantID"]) + "\":" + str(t["Telemetry"]) + "}"
            self.saveData2(Temp_data.id, t)

    def get_data(self, ip=""):
        client = http.client.HTTPConnection(ip)
        client.connect()
        client.request('GET', 'get_data')
        t = client.getresponse().read().decode('UTF-8')
        return dict(json.loads(t[:-2] + "]}"))

    def saveData(self, id, participantID, start, end, data):
        try:
            db = pymysql.connect(host="VH293.spaceweb.ru", user="savateevdm", password="LJJ1C&xG3GW1Z53H",
                                 db="savateevdm",
                                 port=3306)
        except:
            print("Unable to connect to db")
        with db.cursor() as cursor:
            cursor.execute(
                f"UPDATE `race` SET `start`=%s,`finish`=%s,`telemetry`=%s WHERE competition_id=%s and participant_id=%s",
                (start, end, data, id, participantID))
            db.commit()

    def saveData2(self, id, data):
        self.saveData(id, str(data['ParticipantID']), str(data['Start']), str(data['Finish']), str(data['Telemetry']))

    def saveData3(self, id, data1, data2):
        self.saveData(id, str(data1['ParticipantID']) + ";" + str(data2['ParticipantID']),
                      str(data1['Start']) + ";" + str(data2['Start']),
                      str(data1['Finish']) + ";" + str(data2['Finish']),
                      "{" + "\"" + str(data1['ParticipantID']) + "\"" + ":" + str(
                          data1['Telemetry']) + "," + """\"""" + str(
                          data2['ParticipantID'] + 1) + """\"""" + ":" + str(
                          data1['Telemetry']) + "}")

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

    def up_f2(self):
        result2 = []
        connection = pymysql.connect(
            host='VH293.spaceweb.ru.',
            port=3306,
            user='savateevdm',
            password='LJJ1C&xG3GW1Z53H',
            database='savateevdm',
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `race`"
            cursor.execute(select_all_rows)
            res2 = cursor.fetchall()
        connection.close()
        cursor.close()

        for i in res2:
            res2 = list(i.values())
            result2.append(res2)
        print(result2)

        self.filmsTable_5.setRowCount(len(result2))
        self.filmsTable_5.setColumnCount(len(result2[0]))
        self.filmsTable_5.setHorizontalHeaderLabels(
            ['ID соревнования', 'Номер участника', 'Время начала', 'Время окончания', 'Телементрия', 'Тип заезда'])

        for i, elem in enumerate(result2):
            for j, val in enumerate(elem):
                self.filmsTable_5.setItem(i, j, QTableWidgetItem(str(val)))

    def af2(self):
        dialog = AddRaceWidget2(self)
        dialog.show()

    def df2(self):
        rows = list(set([i.row() for i in self.filmsTable_5.selectedItems()]))
        ids = [self.filmsTable_5.item(i, 0).text() for i in rows]
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
                insert_query = f'''DELETE FROM `race` WHERE id = "{int(''.join(ids))}";'''
                cursor.execute(insert_query)
                connection.commit()
                print('удалена')

            connection.close()
            cursor.close()
            self.up_f2()

    def exit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())