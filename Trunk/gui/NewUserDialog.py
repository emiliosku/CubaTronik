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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(717, 232)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(18)
        font.setKerning(False)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_profilePicture = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_profilePicture.setFont(font)
        self.label_profilePicture.setObjectName(_fromUtf8("label_profilePicture"))
        self.verticalLayout_3.addWidget(self.label_profilePicture)
        self.list_profilePicture = QtGui.QListView(self.groupBox)
        self.list_profilePicture.setObjectName(_fromUtf8("list_profilePicture"))
        self.verticalLayout_3.addWidget(self.list_profilePicture)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_userName = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_userName.sizePolicy().hasHeightForWidth())
        self.label_userName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_userName.setFont(font)
        self.label_userName.setObjectName(_fromUtf8("label_userName"))
        self.verticalLayout_2.addWidget(self.label_userName)
        self.txt_newUserName = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_newUserName.sizePolicy().hasHeightForWidth())
        self.txt_newUserName.setSizePolicy(sizePolicy)
        self.txt_newUserName.setObjectName(_fromUtf8("txt_newUserName"))
        self.verticalLayout_2.addWidget(self.txt_newUserName)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pb_cancel = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_cancel.sizePolicy().hasHeightForWidth())
        self.pb_cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Single Sleeve"))
        font.setPointSize(14)
        font.setKerning(False)
        self.pb_cancel.setFont(font)
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.horizontalLayout_2.addWidget(self.pb_cancel)
        self.pb_create = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_create.sizePolicy().hasHeightForWidth())
        self.pb_create.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pb_create.setFont(font)
        self.pb_create.setObjectName(_fromUtf8("pb_create"))
        self.horizontalLayout_2.addWidget(self.pb_create)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "New User", None))
        self.label_profilePicture.setText(_translate("Dialog", "Profile picture", None))
        self.label_userName.setText(_translate("Dialog", "User name", None))
        self.pb_cancel.setText(_translate("Dialog", "Cancel", None))
        self.pb_create.setText(_translate("Dialog", "Create", None))

