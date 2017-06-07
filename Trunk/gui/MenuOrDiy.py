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
        self.horizontalLayout = QtGui.QHBoxLayout(MenuOrDiy)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
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
        self.horizontalLayout.addWidget(self.pb_menu)
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
        self.horizontalLayout.addWidget(self.pb_diy)

        self.retranslateUi(MenuOrDiy)
        QtCore.QMetaObject.connectSlotsByName(MenuOrDiy)

    def retranslateUi(self, MenuOrDiy):
        MenuOrDiy.setWindowTitle(_translate("MenuOrDiy", "Form", None))
        self.pb_menu.setText(_translate("MenuOrDiy", "Menu", None))
        self.pb_diy.setText(_translate("MenuOrDiy", "diy", None))

