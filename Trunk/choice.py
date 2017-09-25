"""
    File created by Emili Zubillaga
    CubaTronik Project 2017
"""

import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from gui.MenuOrDiy import *
from gui.SignInPassword import *
from gui.Diy import *
from gui.Menu import *
from loadFiles import *


class MenuOrDiy(QWidget,Ui_MenuOrDiy):
    def __init__(self, parent = None):
        super(MenuOrDiy, self).__init__(parent)
        self.setupUi(self)
        self.setButtonsIcons()

    def setButtonsIcons(self):
        bigIconSize = 64
        self.pb_diy.setIcon(QIcon(os.path.join("img", "bulb-icon.png")))
        self.pb_diy.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_menu.setIcon(QIcon(os.path.join("img", "prescription-icon.png")))
        self.pb_menu.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_back.setIcon(QIcon(os.path.join("img", "arrow-back-icon.png")))
        self.pb_back.setIconSize(QSize(bigIconSize, bigIconSize))


class SignInPassword(QDialog, Ui_TypePassword):
    def __init__(self, parent = None):
        super(SignInPassword, self).__init__(parent)
        self.setupUi(self)

        QObject.connect(self.pb_cancel, SIGNAL("clicked()"), self.close)


class Diy(QWidget, Ui_DiyScreen):
    def __init__(self, parent = None):
        super(Diy, self).__init__(parent)
        self.setupUi(self)
        self.setButtonsIcons()
        self.load = loadData()

        QObject.connect(self.list_booze, SIGNAL("currentTextChanged(QString)"), self.boozeSelected)
        QObject.connect(self.list_soda, SIGNAL("currentTextChanged(QString)"), self.sodaSelected)
        QObject.connect(self.list_extraTouch, SIGNAL("currentTextChanged(QString)"), self.extraSelected)
        QObject.connect(self.pb_makeDrink, SIGNAL("clicked()"), self.sendCommand)


    def setDefaultText(self):
        self.label_booze.setText("Nothing yet...")
        self.label_soda.setText("Nothing yet...")
        self.label_extraTouch.setText("That's optional")

    def setButtonsIcons(self):
        bigIconSize = 64
        self.pb_makeDrink.setIcon(QIcon(os.path.join("img", "formula-icon.png")))
        self.pb_makeDrink.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_back.setIcon(QIcon(os.path.join("img", "arrow-back-icon.png")))
        self.pb_back.setIconSize(QSize(bigIconSize, bigIconSize))

    def fillLists(self):
        booze = self.load.loadDiyDrinks()[0]
        soda = self.load.loadDiyDrinks()[1]
        extra = self.load.loadDiyDrinks()[2]

        for item in booze:
            self.list_booze.addItem(item)
        for item in soda:
            self.list_soda.addItem(item)
        for item in extra:
            self.list_extraTouch.addItem(item)

    def clearLists(self):
        self.list_booze.clear()
        self.list_soda.clear()
        self.list_extraTouch.clear()

    def boozeSelected(self, item):
        self.label_booze.setText(item)

    def sodaSelected(self, item):
        self.label_soda.setText(item)

    def extraSelected(self, item):
        self.label_extraTouch.setText(item)

    def sendCommand(self):
        com1 = self.list_booze.currentItem()
        com2 = self.list_soda.currentItem()
        com3 = self.list_extraTouch.currentItem()
        com4 = self.level_alcohol.value()

        # Restoring the indexes to the top and unselect any Item that had been selected before.
        self.list_booze.setCurrentRow(0, QItemSelectionModel.Deselect)
        self.list_booze.setCurrentRow(-1)
        self.list_booze.setItemSelected(com1, False)
        self.list_soda.setCurrentRow(0, QItemSelectionModel.Deselect)
        self.list_soda.setCurrentRow(-1)
        self.list_soda.setItemSelected(com2, False)
        self.list_extraTouch.setCurrentRow(0, QItemSelectionModel.Deselect)
        self.list_extraTouch.setCurrentRow(-1)
        self.list_extraTouch.setItemSelected(com3, False)
        self.level_alcohol.setValue(0)
        self.setDefaultText()

        # Getting the items from each list in order to send them as a command.
        if com3 is not None:
            com3 = com3.text()
        elif com3 is None:
            com3 = "None"
        if com2 is not None:
            com2 = com2.text()
        elif com2 is None:
            com2 = "None"
        if com1 is not None:
            com1 = com1.text()
        elif com1 is None:
            com1 = "None"

    # TODO: Function that parses the drink into a position on the machine in order to send a command. Using a dictionary
class Menu(QWidget, Ui_Menu):
    def __init__(self, parent = None):
        super(Menu, self).__init__(parent)
        self.setupUi(self)
        self.setButtonsIcons()
        self.load = loadData()

        QObject.connect(self.list_mixedDrinks, SIGNAL("currentTextChanged(QString)"), self.drinkSelected)

    def setButtonsIcons(self):
        bigIconSize = 64
        self.pb_back.setIcon(QIcon(os.path.join("img", "arrow-back-icon.png")))
        self.pb_back.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_create.setIcon(QIcon(os.path.join("img", "formula-icon.png")))
        self.pb_create.setIconSize((QSize(bigIconSize, bigIconSize)))

    def fillMenuList(self):
        fullMenuList = self.load.loadMenu()
        for item in fullMenuList.keys():
            self.list_mixedDrinks.addItem(item)

    def drinkSelected(self, item):
        fullMenuList = self.load.loadMenu()
        if not str(item) == "":
            self.txt_description.setText(fullMenuList[str(item)])

    def setDefaultText(self):
        self.txt_description.setText("Choose a drink and read its description before it being prepared.")
