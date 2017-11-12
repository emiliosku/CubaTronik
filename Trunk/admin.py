"""
    File created by Emili Zubillaga
    CubaTronik Project 2017
"""

import os
from PyQt4.QtCore import *
from gui.AdminMenu import *
from gui.Positioning import *
from gui.BottleName import *
from PyQt4.QtGui import *


class AdminMode(QWidget, Ui_AdminMenu):
    def __init__(self, parent = None):
        super(AdminMode, self).__init__(parent)
        self.setupUi(self)
        self.setButtonsIcons()
        self.mymenu = QMenu()

    def setButtonsIcons(self):
        bigIconSize = 64
        pass


class Positioning(QWidget, Ui_Positioning):
    def __init__(self, parent = None):
        super(Positioning, self).__init__(parent)
        self.setupUi(self)
        self.setButtonsIcons()

    def setButtonsIcons(self):
        bigIconSize = 64
        self.pb_up.setIcon(QIcon(os.path.join("img", "arrow-up-icon.png")))
        self.pb_up.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_down.setIcon(QIcon(os.path.join("img", "arrow-down-icon.png")))
        self.pb_down.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_right.setIcon(QIcon(os.path.join("img", "arrow-next-3-icon.png")))
        self.pb_right.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_left.setIcon(QIcon(os.path.join("img", "arrow-back-icon.png")))
        self.pb_left.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_fastRight.setIcon(QIcon(os.path.join("img", "arrow-forward-icon.png")))
        self.pb_fastRight.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_fastLeft.setIcon(QIcon(os.path.join("img", "arrow-rewind-icon.png")))
        self.pb_fastLeft.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_home.setIcon(QIcon(os.path.join("img", "Home-icon.png")))
        self.pb_home.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_exit.setIcon(QIcon(os.path.join("img", "arrow-back-icon.png")))
        self.pb_exit.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_fastUp.setIcon(QIcon(os.path.join("img", "arrow-upload-icon.png")))
        self.pb_fastUp.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_fastDown.setIcon(QIcon(os.path.join("img", "arrow-download-icon.png")))
        self.pb_fastDown.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_higher.setIcon(QIcon(os.path.join("img", "Add-icon.png")))
        self.pb_higher.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_lower.setIcon(QIcon(os.path.join("img", "Minus-icon.png")))
        self.pb_lower.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_finish.setIcon(QIcon(os.path.join("img", "check-1-icon.png")))
        self.pb_finish.setIconSize(QSize(bigIconSize, bigIconSize))

class BottleName(QDialog, Ui_BottleName):
    def __init__(self, parent = None):
        super(BottleName, self).__init__(parent)
        self.setupUi(self)
        self.setButtonsIcons()

        QObject.connect(self.pb_cancel, SIGNAL("clicked()"), self.close)

    def setButtonsIcons(self):
        mediumIconSize = 32
        self.pb_continue.setIcon(QIcon(os.path.join("img", "check-1-icon.png")))
        self.pb_continue.setIconSize(QSize(mediumIconSize, mediumIconSize))