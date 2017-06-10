"""
    File created by Emili Zubillaga
    CubaTronik Project 2017
"""

import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from gui.NewDrinkDialog import *
from gui.MainLayout import *
from gui.NewUserDialog import *
from choice import *
from loadFiles import *

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow,self).__init__(parent)
        self.central = QStackedWidget()
        self.setCentralWidget(self.central)

        self.first = MainLayout()
        self.newDrinkDialog = NewDrinkDialog()
        self.newUserDialog = NewUserDialog()

        """
            Menu Bar Configuration.
        """
        self.adminAction = QAction("Enter Admin Mode", self)
        self.exitAction = QAction("Exit", self)
        self.loadAction = QAction("Load Data", self)
        self.statusBar()
        mainMenu = self.menuBar()

        # Configuring the Program menu.
        programMenu = mainMenu.addMenu("&Program")
        programMenu.addAction(self.adminAction)
        programMenu.addSeparator()
        programMenu.addAction(self.exitAction)

        # Configuring the Statistics menu
        statsMenu = mainMenu.addMenu("&Statistics")
        statsMenu.addAction(self.loadAction)

        """
            Signals' connections configuration.
        """
        QObject.connect(self.first.pb_newDrink, SIGNAL("clicked()"), self.popUpDialogUsers)
        QObject.connect(self.newDrinkDialog.pb_newUser, SIGNAL("clicked()"), self.popUpDialogCreate)
        QObject.connect(self.exitAction, SIGNAL("triggered()"), self.closeApp)

        self.central.addWidget(self.first)

    def secondMenu(self):
        self.second = MenuOrDiy()
        self.central.addWidget(self.second)
        self.central.setCurrentWidget(self.second)
        self.newDrinkDialog.close()

    def popUpDialogUsers(self):
        self.newDrinkDialog.show()

    def popUpDialogCreate(self):
        self.newUserDialog.show()


    def closeApp(self):
        sys.exit()




class MainLayout(QWidget, Ui_MainLayout):
    def __init__(self, parent = None):
        super(MainLayout, self).__init__(parent)
        self.setupUi(self)
        self.setButtonsIcons()

    def setButtonsIcons(self):
        bigIconSize = 64
        self.pb_newDrink.setIcon(QIcon(os.path.join("img", "beer-icon.png")))
        self.pb_newDrink.setIconSize(QSize(bigIconSize, bigIconSize))


class NewDrinkDialog(QDialog, Ui_userSelectionDialog):
    def __init__(self, parent = None):
        super(NewDrinkDialog, self).__init__(parent)
        self.setupUi(self)
        self.setButtonsIcons()
        self.newUser = NewUserDialog()

        QObject.connect(self.pb_cancel, SIGNAL("clicked()"), self.closeDialog)

    def setButtonsIcons(self):
        mediumIconSize = 32
        bigIconSize = 64
        self.pb_newUser.setIcon(QIcon(os.path.join("img", "plus-icon.png")))
        self.pb_newUser.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_guest.setIcon(QIcon(os.path.join("img", "Barney-icon.png")))
        self.pb_guest.setIconSize(QSize(mediumIconSize, mediumIconSize))

    def closeDialog(self):
        self.close()

class NewUserDialog(QDialog, Ui_NewUserDialog):
    def __init__(self, parent = None):
        super(NewUserDialog, self).__init__(parent)
        self.setupUi(self)
        QObject.connect(self.pb_cancel, SIGNAL("clicked()"), self.closeDialog)

        """
            Filling in the profile picture QListWidget
        """
        self.list_profilePicture.setViewMode(QtGui.QListView.IconMode)
        self.load = loadData()
        for x in self.load.loadProfilePictures():
            icon = QIcon()
            icon.addPixmap(QPixmap(QString.fromUtf8(str(x))), QIcon.Normal, QIcon.On)
            item = QListWidgetItem(icon, "")
            self.list_profilePicture.addItem(item)
        self.list_profilePicture.show()

    def closeDialog(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.processEvents()
    main = MainWindow()
    main.resize(700, 500)
    main.setWindowTitle("CubaTronik Project")
    main.show()
    app.setWindowIcon(QIcon(os.path.join("img", "beer-icon.png")))
    sys.exit(app.exec_())