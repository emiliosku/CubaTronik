# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainLayout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(842, 590)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pb_newDrink = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_newDrink.sizePolicy().hasHeightForWidth())
        self.pb_newDrink.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Rainbow Bridge Personal Use"))
        font.setPointSize(26)
        self.pb_newDrink.setFont(font)
        self.pb_newDrink.setObjectName(_fromUtf8("pb_newDrink"))
        self.horizontalLayout.addWidget(self.pb_newDrink)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 842, 26))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuAdmin = QtGui.QMenu(self.menuBar)
        self.menuAdmin.setObjectName(_fromUtf8("menuAdmin"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionEnter_Admin_Mode = QtGui.QAction(MainWindow)
        self.actionEnter_Admin_Mode.setObjectName(_fromUtf8("actionEnter_Admin_Mode"))
        self.menuAdmin.addAction(self.actionEnter_Admin_Mode)
        self.menuBar.addAction(self.menuAdmin.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CubaTronik", None))
        self.pb_newDrink.setText(_translate("MainWindow", "New drink", None))
        self.menuAdmin.setTitle(_translate("MainWindow", "Admin", None))
        self.actionEnter_Admin_Mode.setText(_translate("MainWindow", "Enter Admin Mode", None))

