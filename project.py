#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from score import Ui_ScoreWindow
import score
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1147, 754)

        #létrehozom a gyümölcs tárolókat, amikben a kiválasztott kártyák lesznek

        applestack = [] 
        grapesstack = []
        strawberrystack = []
        peachstack = []
        plumstack = []
        pearstack = []

        MainWindow.setWindowIcon(QtGui.QIcon("cards/icon.png"))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #paklik

        self.deck1 = QtWidgets.QLabel(self.centralwidget)  # baloldali pakli
        self.deck1.setGeometry(QtCore.QRect(180, 100, 151, 201))
        self.deck1.setText("")
        self.deck1.setPixmap(QtGui.QPixmap("cards/empty.png"))
        self.deck1.setScaledContents(True)
        self.deck1.setObjectName("deck1")

        self.deck2 = QtWidgets.QLabel(self.centralwidget) #jobb oldali pakli
        self.deck2.setGeometry(QtCore.QRect(660, 90, 151, 201))
        self.deck2.setText("")
        self.deck2.setPixmap(QtGui.QPixmap("cards/empty.png"))
        self.deck2.setScaledContents(True)
        self.deck2.setObjectName("deck2")

        #tárolók képe

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

        self.left_deck, self.right_deck =self.deckgenerator() # legenerálom a paklikat

        #a tárolók feletti leírás

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(80, 380, 67, 17))
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label")

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

        # ez számolja hogy mennyi kártya van a tárolóban

        self.counter_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.counter_label_1.setGeometry(QtCore.QRect(40, 650, 140, 17))
        self.counter_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.counter_label_1.setObjectName("counter_label_1")

        self.counter_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.counter_label_2.setGeometry(QtCore.QRect(215, 650, 140, 17))
        self.counter_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.counter_label_2.setObjectName("counter_label_2")
        
        self.counter_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.counter_label_3.setGeometry(QtCore.QRect(390, 650, 140, 17))
        self.counter_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.counter_label_3.setObjectName("counter_label_3")

        self.counter_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.counter_label_4.setGeometry(QtCore.QRect(570, 650, 140, 17))
        self.counter_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.counter_label_4.setObjectName("counter_label_4")

        self.counter_label_5 = QtWidgets.QLabel(self.centralwidget)
        self.counter_label_5.setGeometry(QtCore.QRect(755, 650, 140, 17))
        self.counter_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.counter_label_5.setObjectName("counter_label_5")

        self.counter_label_6 = QtWidgets.QLabel(self.centralwidget)
        self.counter_label_6.setGeometry(QtCore.QRect(935, 650, 140, 17))
        self.counter_label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.counter_label_6.setObjectName("counter_label_6")  

        #baloldali paklihoz kiválasztó gomb      

        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(200, 320, 151, 25))
        self.Button1.setObjectName("Button1")
        self.Button1.clicked.connect(lambda: self.putinstack(self.left_deck, self.right_deck, applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack))

        #jobboldali paklihoz kiválasztó gomb

        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(690, 320, 151, 25))
        self.Button2.setObjectName("Button2")
        self.Button2.clicked.connect(lambda: self.putinstack(self.right_deck, self.left_deck, applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack))

        #mind a két pakliból eléget egy-egy lapot

        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3.setGeometry(QtCore.QRect(450, 320, 151, 25))
        self.Button3.setObjectName("Button3")
        self.Button3.clicked.connect(lambda: self.discard(self.left_deck, self.right_deck, applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack))



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1147, 22))
        self.menubar.setObjectName("menubar")

        #menüsáv

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.menuuj = QtWidgets.QMenu(self.menubar)
        self.menuuj.setObjectName("menuuj")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.menuuj.addAction(self.actionnew)
        self.menubar.addAction(self.menuuj.menuAction())

        self.actionnew.triggered.connect(lambda: self.click(MainWindow))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):

        #Itt csak a kiírt szövegek vannak

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "Alma"))
        self.label_2.setText(_translate("MainWindow", "Barack"))
        self.label_3.setText(_translate("MainWindow", "Szőlő"))
        self.label_4.setText(_translate("MainWindow", "Eper"))
        self.label_5.setText(_translate("MainWindow", "Szilva"))
        self.label_6.setText(_translate("MainWindow", "Körte"))
        self.Button1.setText(_translate("MainWindow", "Húzz ebből a pakliból"))
        self.Button2.setText(_translate("MainWindow", "Húzz ebből a pakliból"))
        self.Button3.setText(_translate("MainWindow", "Dobd el mind két kártyát"))
        self.counter_label_1.setText(_translate("MainWindow", "A pakli mérete 0"))
        self.counter_label_2.setText(_translate("MainWindow", "A pakli mérete 0"))
        self.counter_label_3.setText(_translate("MainWindow", "A pakli mérete 0"))
        self.counter_label_4.setText(_translate("MainWindow", "A pakli mérete 0"))
        self.counter_label_5.setText(_translate("MainWindow", "A pakli mérete 0"))
        self.counter_label_6.setText(_translate("MainWindow", "A pakli mérete 0"))
        self.menuuj.setTitle(_translate("MainWindow", "Játék"))
        self.actionnew.setText(_translate("MainWindow", "Új játék"))
        self.actionnew.setShortcut(_translate("MainWindow", "Ctrl+N"))

    def click(self, MainWindow):

        #Az új játék gomb triggerelt eljárás

        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        


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

        #Ez a kettő átrakja a húzópaklinak a felső lapjait az aktuálisra

        self.deck1.setPixmap(QtGui.QPixmap("cards/" +  left_deck[0] +".png"))
        self.deck2.setPixmap(QtGui.QPixmap("cards/" +  right_deck[0] +".png"))

        return left_deck, right_deck

    

    def putinstack(self, choosendeck, otherdeck, applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack):
        #ez belerakja a kiválasztott kártyákat a tárolokba majd kiírja azokat
        
        if len(choosendeck) != 0: 
            card = choosendeck[0]

            if card[:4] == "appl" :

                if len(applestack) == 5 :
                    self.pop_up_message("Alma", choosendeck, otherdeck, applestack, card, self.applelabel, self.counter_label_1)

                else:
                    applestack.append(card)
                    self.applelabel.setPixmap(QtGui.QPixmap("cards/" +  applestack[-1] +".png"))
                    self.counter_label_1.setText( "Size of this deck is " + str(len(applestack)))
                    
                    choosendeck.pop(0)
                    otherdeck.pop(0)

                if choosendeck:
                    #ez a feltétel azért kell mert van olyan eset hogy pont akkor akarja a felhasználó a hatodik gyümölcsöt belerakni a tárolóba mikor már kiürültek a paklik
                    self.deck1.setPixmap(QtGui.QPixmap("cards/" +  self.left_deck[0] +".png"))
                    self.deck2.setPixmap(QtGui.QPixmap("cards/" +  self.right_deck[0] +".png"))
                else:
                    self.deck1.setPixmap(QtGui.QPixmap("cards/empty.png"))
                    self.deck2.setPixmap(QtGui.QPixmap("cards/empty.png"))
                    self.pop_up_end(applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack)


            elif card[:4] == "grap" :
                if len(grapesstack) == 5 :
                    self.pop_up_message("Szőlő", choosendeck, otherdeck,  grapesstack,  card, self.grapeslabel, self.counter_label_3)

                else:
                    grapesstack.append(card)
                    self.grapeslabel.setPixmap(QtGui.QPixmap("cards/" +  grapesstack[-1] +".png"))
                    self.counter_label_3.setText( "Size of this deck is " + str(len(grapesstack)))

                    choosendeck.pop(0)
                    otherdeck.pop(0)

                if choosendeck:
                    self.deck1.setPixmap(QtGui.QPixmap("cards/" +  self.left_deck[0] +".png"))
                    self.deck2.setPixmap(QtGui.QPixmap("cards/" +  self.right_deck[0] +".png"))
                else:
                    self.deck1.setPixmap(QtGui.QPixmap("cards/empty.png"))
                    self.deck2.setPixmap(QtGui.QPixmap("cards/empty.png"))
                    self.pop_up_end(applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack)

            elif card[:4] == "stra" :
                if len(strawberrystack) == 5 :
                    self.pop_up_message("Eper" , choosendeck, otherdeck,  strawberrystack,  card, self.strawberrylabel, self.counter_label_4)

                else:
                    strawberrystack.append(card)
                    self.strawberrylabel.setPixmap(QtGui.QPixmap("cards/" +  strawberrystack[-1] +".png"))
                    self.counter_label_4.setText("Size of this deck is " + str(len(strawberrystack)))

                    choosendeck.pop(0)
                    otherdeck.pop(0)

                if choosendeck:
                    self.deck1.setPixmap(QtGui.QPixmap("cards/" +  self.left_deck[0] +".png"))
                    self.deck2.setPixmap(QtGui.QPixmap("cards/" +  self.right_deck[0] +".png"))
                else:
                    self.deck1.setPixmap(QtGui.QPixmap("cards/empty.png"))
                    self.deck2.setPixmap(QtGui.QPixmap("cards/empty.png"))
                    self.pop_up_end(applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack)

            elif card[:4] == "peac" :
                if len(peachstack) == 5:
                    self.pop_up_message("Barack", choosendeck, otherdeck,  peachstack,  card, self.peachlabel, self.counter_label_2)

                else:
                    peachstack.append(card)
                    self.peachlabel.setPixmap(QtGui.QPixmap("cards/" +  peachstack[-1] +".png"))
                    self.counter_label_2.setText( "Size of this deck is " + str(len(peachstack)))

                    choosendeck.pop(0)
                    otherdeck.pop(0)

                if choosendeck:
                    self.deck1.setPixmap(QtGui.QPixmap("cards/" +  self.left_deck[0] +".png"))
                    self.deck2.setPixmap(QtGui.QPixmap("cards/" +  self.right_deck[0] +".png"))
                else:
                    self.deck1.setPixmap(QtGui.QPixmap("cards/empty.png"))
                    self.deck2.setPixmap(QtGui.QPixmap("cards/empty.png"))
                    self.pop_up_end(applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack)

            elif card[:4] == "plum" :
                if len(plumstack) == 5:
                    self.pop_up_message("Szilva", choosendeck, otherdeck, plumstack, card, self.plumlabel, self.counter_label_5)

                else:
                    plumstack.append(card)
                    self.plumlabel.setPixmap(QtGui.QPixmap("cards/" +  plumstack[-1] +".png"))
                    self.counter_label_5.setText( "Size of this deck is " + str(len(plumstack)))

                    choosendeck.pop(0)
                    otherdeck.pop(0)

                if choosendeck:
                    self.deck1.setPixmap(QtGui.QPixmap("cards/" +  self.left_deck[0] +".png"))
                    self.deck2.setPixmap(QtGui.QPixmap("cards/" +  self.right_deck[0] +".png"))
                else:
                    self.deck1.setPixmap(QtGui.QPixmap("cards/empty.png"))
                    self.deck2.setPixmap(QtGui.QPixmap("cards/empty.png"))
                    self.pop_up_end(applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack)

            elif card[:4] == "pear" :
                if len(pearstack) == 5:
                    self.pop_up_message("Körte", choosendeck, otherdeck, pearstack, card, self.pearlabel, self.counter_label_6)

                else:             
                    pearstack.append(card)
                    self.pearlabel.setPixmap(QtGui.QPixmap("cards/" +  pearstack[-1] +".png"))
                    self.counter_label_6.setText( "Size of this deck is " + str(len(pearstack)))

                    choosendeck.pop(0)
                    otherdeck.pop(0)

                if choosendeck:
                    self.deck1.setPixmap(QtGui.QPixmap("cards/" +  self.left_deck[0] +".png"))
                    self.deck2.setPixmap(QtGui.QPixmap("cards/" +  self.right_deck[0] +".png"))
                else:
                    self.deck1.setPixmap(QtGui.QPixmap("cards/empty.png"))
                    self.deck2.setPixmap(QtGui.QPixmap("cards/empty.png"))
                    self.pop_up_end(applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack)


    def pop_up_end(self, applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack):

        #Mikor kifogytak a lapok akkor felugrik egy pop up üzenet hogy erről tályékoztassa a felhasználót

        msg = QMessageBox()
        msg.setWindowTitle("Vége")
        msg.setText("Elfogyott a paklikból a kártya. Nyomd meg az 'ok' gombot és nézd meg az eredményt")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)

        x = msg.exec_()

        if x == QMessageBox.Ok:
            #Itt betölti a játék végi kiértékelőt
            ui = score.Ui_ScoreWindow()
            ui.setupUi(MainWindow)
            ui.scoreloadup(applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack)

    def discard(self, choosendeck, otherdeck, applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack):
        
        #Mind a két pakliból kidob egy-egy lapot

        choosendeck.pop(0)
        otherdeck.pop(0)

        if len(choosendeck) != 0:
            self.deck1.setPixmap(QtGui.QPixmap("cards/" +  self.left_deck[0] +".png"))
            self.deck2.setPixmap(QtGui.QPixmap("cards/" +  self.right_deck[0] +".png"))
        else:
            self.deck1.setPixmap(QtGui.QPixmap("cards/empty.png"))
            self.deck2.setPixmap(QtGui.QPixmap("cards/empty.png"))
            self.pop_up_end(applestack, grapesstack, strawberrystack, peachstack, plumstack, pearstack)



    def pop_up_message(self, fruit,  choosendeck, otherdeck, stack, card, fruitlabel, counter_label):

        #Ez a pop-up üzenet figyelmeztet ha több mint 5 lapot akar belerakni a játékos egy tároloba

        msg = QMessageBox()
        msg.setWindowTitle("Válassz okosan")
        msg.setText(fruit + " gyümölcsből van már a pakliban 5 lap")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Retry|QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)


        x = msg.exec_()

        if x == QMessageBox.Retry:
            pass

        else: 
            stack.append(card)
            fruitlabel.setPixmap(QtGui.QPixmap("cards/" +  stack[-1] +".png"))
            counter_label.setText( "Size of this deck is " + str(len(stack)))

            choosendeck.pop(0)
            otherdeck.pop(0)


 

if __name__ == "__main__":
    import sys

    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())