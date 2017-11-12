# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Blank.ui'
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

class Ui_EasterEgg(object):
    def setupUi(self, EasterEgg):
        EasterEgg.setObjectName(_fromUtf8("EasterEgg"))
        EasterEgg.resize(400, 300)
        EasterEgg.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(EasterEgg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_gif = QtGui.QLabel(EasterEgg)
        self.label_gif.setText(_fromUtf8(""))
        self.label_gif.setObjectName(_fromUtf8("label_gif"))
        self.verticalLayout.addWidget(self.label_gif)

        self.retranslateUi(EasterEgg)
        QtCore.QMetaObject.connectSlotsByName(EasterEgg)

    def retranslateUi(self, EasterEgg):
        EasterEgg.setWindowTitle(_translate("EasterEgg", "¡¿Como?!", None))

