"""
    File created by Emili Zubillaga
    CubaTronik Project 2017
"""

import re
import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import mysql.connector
from mysql.connector import errorcode
from gui.NewDrinkDialog import *
from gui.MainLayout import *
from gui.NewUserDialog import *
from choice import *
from loadFiles import *
import logging
import time

logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.INFO)

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow,self).__init__(parent)
        self.central = QStackedWidget()
        self.setCentralWidget(self.central)

        self.first = MainLayout()
        self.newDrinkDialog = NewDrinkDialog()
        self.newUserDialog = NewUserDialog()
        self.myThread = NewUserAdded()
        self.myThread.start()

        """
            Menu Bar Configuration.
        """
        self.adminAction = QAction("Enter Admin Mode", self)
        self.exitAction = QAction("Exit", self)
        self.saveAction = QAction("Save Data", self)
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
        statsMenu.addAction(self.saveAction)

        """
            Signals' connections configuration.
        """
        QObject.connect(self.first.pb_newDrink, SIGNAL("clicked()"), self.popUpDialogUsers)
        QObject.connect(self.newDrinkDialog.pb_newUser, SIGNAL("clicked()"), self.popUpDialogCreate)
        QObject.connect(self.exitAction, SIGNAL("triggered()"), self.closeApp)
        QObject.connect(self.myThread, SIGNAL("newUser"), self.newDrinkDialog.refreshUsers)

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
        self.load = loadData()
        self.myThread = NewUserAdded()
        self.list = self.load.loadProfilePictures()

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

    def refreshUsers(self):
        mediumIconSize = 32
        self.list_usersAvailable.clear()
        self.users = self.load.refreshData()
        self.list_usersAvailable.setIconSize(QSize(mediumIconSize, mediumIconSize))
        for user in self.users:
            f = open(user, "r")
            text = f.readlines()
            for line in text:
                if re.match(r'<USER>', line):
                    userName = re.findall(r'<USER>(\w*)\n', line)[0]
                if re.match(r'<PICTURE>', line):
                    picture = re.findall(r'<PICTURE>(\d*)\n', line)[0]
            icon = QIcon()
            icon.addPixmap(QPixmap(QString.fromUtf8(str(self.list[int(picture)]))), QIcon.Normal, QIcon.On)
            item = QListWidgetItem(icon, userName)
            self.list_usersAvailable.addItem(item)
        self.list_usersAvailable.show()



class NewUserDialog(QDialog, Ui_NewUserDialog):
    def __init__(self, parent = None):
        super(NewUserDialog, self).__init__(parent)
        self.setupUi(self)
        QObject.connect(self.pb_cancel, SIGNAL("clicked()"), self.closeDialog)
        QObject.connect(self.pb_create, SIGNAL("clicked()"), self.getUserBio)

        """
            Filling in the profile picture QListWidget
        """
        self.list_profilePicture.setViewMode(QtGui.QListView.IconMode)
        self.load = loadData()
        self.randomText = True
        for x in self.load.loadProfilePictures():
            icon = QIcon()
            icon.addPixmap(QPixmap(QString.fromUtf8(str(x))), QIcon.Normal, QIcon.On)
            if self.randomText:
                item = QListWidgetItem(icon, "Random")
                self.randomText = False
            else:
                item = QListWidgetItem(icon, "")
            self.list_profilePicture.addItem(item)
        self.list_profilePicture.show()

    def closeDialog(self):
        self.close()

    def getUserBio(self):
        name = self.txt_newUserName.text()
        password1 = self.txt_newUserPassword.text()
        password2 = self.txt_newUserRepeatPassword.text()
        picture = self.list_profilePicture.currentRow()
        if name == "":
            # User Name missing.
            self.missingName()
        else:
            # User Name field filled in.
            if password1 == "" or password2 == "":
                # One or more password fields is empty.
                self.missingPassword()
            elif password1 != "" and password2 != "":
                # Both password fields are filled.
                if password1 != password2:
                    # Both password fields are not equal.
                    self.matchingPasswords()
                else:
                    # Both password fields are equal.
                    if picture == 0:
                        # Missing profile picture.
                        self.missingProfilePicture()
                    else:
                        self.load.saveInfo(name, password1, picture)
                        self.close()

    def missingName(self):
        self.nameAlert = QMessageBox.warning(self, "User Name Error", "A user name is needed to create a new user.", QMessageBox.Ok)

    def missingProfilePicture(self):
        self.pictureAlert = QMessageBox.question(self, "Info", "A random profile picture will be assigned.\nAre you sure?",
                                                 QMessageBox.Yes | QMessageBox.Cancel)

    def missingPassword(self):
        self.passAlert = QMessageBox.warning(self, "Password Error", "One or more Password fields is empty. Check your Password.",
                                             QMessageBox.Ok)

    def matchingPasswords(self):
        self.matchPass = QMessageBox.warning(self, "Passwords don't match", "The passwords you type do not match. Please, check your password",
                                             QMessageBox.Ok)


class NewUserAdded(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.usersNumber = 0
        self.load = loadData()

    def __del__(self):
        self.wait()

    def run(self):
        while 1:
            time.sleep(0.5)
            if self.usersNumber < len(self.load.refreshData()):
                self.usersNumber = len(self.load.refreshData())
                self.emit(SIGNAL("newUser"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.processEvents()
    main = MainWindow()
    main.resize(700, 500)
    main.setWindowTitle("CubaTronik Project")
    main.show()
    app.setWindowIcon(QIcon(os.path.join("img", "beer-icon.png")))
    sys.exit(app.exec_())