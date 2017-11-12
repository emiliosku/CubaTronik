# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminPassword.ui'
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

class Ui_AdminPass(object):
    def setupUi(self, AdminPass):
        AdminPass.setObjectName(_fromUtf8("AdminPass"))
        AdminPass.resize(497, 138)
        AdminPass.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(AdminPass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(AdminPass)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.txt_password = QtGui.QLineEdit(AdminPass)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.txt_password.setFont(font)
        self.txt_password.setEchoMode(QtGui.QLineEdit.Password)
        self.txt_password.setObjectName(_fromUtf8("txt_password"))
        self.horizontalLayout.addWidget(self.txt_password)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pb_cancel = QtGui.QPushButton(AdminPass)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pb_cancel.setFont(font)
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.horizontalLayout_2.addWidget(self.pb_cancel)
        self.pb_check = QtGui.QPushButton(AdminPass)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pb_check.setFont(font)
        self.pb_check.setDefault(True)
        self.pb_check.setObjectName(_fromUtf8("pb_check"))
        self.horizontalLayout_2.addWidget(self.pb_check)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(AdminPass)
        QtCore.QMetaObject.connectSlotsByName(AdminPass)

    def retranslateUi(self, AdminPass):
        AdminPass.setWindowTitle(_translate("AdminPass", "Enter Admin Mode", None))
        self.label.setText(_translate("AdminPass", "Password", None))
        self.pb_cancel.setText(_translate("AdminPass", "Cancel", None))
        self.pb_check.setText(_translate("AdminPass", "Check In", None))

