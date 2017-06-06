# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewDrinkDialog.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pb_guest = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_guest.sizePolicy().hasHeightForWidth())
        self.pb_guest.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Rainbow Bridge Personal Use"))
        font.setPointSize(14)
        self.pb_guest.setFont(font)
        self.pb_guest.setAutoDefault(False)
        self.pb_guest.setObjectName(_fromUtf8("pb_guest"))
        self.verticalLayout.addWidget(self.pb_guest)
        self.list_usersAvailable = QtGui.QListWidget(Dialog)
        self.list_usersAvailable.setObjectName(_fromUtf8("list_usersAvailable"))
        self.verticalLayout.addWidget(self.list_usersAvailable)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.pb_newUser = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Rainbow Bridge Personal Use"))
        font.setPointSize(10)
        self.pb_newUser.setFont(font)
        self.pb_newUser.setAutoDefault(False)
        self.pb_newUser.setDefault(True)
        self.pb_newUser.setObjectName(_fromUtf8("pb_newUser"))
        self.horizontalLayout.addWidget(self.pb_newUser)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "New Drink", None))
        self.pb_guest.setText(_translate("Dialog", "Guest", None))
        self.pb_newUser.setText(_translate("Dialog", "Add New User", None))

