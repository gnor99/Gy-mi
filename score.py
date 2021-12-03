#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

import sys


class Ui_ScoreWindow(object):
    """def __init__(self):
        super(Ui_ScoreWindow, self).__init__()
#        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)"""




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 40, 131, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.gif = QtWidgets.QLabel(self.centralwidget)
        self.gif.setGeometry(QtCore.QRect(110, 340, 190, 190))
        self.gif.setScaledContents(True)
        self.gif.setAlignment(QtCore.Qt.AlignCenter)
        self.gif.setObjectName("gif")

        self.pontszam = QtWidgets.QLabel(self.centralwidget)
        self.pontszam.setGeometry(QtCore.QRect(310, 440, 250, 41))
        self.pontszam.setAlignment(QtCore.Qt.AlignCenter)
        self.pontszam.setObjectName("pontok")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 120, 661, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Pontok"))



        self.pontszam.setText(_translate("MainWindow", "Gratulálok! pontot értél el!"))        
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Alma"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Szőlő"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Eper"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Barack"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Szilva"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Körte"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Pontszám"))

    def scorecounter(self, d):
        strd = str(d[1]) + str(d[2]) + str(d[3]) + str(d[4]) + str(d[5])

        if strd[0] == '0':
            return 0 

        for i in range(5):
            if int(strd[i]) > 1:
                return 0

        if strd[0] == '0':
            return 0

        elif strd[1] =='0' :
            return 1

        elif strd[2] == '0':
            return 3

        elif strd[3] == '0':
            return 5

        elif strd[4] == '0':
            return 7

        else:
            return 11 



    def scoreloadup(self, applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack):
        appledir={1:0 ,2:0 ,3:0 ,4:0 ,5:0 }
        grapesdir={1:0 ,2:0 ,3:0 ,4:0 ,5:0 }
        strawberrydir={1:0 ,2:0 ,3:0 ,4:0 ,5:0 }
        peachdir={1:0 ,2:0 ,3:0 ,4:0 ,5:0 }
        plumdir={1:0 ,2:0 ,3:0 ,4:0 ,5:0 }
        peardir={1:0 ,2:0 ,3:0 ,4:0 ,5:0 }

        if applestack != []:
            for i in applestack:
                appledir[int(i[-1])] += 1

        if grapesstack != []:
            for i in grapesstack:
                grapesdir[int(i[-1])] += 1

        if strawberrystack != []:
            for i in strawberrystack:
                strawberrydir[int(i[-1])] += 1

        if peachstack != []:
            for i in peachstack:
                peachdir[int(i[-1])] += 1

        if plumstack != []:
            for i in plumstack:
                plumdir[int(i[-1])] += 1

        if pearstack != []:
            for i in pearstack:
                peardir[int(i[-1])] += 1


        for i in range(6):
            for j in range(5):
                if i == 0:
                    self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(appledir[j+1])))
                    self.tableWidget.setItem(i,5,QtWidgets.QTableWidgetItem(str(self.scorecounter(appledir))))

                if i == 1:
                    self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(grapesdir[j+1])))
                    self.tableWidget.setItem(i,5,QtWidgets.QTableWidgetItem(str(self.scorecounter(grapesdir))))

                if i == 2:
                    self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(strawberrydir[j+1])))
                    self.tableWidget.setItem(i,5,QtWidgets.QTableWidgetItem(str(self.scorecounter(strawberrydir))))

                if i == 3:
                    self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(peachdir[j+1])))
                    self.tableWidget.setItem(i,5,QtWidgets.QTableWidgetItem(str(self.scorecounter(peachdir))))

                if i == 4:
                    self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(plumdir[j+1])))
                    self.tableWidget.setItem(i,5,QtWidgets.QTableWidgetItem(str(self.scorecounter(plumdir))))

                if i == 5:
                    self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(peardir[j+1])))
                    self.tableWidget.setItem(i,5,QtWidgets.QTableWidgetItem(str(self.scorecounter(peardir))))

        c = 0
        
        for i in range(6):
            c  += int(self.tableWidget.item(i,5).text())


        self.pontszam.setText( "Gratulálok! " + str(c) + " pontot értél el!")

        if c <= 11:
            self.movie = QMovie("gifs/???.gif")
            self.gif.setMovie(self.movie)
            self.movie.start()

        elif 11 < c <= 22:
            self.movie = QMovie("gifs/trump.gif")
            self.gif.setMovie(self.movie)
            self.movie.start()

        elif 22 < c <= 33:
            self.movie = QMovie("gifs/soso.gif")
            self.gif.setMovie(self.movie)
            self.movie.start()

        elif 33 < c <= 44:
            self.movie = QMovie("gifs/notbad.gif")
            self.gif.setMovie(self.movie)
            self.movie.start()

        elif 44 < c <= 55:
            self.movie = QMovie("gifs/good.gif")
            self.gif.setMovie(self.movie)
            self.movie.start()

        elif 55 < c < 66:
            self.movie = QMovie("gifs/great.gif")
            self.gif.setMovie(self.movie)
            self.movie.start()

        elif c == 66:
            self.movie = QMovie("gifs/noice.gif")
            self.gif.setMovie(self.movie)
            self.movie.start()


        

        
    



"""

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_ScoreWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())"""