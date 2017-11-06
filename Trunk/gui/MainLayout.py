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

class Ui_MainLayout(object):
    def setupUi(self, MainLayout):
        MainLayout.setObjectName(_fromUtf8("MainLayout"))
        MainLayout.resize(400, 300)
        self.horizontalLayout = QtGui.QHBoxLayout(MainLayout)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pb_newDrink = QtGui.QPushButton(MainLayout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_newDrink.sizePolicy().hasHeightForWidth())
        self.pb_newDrink.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(48)
        self.pb_newDrink.setFont(font)
        self.pb_newDrink.setObjectName(_fromUtf8("pb_newDrink"))
        self.horizontalLayout.addWidget(self.pb_newDrink)

        self.retranslateUi(MainLayout)
        QtCore.QMetaObject.connectSlotsByName(MainLayout)

    def retranslateUi(self, MainLayout):
        MainLayout.setWindowTitle(_translate("MainLayout", "Form", None))
        self.pb_newDrink.setText(_translate("MainLayout", "New Drink", None))

