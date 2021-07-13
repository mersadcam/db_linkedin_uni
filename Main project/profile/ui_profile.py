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
        Profile.resize(1114, 800)
        Profile.setMinimumSize(QSize(1111, 0))
        self.centralwidget = QWidget(Profile)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Nimbus Roman"])
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(Qt.AutoText)

        self.verticalLayout_4.addWidget(self.label_4)

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

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        font2 = QFont()
        font2.setBold(True)
        self.pushButton_7.setFont(font2)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"color:blue;\n"
"border: 1px solid blue;\n"
"padding:10px;\n"
"border-radius:5px;\n"
"background:rgb(183, 224, 255)\n"
"\n"
"")
        self.pushButton_7.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_7, 4, 0, 1, 3)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.pushButton_6.setFont(font3)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"color:blue;\n"
"border: 1px solid blue;\n"
"padding:10px;\n"
"border-radius:5px;\n"
"background:rgb(183, 224, 255)\n"
"\n"
"")
        self.pushButton_6.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_6, 3, 2, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setFamilies([u"Sans"])
        font4.setPointSize(9)
        self.label_2.setFont(font4)

        self.gridLayout.addWidget(self.label_2, 1, 0, 2, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.first_name = QLabel(self.centralwidget)
        self.first_name.setObjectName(u"first_name")
        font5 = QFont()
        font5.setFamilies([u"Sans"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.first_name.setFont(font5)

        self.gridLayout.addWidget(self.first_name, 0, 0, 1, 1)

        self.last_name = QLabel(self.centralwidget)
        self.last_name.setObjectName(u"last_name")
        self.last_name.setFont(font5)

        self.gridLayout.addWidget(self.last_name, 0, 2, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        font6 = QFont()
        font6.setPointSize(15)
        font6.setBold(True)
        self.label_6.setFont(font6)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        font7 = QFont()
        font7.setPointSize(17)
        self.label_7.setFont(font7)

        self.verticalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.label_8)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 55))
        font8 = QFont()
        font8.setPointSize(14)
        self.pushButton.setFont(font8)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"Text-align:left;\n"
"border: 1px solid grey;\n"
"border-radius:10px\n"
"")
        self.pushButton.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 55))
        self.pushButton_2.setFont(font8)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"Text-align:left;\n"
"border: 1px solid grey;\n"
"border-radius:10px\n"
"")
        self.pushButton_2.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 55))
        self.pushButton_3.setFont(font8)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"Text-align:left;\n"
"border: 1px solid grey;\n"
"border-radius:10px\n"
"")
        self.pushButton_3.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 55))
        self.pushButton_4.setFont(font8)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"Text-align:left;\n"
"border: 1px solid grey;\n"
"border-radius:10px\n"
"")
        self.pushButton_4.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 197, 470))
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
        self.label_4.setText(QCoreApplication.translate("Profile", u"Profile", None))
        self.label_3.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("Profile", u"Connections", None))
        self.label_5.setText(QCoreApplication.translate("Profile", u"Country", None))
        self.pushButton_6.setText(QCoreApplication.translate("Profile", u"Contact info", None))
        self.label_2.setText(QCoreApplication.translate("Profile", u"Status", None))
        self.first_name.setText(QCoreApplication.translate("Profile", u"Mersad", None))
        self.last_name.setText(QCoreApplication.translate("Profile", u"Khalafi", None))
        self.label_6.setText(QCoreApplication.translate("Profile", u"-", None))
        self.label_7.setText(QCoreApplication.translate("Profile", u"About", None))
        self.label_8.setText(QCoreApplication.translate("Profile", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Profile", u"   Skills and endorsments", None))
        self.pushButton_2.setText(QCoreApplication.translate("Profile", u"   Background", None))
        self.pushButton_3.setText(QCoreApplication.translate("Profile", u"   \u202b\u202aAccomplishments\u202c\u202c", None))
        self.pushButton_4.setText(QCoreApplication.translate("Profile", u"   Skills and endorsments", None))
        self.label.setText(QCoreApplication.translate("Profile", u"Select language", None))
    # retranslateUi

