# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Save(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 48)
        Dialog.setStyleSheet("background-color: rgb(216, 225, 229);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(41, 96, 115);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.save_line = QtWidgets.QLineEdit(Dialog)
        self.save_line.setMinimumSize(QtCore.QSize(240, 30))
        self.save_line.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.save_line.setFont(font)
        self.save_line.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(41, 96, 115);")
        self.save_line.setObjectName("save_line")
        self.horizontalLayout.addWidget(self.save_line)
        self.save_button = QtWidgets.QPushButton(Dialog)
        self.save_button.setMinimumSize(QtCore.QSize(50, 30))
        self.save_button.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("color: rgb(41, 96, 115);\n"
"background-color: rgb(173, 197, 207);")
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Save"))
        self.label.setText(_translate("Dialog", "Save name"))
        self.save_line.setText(_translate("Dialog", "undifined.fasta"))
        self.save_button.setText(_translate("Dialog", "Save"))
