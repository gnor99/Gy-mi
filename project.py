#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1147, 754)

        applestack = [] 
        grapesstack = []
        strawberrystack = []
        peachstack = []
        plumstack = []
        pearstack = []

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.deck1 = QtWidgets.QLabel(self.centralwidget)
        self.deck1.setGeometry(QtCore.QRect(180, 100, 151, 201))
        self.deck1.setText("")
        self.deck1.setPixmap(QtGui.QPixmap("cards/empty.png"))
        self.deck1.setScaledContents(True)
        self.deck1.setObjectName("deck1")

        self.deck2 = QtWidgets.QLabel(self.centralwidget)
        self.deck2.setGeometry(QtCore.QRect(660, 90, 151, 201))
        self.deck2.setText("")
        self.deck2.setPixmap(QtGui.QPixmap("cards/empty.png"))
        self.deck2.setScaledContents(True)
        self.deck2.setObjectName("deck2")

        self.applelabel = QtWidgets.QLabel(self.centralwidget)
        self.applelabel.setGeometry(QtCore.QRect(30, 430, 151, 201))
        self.applelabel.setText("")
        self.applelabel.setPixmap(QtGui.QPixmap("cards/empty.png"))
        self.applelabel.setScaledContents(True)
        self.applelabel.setObjectName("applelabel")

        self.grapeslabel = QtWidgets.QLabel(self.centralwidget)
        self.grapeslabel.setGeometry(QtCore.QRect(390, 430, 151, 201))
        self.grapeslabel.setText("")
        self.grapeslabel.setPixmap(QtGui.QPixmap("cards/empty.png"))
        self.grapeslabel.setScaledContents(True)
        self.grapeslabel.setObjectName("grapeslabel")

        self.strawberrylabel = QtWidgets.QLabel(self.centralwidget)
        self.strawberrylabel.setGeometry(QtCore.QRect(570, 430, 151, 201))
        self.strawberrylabel.setText("")
        self.strawberrylabel.setPixmap(QtGui.QPixmap("cards/empty.png"))
        self.strawberrylabel.setScaledContents(True)
        self.strawberrylabel.setObjectName("strawberrylabel")

        self.peachlabel = QtWidgets.QLabel(self.centralwidget)
        self.peachlabel.setGeometry(QtCore.QRect(210, 430, 151, 201))
        self.peachlabel.setText("")
        self.peachlabel.setPixmap(QtGui.QPixmap("cards/empty.png"))
        self.peachlabel.setScaledContents(True)
        self.peachlabel.setObjectName("peachlabel")

        self.plumlabel = QtWidgets.QLabel(self.centralwidget)
        self.plumlabel.setGeometry(QtCore.QRect(750, 430, 151, 201))
        self.plumlabel.setText("")
        self.plumlabel.setPixmap(QtGui.QPixmap("cards/empty.png"))
        self.plumlabel.setScaledContents(True)
        self.plumlabel.setObjectName("plumlabel")

        self.pearlabel = QtWidgets.QLabel(self.centralwidget)
        self.pearlabel.setGeometry(QtCore.QRect(930, 430, 151, 201))
        self.pearlabel.setText("")
        self.pearlabel.setPixmap(QtGui.QPixmap("cards/empty.png"))
        self.pearlabel.setScaledContents(True)
        self.pearlabel.setObjectName("pearlabel")

        self.left_deck, self.right_deck =self.deckgenerator()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 380, 67, 17))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 380, 41, 17))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 380, 67, 17))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 380, 91, 17))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(790, 380, 67, 17))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(980, 380, 67, 17))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(200, 320, 151, 25))
        self.Button1.setObjectName("Button1")
        self.Button1.clicked.connect(lambda: self.putinstack(self.left_deck, self.right_deck, applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack))

        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(690, 320, 151, 25))
        self.Button2.setObjectName("Button2")
        self.Button2.clicked.connect(lambda: self.putinstack(self.right_deck, self.left_deck, applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1147, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





        #self.putinstack(applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack) 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Apple"))
        self.label_2.setText(_translate("MainWindow", "Peach"))
        self.label_3.setText(_translate("MainWindow", "Grapes"))
        self.label_4.setText(_translate("MainWindow", "Strawberry"))
        self.label_5.setText(_translate("MainWindow", "Plum"))
        self.label_6.setText(_translate("MainWindow", "Pear"))
        self.Button1.setText(_translate("MainWindow", "Draw from this deck"))
        self.Button2.setText(_translate("MainWindow", "Draw from this deck"))

    #def clicked(self, button):


    def deckgenerator(self):

        fruits = ['apple','grapes', 'strawberry', 'peach', 'plum', 'pear'] #ennyi gyümölcs van

        left_deck = []
        right_deck = []

        for i in fruits: #Ennyi gyümölcs van
            for j in range(5): #Számozás
                for k in range(4): # Mindegyik kártyából ennyi van
                    left_deck.append(i + '_' + str(j+1)) #létrehoz egy kátyát úgy hogy elöször szerepel a gyümölcs és utána hogy hányas számú a kártya

        random.shuffle(left_deck) #megkeveri a kártyákat

        for i in range(40): #az egyszemélyes játéknál 40 lapot vissza kell tenni a dobozba
            left_deck.pop(0)

        for i in range(40): #ketté szedjük a paklit
            right_deck.append(left_deck.pop(0)) 

        self.deck1.setPixmap(QtGui.QPixmap("cards/" +  left_deck[0] +".png"))
        self.deck2.setPixmap(QtGui.QPixmap("cards/" +  right_deck[0] +".png"))

        return left_deck, right_deck

    

    def putinstack(self, choosendeck, otherdeck, applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack):
        #ez belerakja a kiválasztott kártyákat a tárolokba majd kiírja azokat
        card = choosendeck[0]

        if card[:4] == "appl" :
            applestack.append(card)
            self.applelabel.setPixmap(QtGui.QPixmap("cards/" +  applestack[0] +".png"))
        elif card[:4] == "grap" :
            grapesstack.append(card)
            self.grapeslabel.setPixmap(QtGui.QPixmap("cards/" +  grapesstack[0] +".png"))
        elif card[:4] == "stra" :
            strawberrystack.append(card)
            self.strawberrylabel.setPixmap(QtGui.QPixmap("cards/" +  strawberrystack[0] +".png"))
        elif card[:4] == "peac" :
            peachstack.append(card)
            self.peachlabel.setPixmap(QtGui.QPixmap("cards/" +  peachstack[0] +".png"))
        elif card[:4] == "plum" :
            plumstack.append(card)
            self.plumlabel.setPixmap(QtGui.QPixmap("cards/" +  plumstack[0] +".png"))
        elif card[:4] == "pear" :
            pearstack.append(card)
            self.pearlabel.setPixmap(QtGui.QPixmap("cards/" +  pearstack[0] +".png"))

        choosendeck.pop(0)
        otherdeck.pop(0)

        self.deck1.setPixmap(QtGui.QPixmap("cards/" +  self.left_deck[0] +".png"))
        self.deck2.setPixmap(QtGui.QPixmap("cards/" +  self.right_deck[0] +".png"))

        """
    def draw(self, left_deck, right_deck):
            first = self.left_deck.pop(0) #kiveszi az elso kartyát az elsö paklibol aka huz egy lapot
   

            sec = self.right_deck.pop(0) #kiveszi az elso kartyát a masodik paklibol aka huz egy lapot


        return first, sec
        """

if __name__ == "__main__":
    import sys

    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


    

    

    allstack = [applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack]
