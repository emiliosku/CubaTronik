"""
    File created by Emili Zubillaga
    CubaTronik Project
"""

import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import logging
from gui.MainLayout import *
from gui.NewDrinkDialog import *


logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.INFO)


class MainController(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        QtCore.QObject.connect(self.pb_newDrink, QtCore.SIGNAL("clicked()"), self.createDialog)

    def createDialog(self):
        self.newUser = UserDialog()
        self.newUser.show()

class UserDialog(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":
    # Launch GUI
    app = QApplication(sys.argv)
    app.processEvents()
    main = MainController()
    main.show()
    app.setWindowIcon(QIcon(os.path.join("img", "beer-icon.png")))
    sys.exit(app.exec_())



