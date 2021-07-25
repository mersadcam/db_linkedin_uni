# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'background.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc
import resources_rc
import resources_rc

class Ui_background(object):
    def setupUi(self, background):
        if not background.objectName():
            background.setObjectName(u"background")
        background.resize(1114, 850)
        background.setMinimumSize(QSize(1111, 850))
        background.setMaximumSize(QSize(1602, 850))
        background.setStyleSheet(u"background:rgba(248, 253, 255, 206);\n"
"color:rgb(1, 31, 54);\\n")
        self.centralwidget = QWidget(background)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.back_pushButton = QPushButton(self.centralwidget)
        self.back_pushButton.setObjectName(u"back_pushButton")
        self.back_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_pushButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/images/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_pushButton.setIcon(icon)
        self.back_pushButton.setIconSize(QSize(28, 28))
        self.back_pushButton.setFlat(True)

        self.horizontalLayout_4.addWidget(self.back_pushButton)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Nimbus Roman"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(Qt.AutoText)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.add_pushButton = QPushButton(self.centralwidget)
        self.add_pushButton.setObjectName(u"add_pushButton")
        self.add_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_pushButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border:1px solid grey;\n"
"	border-radius:5px;\n"
"	background:rgba(214, 239, 255, 231);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_pushButton.setIcon(icon1)
        self.add_pushButton.setIconSize(QSize(35, 35))
        self.add_pushButton.setFlat(True)

        self.horizontalLayout.addWidget(self.add_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1094, 693))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        background.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(background)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1114, 22))
        background.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(background)
        self.statusbar.setObjectName(u"statusbar")
        background.setStatusBar(self.statusbar)

        self.retranslateUi(background)

        QMetaObject.connectSlotsByName(background)
    # setupUi

    def retranslateUi(self, background):
        background.setWindowTitle(QCoreApplication.translate("background", u"MainWindow", None))
        self.back_pushButton.setText("")
        self.label_4.setText(QCoreApplication.translate("background", u"Background", None))
        self.add_pushButton.setText("")
    # retranslateUi

