# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewUserDialog.ui'
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

class Ui_NewUserDialog(object):
    def setupUi(self, NewUserDialog):
        NewUserDialog.setObjectName(_fromUtf8("NewUserDialog"))
        NewUserDialog.resize(775, 355)
        NewUserDialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(NewUserDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(NewUserDialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(22)
        font.setKerning(False)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.list_profilePicture = QtGui.QListWidget(self.groupBox_2)
        self.list_profilePicture.setObjectName(_fromUtf8("list_profilePicture"))
        self.horizontalLayout_2.addWidget(self.list_profilePicture)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.txt_newUserName = QtGui.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txt_newUserName.setFont(font)
        self.txt_newUserName.setObjectName(_fromUtf8("txt_newUserName"))
        self.horizontalLayout_4.addWidget(self.txt_newUserName)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.txt_newUserPassword = QtGui.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txt_newUserPassword.setFont(font)
        self.txt_newUserPassword.setObjectName(_fromUtf8("txt_newUserPassword"))
        self.horizontalLayout_5.addWidget(self.txt_newUserPassword)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.txt_newUserRepeatPassword = QtGui.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txt_newUserRepeatPassword.setFont(font)
        self.txt_newUserRepeatPassword.setObjectName(_fromUtf8("txt_newUserRepeatPassword"))
        self.horizontalLayout_6.addWidget(self.txt_newUserRepeatPassword)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pb_cancel = QtGui.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pb_cancel.setFont(font)
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.horizontalLayout_3.addWidget(self.pb_cancel)
        self.pb_create = QtGui.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pb_create.setFont(font)
        self.pb_create.setDefault(True)
        self.pb_create.setObjectName(_fromUtf8("pb_create"))
        self.horizontalLayout_3.addWidget(self.pb_create)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(NewUserDialog)
        QtCore.QMetaObject.connectSlotsByName(NewUserDialog)

    def retranslateUi(self, NewUserDialog):
        NewUserDialog.setWindowTitle(_translate("NewUserDialog", "Registration", None))
        self.groupBox.setTitle(_translate("NewUserDialog", "New User", None))
        self.groupBox_2.setTitle(_translate("NewUserDialog", "Profile picture", None))
        self.groupBox_3.setTitle(_translate("NewUserDialog", "User", None))
        self.label.setText(_translate("NewUserDialog", "Name", None))
        self.label_2.setText(_translate("NewUserDialog", "Password", None))
        self.label_3.setText(_translate("NewUserDialog", "Repeat\n"
"Password", None))
        self.pb_cancel.setText(_translate("NewUserDialog", "Cancel", None))
        self.pb_create.setText(_translate("NewUserDialog", "Create", None))

