# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wmain.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Beve(object):
    def setupUi(self, Beve):
        if not Beve.objectName():
            Beve.setObjectName(u"Beve")
        Beve.resize(800, 600)
        self.centralwidget = QWidget(Beve)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainStartButton = QPushButton(self.centralwidget)
        self.mainStartButton.setObjectName(u"mainStartButton")
        self.mainStartButton.setGeometry(QRect(340, 470, 75, 23))
        Beve.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Beve)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        Beve.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Beve)
        self.statusbar.setObjectName(u"statusbar")
        Beve.setStatusBar(self.statusbar)

        self.retranslateUi(Beve)

        QMetaObject.connectSlotsByName(Beve)
    # setupUi

    def retranslateUi(self, Beve):
        Beve.setWindowTitle(QCoreApplication.translate("Beve", u"MainWindow", None))
        self.mainStartButton.setText(QCoreApplication.translate("Beve", u"Start ", None))
    # retranslateUi

