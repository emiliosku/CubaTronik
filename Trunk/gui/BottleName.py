# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BottleName.ui'
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

class Ui_BottleName(object):
    def setupUi(self, BottleName):
        BottleName.setObjectName(_fromUtf8("BottleName"))
        BottleName.resize(400, 181)
        BottleName.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(BottleName)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_bottle = QtGui.QLabel(BottleName)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_bottle.setFont(font)
        self.label_bottle.setObjectName(_fromUtf8("label_bottle"))
        self.horizontalLayout.addWidget(self.label_bottle)
        self.txt_bottleName = QtGui.QLineEdit(BottleName)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txt_bottleName.setFont(font)
        self.txt_bottleName.setObjectName(_fromUtf8("txt_bottleName"))
        self.horizontalLayout.addWidget(self.txt_bottleName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pb_cancel = QtGui.QPushButton(BottleName)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_cancel.sizePolicy().hasHeightForWidth())
        self.pb_cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pb_cancel.setFont(font)
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.horizontalLayout_2.addWidget(self.pb_cancel)
        self.pb_continue = QtGui.QPushButton(BottleName)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_continue.sizePolicy().hasHeightForWidth())
        self.pb_continue.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pb_continue.setFont(font)
        self.pb_continue.setDefault(True)
        self.pb_continue.setObjectName(_fromUtf8("pb_continue"))
        self.horizontalLayout_2.addWidget(self.pb_continue)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(BottleName)
        QtCore.QMetaObject.connectSlotsByName(BottleName)

    def retranslateUi(self, BottleName):
        BottleName.setWindowTitle(_translate("BottleName", "Dialog", None))
        self.label_bottle.setText(_translate("BottleName", "Bottle to\n"
"position", None))
        self.pb_cancel.setText(_translate("BottleName", "Cancel", None))
        self.pb_continue.setText(_translate("BottleName", "Continue", None))

