# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminMenu.ui'
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

class Ui_AdminMenu(object):
    def setupUi(self, AdminMenu):
        AdminMenu.setObjectName(_fromUtf8("AdminMenu"))
        AdminMenu.resize(890, 652)
        self.verticalLayout = QtGui.QVBoxLayout(AdminMenu)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pb_bottlePositioning = QtGui.QPushButton(AdminMenu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_bottlePositioning.sizePolicy().hasHeightForWidth())
        self.pb_bottlePositioning.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pb_bottlePositioning.setFont(font)
        self.pb_bottlePositioning.setObjectName(_fromUtf8("pb_bottlePositioning"))
        self.horizontalLayout_3.addWidget(self.pb_bottlePositioning)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pb_homing = QtGui.QPushButton(AdminMenu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_homing.sizePolicy().hasHeightForWidth())
        self.pb_homing.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pb_homing.setFont(font)
        self.pb_homing.setObjectName(_fromUtf8("pb_homing"))
        self.horizontalLayout_4.addWidget(self.pb_homing)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pb_flush = QtGui.QPushButton(AdminMenu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_flush.sizePolicy().hasHeightForWidth())
        self.pb_flush.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pb_flush.setFont(font)
        self.pb_flush.setObjectName(_fromUtf8("pb_flush"))
        self.horizontalLayout_5.addWidget(self.pb_flush)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pb_pumpConfig = QtGui.QPushButton(AdminMenu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_pumpConfig.sizePolicy().hasHeightForWidth())
        self.pb_pumpConfig.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pb_pumpConfig.setFont(font)
        self.pb_pumpConfig.setObjectName(_fromUtf8("pb_pumpConfig"))
        self.horizontalLayout_6.addWidget(self.pb_pumpConfig)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pb_exit = QtGui.QPushButton(AdminMenu)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pb_exit.setFont(font)
        self.pb_exit.setDefault(True)
        self.pb_exit.setObjectName(_fromUtf8("pb_exit"))
        self.horizontalLayout.addWidget(self.pb_exit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(AdminMenu)
        QtCore.QMetaObject.connectSlotsByName(AdminMenu)

    def retranslateUi(self, AdminMenu):
        AdminMenu.setWindowTitle(_translate("AdminMenu", "Admin Menu", None))
        self.pb_bottlePositioning.setText(_translate("AdminMenu", "Bottle Positioning", None))
        self.pb_homing.setText(_translate("AdminMenu", "Homing", None))
        self.pb_flush.setText(_translate("AdminMenu", "Flush", None))
        self.pb_pumpConfig.setText(_translate("AdminMenu", "Pump Configuration", None))
        self.pb_exit.setText(_translate("AdminMenu", "Exit Admin Mode", None))

