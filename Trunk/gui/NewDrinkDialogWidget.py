# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewDrinkDialogWidget.ui'
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

class Ui_userSelectionDialogWidget(object):
    def setupUi(self, userSelectionDialogWidget):
        userSelectionDialogWidget.setObjectName(_fromUtf8("userSelectionDialogWidget"))
        userSelectionDialogWidget.resize(405, 300)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(48)
        userSelectionDialogWidget.setFont(font)
        self.horizontalLayout = QtGui.QHBoxLayout(userSelectionDialogWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.list_usersAvailable = QtGui.QListWidget(userSelectionDialogWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_usersAvailable.sizePolicy().hasHeightForWidth())
        self.list_usersAvailable.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(48)
        self.list_usersAvailable.setFont(font)
        self.list_usersAvailable.setObjectName(_fromUtf8("list_usersAvailable"))
        self.verticalLayout.addWidget(self.list_usersAvailable)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pb_guest = QtGui.QPushButton(userSelectionDialogWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_guest.sizePolicy().hasHeightForWidth())
        self.pb_guest.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pb_guest.setFont(font)
        self.pb_guest.setObjectName(_fromUtf8("pb_guest"))
        self.horizontalLayout_4.addWidget(self.pb_guest)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pb_newUser = QtGui.QPushButton(userSelectionDialogWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_newUser.sizePolicy().hasHeightForWidth())
        self.pb_newUser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pb_newUser.setFont(font)
        self.pb_newUser.setObjectName(_fromUtf8("pb_newUser"))
        self.horizontalLayout_2.addWidget(self.pb_newUser)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.pb_back = QtGui.QPushButton(userSelectionDialogWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_back.sizePolicy().hasHeightForWidth())
        self.pb_back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pb_back.setFont(font)
        self.pb_back.setObjectName(_fromUtf8("pb_back"))
        self.horizontalLayout_3.addWidget(self.pb_back)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(userSelectionDialogWidget)
        QtCore.QMetaObject.connectSlotsByName(userSelectionDialogWidget)

    def retranslateUi(self, userSelectionDialogWidget):
        userSelectionDialogWidget.setWindowTitle(_translate("userSelectionDialogWidget", "Form", None))
        self.pb_guest.setText(_translate("userSelectionDialogWidget", "Guest", None))
        self.pb_newUser.setText(_translate("userSelectionDialogWidget", "New", None))
        self.pb_back.setText(_translate("userSelectionDialogWidget", "Back", None))

