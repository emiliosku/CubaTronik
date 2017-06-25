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

class Ui_userSelectionDialog(object):
    def setupUi(self, userSelectionDialog):
        userSelectionDialog.setObjectName(_fromUtf8("userSelectionDialog"))
        userSelectionDialog.setWindowModality(QtCore.Qt.NonModal)
        userSelectionDialog.setEnabled(True)
        userSelectionDialog.resize(450, 250)
        userSelectionDialog.setModal(True)
        self.horizontalLayout = QtGui.QHBoxLayout(userSelectionDialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pb_guest = QtGui.QPushButton(userSelectionDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_guest.sizePolicy().hasHeightForWidth())
        self.pb_guest.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(20)
        self.pb_guest.setFont(font)
        self.pb_guest.setAutoDefault(False)
        self.pb_guest.setObjectName(_fromUtf8("pb_guest"))
        self.verticalLayout.addWidget(self.pb_guest)
        self.list_usersAvailable = QtGui.QListWidget(userSelectionDialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(24)
        self.list_usersAvailable.setFont(font)
        self.list_usersAvailable.setObjectName(_fromUtf8("list_usersAvailable"))
        self.verticalLayout.addWidget(self.list_usersAvailable)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.pb_newUser = QtGui.QPushButton(userSelectionDialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(24)
        self.pb_newUser.setFont(font)
        self.pb_newUser.setObjectName(_fromUtf8("pb_newUser"))
        self.verticalLayout_2.addWidget(self.pb_newUser)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pb_cancel = QtGui.QPushButton(userSelectionDialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(14)
        self.pb_cancel.setFont(font)
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.verticalLayout_2.addWidget(self.pb_cancel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(userSelectionDialog)
        QtCore.QMetaObject.connectSlotsByName(userSelectionDialog)

    def retranslateUi(self, userSelectionDialog):
        userSelectionDialog.setWindowTitle(_translate("userSelectionDialog", "Choose a player", None))
        self.pb_guest.setText(_translate("userSelectionDialog", "Guest", None))
        self.pb_newUser.setText(_translate("userSelectionDialog", "New", None))
        self.pb_cancel.setText(_translate("userSelectionDialog", "Cancel", None))

