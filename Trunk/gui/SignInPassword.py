# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignInPassword.ui'
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

class Ui_TypePassword(object):
    def setupUi(self, TypePassword):
        TypePassword.setObjectName(_fromUtf8("TypePassword"))
        TypePassword.setWindowModality(QtCore.Qt.NonModal)
        TypePassword.resize(462, 120)
        TypePassword.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(TypePassword)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_pw = QtGui.QLabel(TypePassword)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(18)
        self.label_pw.setFont(font)
        self.label_pw.setObjectName(_fromUtf8("label_pw"))
        self.horizontalLayout_2.addWidget(self.label_pw)
        self.txt_pw = QtGui.QLineEdit(TypePassword)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(16)
        self.txt_pw.setFont(font)
        self.txt_pw.setEchoMode(QtGui.QLineEdit.Password)
        self.txt_pw.setObjectName(_fromUtf8("txt_pw"))
        self.horizontalLayout_2.addWidget(self.txt_pw)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pb_signIn = QtGui.QPushButton(TypePassword)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_signIn.sizePolicy().hasHeightForWidth())
        self.pb_signIn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(14)
        self.pb_signIn.setFont(font)
        self.pb_signIn.setAutoDefault(False)
        self.pb_signIn.setDefault(True)
        self.pb_signIn.setObjectName(_fromUtf8("pb_signIn"))
        self.horizontalLayout_3.addWidget(self.pb_signIn)
        self.pb_cancel = QtGui.QPushButton(TypePassword)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_cancel.sizePolicy().hasHeightForWidth())
        self.pb_cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(14)
        self.pb_cancel.setFont(font)
        self.pb_cancel.setAutoDefault(False)
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.horizontalLayout_3.addWidget(self.pb_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(TypePassword)
        QtCore.QMetaObject.connectSlotsByName(TypePassword)

    def retranslateUi(self, TypePassword):
        TypePassword.setWindowTitle(_translate("TypePassword", "Sign In with your Password", None))
        self.label_pw.setText(_translate("TypePassword", "Password", None))
        self.pb_signIn.setText(_translate("TypePassword", "Sign In", None))
        self.pb_cancel.setText(_translate("TypePassword", "Cancel", None))

