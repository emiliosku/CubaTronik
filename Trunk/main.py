"""
    File created by Emili Zubillaga
    CubaTronik Project 2017
"""


#==================
##### IMPORTS #####
#==================


from gui.NewDrinkDialogWidget import *
from gui.MainLayout import *
from gui.NewUserDialog import *
from gui.SignInPassword import *
from gui.AdminPassword import *
from gui.Blank import *
from choice import *
from admin import *
from loadFiles import *
import logging
import time
import random


# Logging feature configuratiion
logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.INFO)


#======================
##### MAIN WINDOW #####
#======================
#TODO: organize all the methods used on the sketch!!
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
        self.newDrinkDialog = NewDrinkDialogWidget()
        self.newUserDialog = createNewUser()
        self.password = SignInPassword()
        self.adminPassword = AdminPassword()
        self.data = loadData()
        self.diy = Diy()
        self.menu = Menu()
        self.adminMenu = AdminMode()
        self.positioning = Positioning()
        self.bottleName = BottleName()
        self.blank = Blank()

        """
            Menu Bar Configuration.
        """
        self.adminAction = QAction("Enter Admin Mode", self)
        self.exitAction = QAction("Exit", self)
        self.allTimeStatsAction = QAction("All Time Statistics", self)
        self.monthStatsAction = QAction("Month Statistics", self)
        self.editUserAction = QAction("Edit users", self)
        self.eraseUserAction = QAction("Erase users", self)
        self.statusBar()
        self.mainMenu = self.menuBar()

        # Configuring the Program menu.
        programMenu = self.mainMenu.addMenu("&Program")
        programMenu.addAction(self.adminAction)
        programMenu.addSeparator()
        programMenu.addAction(self.exitAction)

        # Configuring the Statistics menu
        statsMenu = self.mainMenu.addMenu("&Statistics")
        statsMenu.addAction(self.monthStatsAction)
        statsMenu.addAction(self.allTimeStatsAction)

        # Configuring the Users menu.
        userMenu = self.mainMenu.addMenu("&Users")
        userMenu.addAction(self.editUserAction)
        userMenu.addAction(self.eraseUserAction)

        """
            Signals' connections configuration.
        """
        QObject.connect(self.first.pb_newDrink, SIGNAL("clicked()"), self.refreshUsers)
        QObject.connect(self.exitAction, SIGNAL("triggered()"), sys.exit)
        QObject.connect(self.adminAction, SIGNAL("triggered()"), self.adminPassword.show)
        QObject.connect(self.adminPassword.pb_check, SIGNAL("clicked()"), self.checkAdminPass)
        QObject.connect(self.adminPassword.pb_cancel, SIGNAL("clicked()"), self.closeAdminPopUp)
        QObject.connect(self.bottleName.pb_continue, SIGNAL("clicked()"), self.adminPositioning)
        QObject.connect(self.newDrinkDialog.list_usersAvailable, SIGNAL("itemClicked(QListWidgetItem*)"),
                        self.passwordDialog)
        QObject.connect(self.adminMenu.pb_exit, SIGNAL("clicked()"), self.toFirstMenu)
        QObject.connect(self.adminMenu.pb_bottlePositioning, SIGNAL("clicked()"), self.bottleNameDialog)
        QObject.connect(self.blank.movie, SIGNAL("finished()"), self.closeBlank)
        QObject.connect(self.positioning.pb_exit, SIGNAL("clicked()"), self.toAdminMenu)
        QObject.connect(self.newDrinkDialog.pb_back, SIGNAL("clicked()"), self.toFirstMenu)
        QObject.connect(self.newDrinkDialog.pb_newUser, SIGNAL("clicked()"), self.popupNewUser)
        QObject.connect(self.newUserDialog.pb_cancel, SIGNAL("clicked()"), self.newUserDialog.close)
        QObject.connect(self.newUserDialog.pb_create, SIGNAL("clicked()"), self.getUserBio)
        QObject.connect(self.newDrinkDialog.pb_guest, SIGNAL("clicked()"), self.guestAccess)
        QObject.connect(self.password.pb_cancel, SIGNAL("clicked()"), self.password.close)
        QObject.connect(self.password.pb_signIn, SIGNAL("clicked()"), self.checkPass)
        QObject.connect(self.second.pb_back, SIGNAL("clicked()"), self.toUserChoiceMenu)
        QObject.connect(self.second.pb_diy, SIGNAL("clicked()"), self.diyMenu)
        QObject.connect(self.second.pb_menu, SIGNAL("clicked()"), self.drinksMenu)
        QObject.connect(self.diy.pb_back, SIGNAL("clicked()"), self.secondMenu)
        QObject.connect(self.menu.pb_back, SIGNAL("clicked()"), self.secondMenu)
        QObject.connect(self.newDrinkDialog.pb_guest, SIGNAL("clicked()"), self.data.loadMenu)

        self.central.addWidget(self.first)
        self.central.addWidget(self.second)
        self.central.addWidget(self.diy)
        self.central.addWidget(self.menu)
        self.central.addWidget(self.newDrinkDialog)
        self.central.addWidget(self.adminMenu)
        self.central.addWidget(self.positioning)


    def toFirstMenu(self):
        if self.mainMenu.isHidden():
            self.mainMenu.show()
        self.central.setCurrentWidget(self.first)

    def toUserChoiceMenu(self):
        self.refreshUsers()

    def toAdminMenu(self):
        self.central.setCurrentWidget(self.adminMenu)

    def popupNewUser(self):
        self.newUserDialog.show()
        self.newUserDialog.list_profilePicture.setCurrentRow(0, QItemSelectionModel.Deselect)
        self.newUserDialog.list_profilePicture.setCurrentRow(-1)

    def guestAccess(self):
        self.currentUser = "Guest"
        self.secondMenu()

    def checkAdminPass(self):
        password = self.adminPassword.txt_password.text()
        if password == "admin1234":
            self.mainMenu.hide()
            self.central.setCurrentWidget(self.adminMenu)
            self.adminPassword.txt_password.clear()
            self.adminPassword.close()
        elif password == "69beicon69":
            dir = os.path.join(os.getcwd(), "log/tenor.gif")
            self.blank.label_gif.setMovie(self.blank.movie)
            self.blank.show()
            self.blank.movie.start()
            self.adminPassword.txt_password.clear()
        else:
            QMessageBox.warning(self, "Wrong Password", "The password does not match. Please, type a valid password",
                                QMessageBox.Ok)

    def closeBlank(self):
        self.blank.movie.stop()
        self.blank.close()
        QMessageBox.information(self, "Easter Egg", "Be proud of yourself, you have found an easter egg!",
                                QMessageBox.Close)

    def closeAdminPopUp(self):
        self.adminPassword.txt_password.clear()
        self.adminPassword.close()

    def adminPositioning(self):
        bottle = self.bottleName.txt_bottleName.text()
        if not bottle == "":
            choice = QMessageBox.question(self, "Check bottle name",
                                          "Are you sure that \"%s\" is the bottle you want to register?" %bottle,
                                          QMessageBox.Yes|QMessageBox.No)
            if choice == QMessageBox.Yes:
                self.bottleName.txt_bottleName.clear()
                self.bottleName.close()
                self.positioning.label_bottleName.setText(bottle)
                self.central.setCurrentWidget(self.positioning)
        else:
            QMessageBox.warning(self, "No bottle name", "A name is needed in order to position a bottle.",
                                QMessageBox.Ok)

    def bottleNameDialog(self):
        self.bottleName.show()





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
        self.directory = "%s/log/%s.txt" % (os.getcwd(), self.currentUser)
        readData = open(self.directory, "r")
        self.lines = readData.readlines()
        readData.close()
        pattern = re.compile(r'<SIGNIN>(\d*)')
        for line in self.lines:
            if pattern.search(line):
                signIn = int(pattern.findall(line)[0])
                date = time.time()
                result = self.checkEightHours(date, signIn)
        if not result:
            self.password.txt_pw.clear()
            self.password.show()
        else:
            self.newDrinkDialog.close()
            self.secondMenu()

    def getUserBio(self):
        name = self.newUserDialog.txt_newUserName.text()
        password1 = self.newUserDialog.txt_newUserPassword.text()
        password2 = self.newUserDialog.txt_newUserRepeatPassword.text()
        picture = self.newUserDialog.list_profilePicture.currentRow()

        if name == "":
            # User Name missing.
            QMessageBox.warning(self, "User Name Error","A user name is needed to create a new user.", QMessageBox.Ok)
        else:
            #TODO: check if the user name exists or not.
            # User Name field filled in.
            if password1 == "" or password2 == "":
                # One or more password fields is empty.
                QMessageBox.warning(self, "Password Error","One or more Password fields is empty. Check your Password.",
                                    QMessageBox.Ok)
            elif password1 != "" and password2 != "":
                # Both password fields are filled.
                if password1 != password2:
                    # Both password fields are not equal.
                    QMessageBox.warning(self, "Passwords don't match",
                                        "The passwords you type do not match. Please, check your password",
                                        QMessageBox.Ok)
                else:
                    # Both password fields are equal.
                    if picture == -1:
                        # Missing profile picture.
                        choice = QMessageBox.question(self, "Info", "A random profile picture will be assigned.\nAre you sure?",
                                             QMessageBox.Yes | QMessageBox.Cancel)
                        if choice == QMessageBox.Yes:
                            picture = random.randint(0, self.newUserDialog.pictures)
                            self.data.saveInfo(name, password1, picture)
                            self.currentUser = name
                            self.secondMenu()
                            self.cleanUpFields()

                            self.newUserDialog.close()
                        else:
                            pass
                    else:
                        self.data.saveInfo(name, password1, picture)
                        self.currentUser = name
                        self.secondMenu()
                        self.cleanUpFields()

                        self.newUserDialog.close()


    def cleanUpFields(self):
        """
            Clean PopUp fields.
        """
        self.newUserDialog.txt_newUserName.clear()
        self.newUserDialog.txt_newUserPassword.clear()
        self.newUserDialog.txt_newUserRepeatPassword.clear()
        self.newUserDialog.list_profilePicture.clearSelection()



    # CHECK IF THE PASSWORD ENTERED CORRESPONDS WITH THE USER'S PASSWORD.
    def checkPass(self):
        pw = self.password.txt_pw.text()
        self.password.txt_pw.clear()
        pattern = re.compile(r'<PASSWORD>(\w*)\n')
        for line in self.lines:
            if pattern.search(line):
                if pw == pattern.findall(line)[0]:
                    appendData = open(self.directory, "a")
                    appendData.write("<SIGNIN>%d\n\n" % (time.time()))
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
        result = currentTime - pastTime
        if result >= 36000:
            return False
        else:
            return True

    def refreshUsers(self):
        self.newDrinkDialog.refreshUsers()
        self.central.setCurrentWidget(self.newDrinkDialog)


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



