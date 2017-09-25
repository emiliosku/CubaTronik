# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
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

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName(_fromUtf8("Menu"))
        Menu.resize(781, 536)
        self.horizontalLayout = QtGui.QHBoxLayout(Menu)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(Menu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(24)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.list_mixedDrinks = QtGui.QListWidget(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_mixedDrinks.sizePolicy().hasHeightForWidth())
        self.list_mixedDrinks.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(22)
        self.list_mixedDrinks.setFont(font)
        self.list_mixedDrinks.setObjectName(_fromUtf8("list_mixedDrinks"))
        self.verticalLayout.addWidget(self.list_mixedDrinks)
        self.horizontalLayout.addWidget(self.groupBox)
        self.line = QtGui.QFrame(Menu)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.txt_description = QtGui.QLabel(Menu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_description.sizePolicy().hasHeightForWidth())
        self.txt_description.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(16)
        self.txt_description.setFont(font)
        self.txt_description.setText(_fromUtf8(""))
        self.txt_description.setWordWrap(True)
        self.txt_description.setObjectName(_fromUtf8("txt_description"))
        self.verticalLayout_2.addWidget(self.txt_description)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pb_back = QtGui.QPushButton(Menu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_back.sizePolicy().hasHeightForWidth())
        self.pb_back.setSizePolicy(sizePolicy)
        self.pb_back.setText(_fromUtf8(""))
        self.pb_back.setObjectName(_fromUtf8("pb_back"))
        self.horizontalLayout_2.addWidget(self.pb_back)
        self.pb_create = QtGui.QPushButton(Menu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_create.sizePolicy().hasHeightForWidth())
        self.pb_create.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(24)
        self.pb_create.setFont(font)
        self.pb_create.setAutoDefault(True)
        self.pb_create.setObjectName(_fromUtf8("pb_create"))
        self.horizontalLayout_2.addWidget(self.pb_create)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(_translate("Menu", "Form", None))
        self.groupBox.setTitle(_translate("Menu", "Menu", None))
        self.pb_create.setText(_translate("Menu", "Create", None))

