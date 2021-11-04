# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Open(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(264, 189)
        Dialog.setStyleSheet("background-color: rgb(216, 225, 229);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.open_list = QtWidgets.QListView(Dialog)
        self.open_list.setStyleSheet("background-color: rgb(194, 221, 232);\n"
"color: rgb(37, 86, 103);")
        self.open_list.setObjectName("open_list")
        self.verticalLayout.addWidget(self.open_list)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Open data"))
