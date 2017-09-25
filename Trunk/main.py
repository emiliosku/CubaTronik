"""
    File created by Emili Zubillaga
    CubaTronik Project 2017
"""


#==================
##### IMPORTS #####
#==================


import re
import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from gui.NewDrinkDialog import *
from gui.MainLayout import *
from gui.NewUserDialog import *
from choice import *
from loadFiles import *
import logging
import time

# Logging feature configuratiion
logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.INFO)


#======================
##### MAIN WINDOW #####
#======================

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow,self).__init__(parent)
        self.central = QStackedWidget()
        self.setCentralWidget(self.central)

        self.currentUser = ""
        self.directory = ""
        self.lines = []

        self.first = MainLayout()
        self.second = MenuOrDiy()
        self.newDrinkDialog = NewDrinkDialog()
        self.newUserDialog = NewUserDialog()
        self.myThread = NewUserAdded()
        self.myThread.start()
        self.data = loadData()
        self.password = SignInPassword()
        self.diy = Diy()
        self.menu = Menu()

        """
            Menu Bar Configuration.
        """
        self.adminAction = QAction("Enter Admin Mode", self)
        self.exitAction = QAction("Exit", self)
        self.allTimeStatsAction = QAction("All Time Statistics", self)
        self.monthStatsAction = QAction("Month Statistics", self)
        self.statusBar()
        mainMenu = self.menuBar()

        # Configuring the Program menu.
        programMenu = mainMenu.addMenu("&Program")
        programMenu.addAction(self.adminAction)
        programMenu.addSeparator()
        programMenu.addAction(self.exitAction)

        # Configuring the Statistics menu
        statsMenu = mainMenu.addMenu("&Statistics")
        statsMenu.addAction(self.monthStatsAction)
        statsMenu.addAction(self.allTimeStatsAction)

        """
            Signals' connections configuration.
        """
        QObject.connect(self.first.pb_newDrink, SIGNAL("clicked()"), self.newDrinkDialog.show)
        QObject.connect(self.exitAction, SIGNAL("triggered()"), sys.exit)
        QObject.connect(self.myThread, SIGNAL("newUser"), self.newDrinkDialog.refreshUsers)
        QObject.connect(self.newDrinkDialog.list_usersAvailable, SIGNAL("itemClicked(QListWidgetItem*)"),
                        self.passwordDialog)
        QObject.connect(self.password.pb_signIn, SIGNAL("clicked()"), self.checkPass)
        QObject.connect(self.second.pb_back, SIGNAL("clicked()"), self.firstMenu)
        QObject.connect(self.second.pb_diy, SIGNAL("clicked()"), self.diyMenu)
        QObject.connect(self.second.pb_menu, SIGNAL("clicked()"), self.drinksMenu)
        QObject.connect(self.diy.pb_back, SIGNAL("clicked()"), self.secondMenu)
        QObject.connect(self.menu.pb_back, SIGNAL("clicked()"), self.secondMenu)
        QObject.connect(self.newDrinkDialog.pb_guest, SIGNAL("clicked()"), self.data.loadMenu)

        self.central.addWidget(self.first)
        self.central.addWidget(self.second)
        self.central.addWidget(self.diy)
        self.central.addWidget(self.menu)

    # SETTING UP OF THE SECOND MENU ON THE MAIN WIDGET.
    def secondMenu(self):
        self.central.setCurrentWidget(self.second)
        self.second.label_userName.setText(self.currentUser)

    # SETTING UP OF THE DIY MENU ON THE MAIN WIDGET.
    def diyMenu(self):
        self.diy.clearLists()
        self.diy.fillLists()
        self.central.setCurrentWidget(self.diy)
        self.diy.list_booze.setCurrentRow(-1)
        self.diy.list_soda.setCurrentRow(-1)
        self.diy.list_extraTouch.setCurrentRow(-1)
        self.diy.level_alcohol.setValue(0)
        self.diy.setDefaultText()

    def drinksMenu(self):
        self.menu.list_mixedDrinks.clear()
        self.menu.fillMenuList()
        self.central.setCurrentWidget(self.menu)
        self.menu.list_mixedDrinks.setCurrentRow(-1)
        self.menu.setDefaultText()


    # SETTING UP OF THE FIRST MENU ON THE MAIN WIDGET.
    def firstMenu(self):
        self.central.setCurrentWidget(self.first)

    # POP UP OF THE PASSWORD DIALOG WHEN AUTHENTICATION IS NEEDED.
    def passwordDialog(self, userName):
        self.newDrinkDialog.list_usersAvailable.setItemSelected(userName, False)
        self.newDrinkDialog.list_usersAvailable.setCurrentRow(0, QItemSelectionModel.Deselect)
        result = False
        self.currentUser = str(userName.text())
        self.directory = "%s\\log\\%s.txt" % (os.getcwd(), self.currentUser)
        readData = open(self.directory, "r")
        self.lines = readData.readlines()
        readData.close()
        pattern = re.compile(r'<SIGNIN>(\d*)-(\d*)_(\d*):(\d*):(\d*)')
        for line in self.lines:
            if pattern.search(line):
                signIn = pattern.findall(line)[0]
                lastSignIn = [int(signIn[0]), int(signIn[1]), int(signIn[2]),
                              int(signIn[3]), int(signIn[4])]
                date = time.localtime(time.time())
                currentTime = [date[7], (date[0] % 100), date[3], date[4], date[5]]
                result = self.checkEightHours(currentTime, lastSignIn)
        if not result:
            self.password.txt_pw.clear()
            self.password.show()
        else:
            self.newDrinkDialog.close()
            self.secondMenu()

    # CHECK IF THE PASSWORD ENTERED CORRESPONDS WITH THE USER'S PASSWORD.
    def checkPass(self):
        pw = self.password.txt_pw.text()
        self.password.txt_pw.clear()
        pattern = re.compile(r'<PASSWORD>(\w*)\n')
        for line in self.lines:
            if pattern.search(line):
                if pw == pattern.findall(line)[0]:
                    appendData = open(self.directory, "a")
                    date = time.localtime(time.time())
                    appendData.write("<SIGNIN>%d-%d_%d:%d:%d\n\n" % (date[7], (date[0] % 100),
                                                                    date[3], date[4], date[5]))
                    self.newDrinkDialog.close()
                    self.secondMenu()
                    self.password.close()
                    break
                else:
                    self.password.close()
                    QMessageBox.warning(self, "Wrong Password", "The password you typed is not correct.\n"
                                                                "Please, rewrite your password and try again.",
                                        QMessageBox.Ok)
                    self.password.show()
            else:
                pass

    # CHECK IF AUTHENTICATION IS NEEDED WHEN LOGINS ARE DONE BETWEEN 10 HOURS EACH OR NOT
    def checkEightHours(self, currentTime, pastTime):
        result = [0, 0, 0, 0, 0]
        leapYear = False
        check = False
        sec = currentTime[4] - pastTime[4]
        if sec < 0:
            result[4] = 60 + sec
            pastTime[3] = pastTime[3] + 1
        elif sec > 0:
            result[4] = sec

        min = currentTime[3] - pastTime[3]
        if min < 0:
            result[3] = 60 + min
            pastTime[2] = pastTime[2] + 1
        elif min > 0:
            result[3] = min

        hours = currentTime[2] - pastTime[2]
        if hours < 0:
            result[2] = 24 + hours
            pastTime[0] = pastTime[0] + 1
        elif hours > 0:
            result[2] = hours

        if currentTime[1] % 400 == 0 or currentTime[1] % 4 == 0:
            leapYear = True
        days = currentTime[0] - pastTime[0]
        if days < 0:
            if leapYear:
                result[0] = (366 - currentTime[0]) + pastTime[0]
            else:
                result[0] = (365 - currentTime[0]) + pastTime[0]
            pastTime[1] = pastTime[1] + 1
        elif days > 0:
            result[0] = days

        result[1] = currentTime[1] - pastTime[1]

        if result[2] < 10 and result[1] == 0 and result[0] == 0:
            check = True

        return check