#=====================
#####  NEW DRINK #####
#=====================

class NewDrinkDialogWidget(QWidget, Ui_userSelectionDialogWidget):
    def __init__(self, parent = None):
        super(NewDrinkDialogWidget, self).__init__(parent)
        self.setupUi(self)
        self.setButtonsIcons()

        self.load = loadData()
        self.list = self.load.loadProfilePictures()

    def setButtonsIcons(self):
        mediumIconSize = 32
        bigIconSize = 64
        self.pb_newUser.setIcon(QIcon(os.path.join("img", "plus-icon.png")))
        self.pb_newUser.setIconSize(QSize(bigIconSize, bigIconSize))
        self.pb_guest.setIcon(QIcon(os.path.join("img", "Barney-icon.png")))
        self.pb_guest.setIconSize(QSize(mediumIconSize, mediumIconSize))
        self.pb_back.setIcon(QIcon(os.path.join("img", "arrow-back-icon.png")))
        self.pb_back.setIconSize(QSize(bigIconSize, bigIconSize))

    # THIS FUNCTION REFRESHES THE USER'S LIST.
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


#=====================
#####  NEW USER  #####
#=====================

class createNewUser(QDialog, Ui_NewUserDialog):
    def __init__(self, parent = None):
        super(createNewUser, self).__init__(parent)
        self.setupUi(self)
        self.pictures = 0

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
            self.pictures += 1
        #TODO: save the number of pictures on a file for updating purposes.
        self.list_profilePicture.show()


class SignInPassword(QDialog, Ui_TypePassword):
    def __init__(self, parent = None):
        super(SignInPassword, self).__init__(parent)
        self.setupUi(self)

class AdminPassword(QDialog, Ui_AdminPass):
    def __init__(self, parent = None):
        super(AdminPassword, self).__init__(parent)
        self.setupUi(self)

class Blank(QDialog, Ui_EasterEgg):
    def __init__(self, parent = None):
        super(Blank, self).__init__(parent)
        self.setupUi(self)

        self.movie = QMovie(os.path.join(os.getcwd(), "log/tenor.gif"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.processEvents()
    main = MainWindow()
    main.resize(1024, 600)
    main.setWindowTitle("CubaTronik Project")
    main.show()
    app.setWindowIcon(QIcon(os.path.join("img", "beer-icon.png")))
    sys.exit(app.exec_())