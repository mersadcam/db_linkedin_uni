# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'skills.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources.resources_rc

class Ui_Skills(object):
    def setupUi(self, Skills):
        if not Skills.objectName():
            Skills.setObjectName(u"Skills")
        Skills.resize(1114, 850)
        Skills.setMinimumSize(QSize(1111, 850))
        Skills.setMaximumSize(QSize(1602, 850))
        Skills.setStyleSheet(u"background:rgba(248, 253, 255, 206);\n"
"color:rgb(1, 31, 54);\\n")
        self.centralwidget = QWidget(Skills)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.backup_pushButton = QPushButton(self.centralwidget)
        self.backup_pushButton.setObjectName(u"backup_pushButton")
        self.backup_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.backup_pushButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/images/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backup_pushButton.setIcon(icon)
        self.backup_pushButton.setIconSize(QSize(28, 28))
        self.backup_pushButton.setFlat(True)

        self.horizontalLayout_4.addWidget(self.backup_pushButton)

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

        self.edit_pushButton = QPushButton(self.centralwidget)
        self.edit_pushButton.setObjectName(u"edit_pushButton")
        self.edit_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_pushButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border:1px solid grey;\n"
"	border-radius:5px;\n"
"	background:rgba(214, 239, 255, 231);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/edit_icon2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_pushButton.setIcon(icon1)
        self.edit_pushButton.setIconSize(QSize(35, 35))
        self.edit_pushButton.setFlat(True)

        self.horizontalLayout.addWidget(self.edit_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1094, 693))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        Skills.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Skills)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1114, 22))
        Skills.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Skills)
        self.statusbar.setObjectName(u"statusbar")
        Skills.setStatusBar(self.statusbar)

        self.retranslateUi(Skills)

        QMetaObject.connectSlotsByName(Skills)
    # setupUi

    def retranslateUi(self, Skills):
        Skills.setWindowTitle(QCoreApplication.translate("Skills", u"MainWindow", None))
        self.backup_pushButton.setText("")
        self.label_4.setText(QCoreApplication.translate("Skills", u"Skills and endorsment", None))
        self.edit_pushButton.setText("")
    # retranslateUi

