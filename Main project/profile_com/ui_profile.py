# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources

class Ui_Profile(object):
    def setupUi(self, Profile):
        if not Profile.objectName():
            Profile.setObjectName(u"Profile")
        Profile.resize(1114, 850)
        Profile.setMinimumSize(QSize(1111, 850))
        Profile.setMaximumSize(QSize(1602, 850))
        Profile.setStyleSheet(u"background:rgba(248, 253, 255, 206);\n"
"color:rgb(1, 31, 54);\\n")
        self.centralwidget = QWidget(Profile)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
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


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 190))
        self.label_3.setMaximumSize(QSize(100000, 190))
        font1 = QFont()
        font1.setPointSize(40)
        self.label_3.setFont(font1)
        self.label_3.setPixmap(QPixmap(u":/images/mountain-lake-header.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)

        self.verticalLayout_4.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lastName_label = QLabel(self.centralwidget)
        self.lastName_label.setObjectName(u"lastName_label")
        font2 = QFont()
        font2.setFamilies([u"Nimbus Roman"])
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(True)
        self.lastName_label.setFont(font2)
        self.lastName_label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lastName_label, 0, 2, 1, 1)

        self.firstName_label = QLabel(self.centralwidget)
        self.firstName_label.setObjectName(u"firstName_label")
        self.firstName_label.setFont(font2)
        self.firstName_label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.firstName_label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.contactInfo_pushButton = QPushButton(self.centralwidget)
        self.contactInfo_pushButton.setObjectName(u"contactInfo_pushButton")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.contactInfo_pushButton.setFont(font3)
        self.contactInfo_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.contactInfo_pushButton.setStyleSheet(u"color:rgb(3, 62, 106);\n"
"border: 1px solid rgb(162, 215, 255);\n"
"padding:10px;\n"
"border-radius:5px;\n"
"background:rgba(221, 242, 255, 231)\n"
"\n"
"")
        self.contactInfo_pushButton.setFlat(True)

        self.gridLayout.addWidget(self.contactInfo_pushButton, 3, 2, 1, 1)

        self.headline_label = QLabel(self.centralwidget)
        self.headline_label.setObjectName(u"headline_label")
        font4 = QFont()
        font4.setFamilies([u"Sans"])
        font4.setPointSize(9)
        self.headline_label.setFont(font4)
        self.headline_label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.headline_label, 1, 0, 2, 3)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        self.label_6.setFont(font5)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)

        self.connections_pushButton = QPushButton(self.centralwidget)
        self.connections_pushButton.setObjectName(u"connections_pushButton")
        font6 = QFont()
        font6.setBold(True)
        self.connections_pushButton.setFont(font6)
        self.connections_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.connections_pushButton.setStyleSheet(u"color:rgb(3, 62, 106);\n"
"border: 1px solid rgb(162, 215, 255);\n"
"padding:10px;\n"
"border-radius:5px;\n"
"background:rgba(221, 242, 255, 231)\n"
"\n"
"")
        self.connections_pushButton.setFlat(True)

        self.gridLayout.addWidget(self.connections_pushButton, 4, 0, 1, 3)

        self.country_label = QLabel(self.centralwidget)
        self.country_label.setObjectName(u"country_label")
        self.country_label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.country_label, 3, 0, 1, 1)

        self.editInfo_pushButton = QPushButton(self.centralwidget)
        self.editInfo_pushButton.setObjectName(u"editInfo_pushButton")
        self.editInfo_pushButton.setMinimumSize(QSize(35, 35))
        self.editInfo_pushButton.setMaximumSize(QSize(35, 35))
        self.editInfo_pushButton.setCursor(QCursor(Qt.BusyCursor))
        self.editInfo_pushButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border:1px solid grey;\n"