#=====================
##### FIRST MENU #####
#=====================

class MainLayout(QWidget, Ui_MainLayout):
    def __init__(self, parent = None):
        super(MainLayout, self).__init__(parent)
        self.setupUi(self)
        self.setButtonsIcons()

    def setButtonsIcons(self):
        bigIconSize = 64
        self.pb_newDrink.setIcon(QIcon(os.path.join("img", "beer-icon.png")))
        self.pb_newDrink.setIconSize(QSize(bigIconSize, bigIconSize))


#===============================
##### USER SELECTION DIAOG #####
#===============================

class NewDrinkDialog(QDialog, Ui_userSelectionDialog):
    def __init__(self, parent = None):
        super(NewDrinkDialog, self).__init__(parent)
        self.setupUi(self)
        self.setButtonsIcons()
        self.newUser = NewUserDialog()
        self.load = loadData()
        self.list = self.load.loadProfilePictures()

        QObject.connect(self.pb_cancel, SIGNAL("clicked()"), self.close)
        QObject.connect(self.pb_newUser, SIGNAL("clicked()"), self.popUpDialogCreate)

    def setButtonsIcons(self):
        mediumIconSize = 32
        bigIconSize = 64
        self.pb_newUser.setIcon(QIcon(os.path.join("img", "plus-icon.png")))
        self.pb_newUser.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_guest.setIcon(QIcon(os.path.join("img", "Barney-icon.png")))
        self.pb_guest.setIconSize(QSize(mediumIconSize, mediumIconSize))

    def popUpDialogCreate(self):
        self.newUser.show()

    # THIS FUNCTION REFRESHES THE USER'S LIST AUTOMATICALLY WHEN A USER IS ADDED (THANKS TO NEW USER ADDED THREAD.
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
        QObject.connect(self.pb_cancel, SIGNAL("clicked()"), self.close)
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
            if self.usersNumber != len(self.load.refreshData()):
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