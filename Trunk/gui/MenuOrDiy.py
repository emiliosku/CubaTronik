# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuOrDiy.ui'
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

class Ui_MenuOrDiy(object):
    def setupUi(self, MenuOrDiy):
        MenuOrDiy.setObjectName(_fromUtf8("MenuOrDiy"))
        MenuOrDiy.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(MenuOrDiy)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_welcome = QtGui.QLabel(MenuOrDiy)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_welcome.sizePolicy().hasHeightForWidth())
        self.label_welcome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(20)
        self.label_welcome.setFont(font)
        self.label_welcome.setObjectName(_fromUtf8("label_welcome"))
        self.horizontalLayout.addWidget(self.label_welcome)
        self.label_userName = QtGui.QLabel(MenuOrDiy)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_userName.sizePolicy().hasHeightForWidth())
        self.label_userName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(28)
        self.label_userName.setFont(font)
        self.label_userName.setText(_fromUtf8(""))
        self.label_userName.setObjectName(_fromUtf8("label_userName"))
        self.horizontalLayout.addWidget(self.label_userName)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pb_menu = QtGui.QPushButton(MenuOrDiy)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_menu.sizePolicy().hasHeightForWidth())
        self.pb_menu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(36)
        self.pb_menu.setFont(font)
        self.pb_menu.setObjectName(_fromUtf8("pb_menu"))
        self.horizontalLayout_2.addWidget(self.pb_menu)
        self.pb_diy = QtGui.QPushButton(MenuOrDiy)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_diy.sizePolicy().hasHeightForWidth())
        self.pb_diy.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(36)
        self.pb_diy.setFont(font)
        self.pb_diy.setObjectName(_fromUtf8("pb_diy"))
        self.horizontalLayout_2.addWidget(self.pb_diy)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pb_back = QtGui.QPushButton(MenuOrDiy)
        self.pb_back.setText(_fromUtf8(""))
        self.pb_back.setObjectName(_fromUtf8("pb_back"))
        self.horizontalLayout_3.addWidget(self.pb_back)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(MenuOrDiy)
        QtCore.QMetaObject.connectSlotsByName(MenuOrDiy)

    def retranslateUi(self, MenuOrDiy):
        MenuOrDiy.setWindowTitle(_translate("MenuOrDiy", "Form", None))
        self.label_welcome.setText(_translate("MenuOrDiy", "Welcome ", None))
        self.pb_menu.setText(_translate("MenuOrDiy", "Menu", None))
        self.pb_diy.setText(_translate("MenuOrDiy", "Diy", None))