"	border-radius:5px;\n"
"	background:rgba(214, 239, 255, 231);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/edit_icon2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editInfo_pushButton.setIcon(icon1)
        self.editInfo_pushButton.setIconSize(QSize(25, 25))
        self.editInfo_pushButton.setFlat(True)

        self.gridLayout.addWidget(self.editInfo_pushButton, 2, 4, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        font7 = QFont()
        font7.setPointSize(17)
        self.label_7.setFont(font7)
        self.label_7.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.editAbout_pushButton = QPushButton(self.widget)
        self.editAbout_pushButton.setObjectName(u"editAbout_pushButton")
        self.editAbout_pushButton.setMinimumSize(QSize(35, 35))
        self.editAbout_pushButton.setMaximumSize(QSize(35, 35))
        self.editAbout_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.editAbout_pushButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border:1px solid grey;\n"
"	border-radius:5px;\n"
"	background:rgba(214, 239, 255, 231);\n"
"}")
        self.editAbout_pushButton.setIcon(icon1)
        self.editAbout_pushButton.setIconSize(QSize(25, 25))
        self.editAbout_pushButton.setFlat(True)

        self.horizontalLayout_3.addWidget(self.editAbout_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.aboutContent_label = QLabel(self.widget)
        self.aboutContent_label.setObjectName(u"aboutContent_label")
        self.aboutContent_label.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.aboutContent_label)

        self.skills_pushButton = QPushButton(self.widget)
        self.skills_pushButton.setObjectName(u"skills_pushButton")
        self.skills_pushButton.setMinimumSize(QSize(0, 55))
        font8 = QFont()
        font8.setPointSize(14)
        self.skills_pushButton.setFont(font8)
        self.skills_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.skills_pushButton.setStyleSheet(u"Text-align:left;\n"
"border: 1px solid grey;\n"
"border-radius:10px;\n"
"padding-left: 10px\n"
"")
        self.skills_pushButton.setFlat(True)

        self.verticalLayout.addWidget(self.skills_pushButton)

        self.background_pushButton = QPushButton(self.widget)
        self.background_pushButton.setObjectName(u"background_pushButton")
        self.background_pushButton.setMinimumSize(QSize(0, 55))
        self.background_pushButton.setFont(font8)
        self.background_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.background_pushButton.setStyleSheet(u"Text-align:left;\n"
"border: 1px solid grey;\n"
"border-radius:10px;\n"
"padding-left: 10px\n"
"")
        self.background_pushButton.setFlat(True)

        self.verticalLayout.addWidget(self.background_pushButton)

        self.accomp_pushButton = QPushButton(self.widget)
        self.accomp_pushButton.setObjectName(u"accomp_pushButton")
        self.accomp_pushButton.setMinimumSize(QSize(0, 55))
        self.accomp_pushButton.setFont(font8)
        self.accomp_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.accomp_pushButton.setStyleSheet(u"Text-align:left;\n"
"border: 1px solid grey;\n"
"border-radius:10px;\n"
"padding-left: 10px\n"
"")
        self.accomp_pushButton.setFlat(True)

        self.verticalLayout.addWidget(self.accomp_pushButton)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 55))
        self.pushButton_4.setFont(font8)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"Text-align:left;\n"
"border: 1px solid grey;\n"
"border-radius:10px;\n"
"padding-left: 10px\n"
"")
        self.pushButton_4.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_4)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.label)

        self.selectLang_comboBox = QComboBox(self.centralwidget)
        self.selectLang_comboBox.setObjectName(u"selectLang_comboBox")

        self.horizontalLayout.addWidget(self.selectLang_comboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 197, 500))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(0, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        Profile.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Profile)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1114, 22))
        Profile.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Profile)
        self.statusbar.setObjectName(u"statusbar")
        Profile.setStatusBar(self.statusbar)

        self.retranslateUi(Profile)

        QMetaObject.connectSlotsByName(Profile)
    # setupUi

    def retranslateUi(self, Profile):
        Profile.setWindowTitle(QCoreApplication.translate("Profile", u"MainWindow", None))
        self.backup_pushButton.setText("")
        self.label_4.setText(QCoreApplication.translate("Profile", u"Profile", None))
        self.label_3.setText("")
        self.lastName_label.setText(QCoreApplication.translate("Profile", u"Khalafi", None))
        self.firstName_label.setText(QCoreApplication.translate("Profile", u"Mersad", None))
        self.contactInfo_pushButton.setText(QCoreApplication.translate("Profile", u"Contact info", None))
        self.headline_label.setText(QCoreApplication.translate("Profile", u"Headline", None))
        self.label_6.setText(QCoreApplication.translate("Profile", u"-", None))
        self.connections_pushButton.setText(QCoreApplication.translate("Profile", u"Connections", None))
        self.country_label.setText(QCoreApplication.translate("Profile", u"Country", None))
        self.editInfo_pushButton.setText("")
        self.label_7.setText(QCoreApplication.translate("Profile", u"About", None))
        self.editAbout_pushButton.setText("")
        self.aboutContent_label.setText(QCoreApplication.translate("Profile", u"TextLabel", None))
        self.skills_pushButton.setText(QCoreApplication.translate("Profile", u"Skills and endorsments", None))
        self.background_pushButton.setText(QCoreApplication.translate("Profile", u"Background", None))
        self.accomp_pushButton.setText(QCoreApplication.translate("Profile", u"Accomplishments\u202c\u202c", None))
        self.pushButton_4.setText(QCoreApplication.translate("Profile", u"Edit profile", None))
        self.label.setText(QCoreApplication.translate("Profile", u"Select language", None))
    # retranslateUi

