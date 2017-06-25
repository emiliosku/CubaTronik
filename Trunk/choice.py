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

class MenuOrDiy(QWidget,Ui_MenuOrDiy):
    def __init__(self, parent = None):
        super(MenuOrDiy, self).__init__(parent)
        self.setupUi(self)
        self.setButtonsIcons()

    def setButtonsIcons(self):
        bigIconSize = 64
        self.pb_diy.setIcon(QIcon(os.path.join("img", "bulb-icon.png")))
        self.pb_diy.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_menu.setIcon(QIcon(os.path.join("img", "list-icon.png")))
        self.pb_menu.setIconSize(QSize(bigIconSize, bigIconSize))


class SignInPassword(QDialog, Ui_TypePassword):
    def __init__(self, parent = None):
        super(SignInPassword, self).__init__(parent)
        self.setupUi(self)

        QObject.connect(self.pb_cancel, SIGNAL("clicked()"), self.close)




