# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc

class Ui_Mainwindow(object):
    def setupUi(self, Mainwindow):
        if not Mainwindow.objectName():
            Mainwindow.setObjectName(u"Mainwindow")
        Mainwindow.resize(1111, 850)
        Mainwindow.setMinimumSize(QSize(1111, 850))
        Mainwindow.setMaximumSize(QSize(1111, 850))
        Mainwindow.setStyleSheet(u"background:rgba(248, 253, 255, 206);\n"
"color:rgb(1, 31, 54);\\n")
        self.centralwidget = QWidget(Mainwindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.profile_widget = QWidget(self.centralwidget)
        self.profile_widget.setObjectName(u"profile_widget")
        self.profile_widget.setMinimumSize(QSize(0, 110))
        self.profile_widget.setMaximumSize(QSize(16777215, 117))
        self.profile_widget.setStyleSheet(u"QWidget#profile_widget{border:1px solid rgb(48, 162, 249)}")
        self.horizontalLayout_4 = QHBoxLayout(self.profile_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.profile_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(101, 101))
        self.label.setMaximumSize(QSize(101, 101))
        self.label.setCursor(QCursor(Qt.PointingHandCursor))
        self.label.setPixmap(QPixmap(u":/images/User-Profile-PNG-Image.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.profile_widget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_4 = QLabel(self.profile_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.plainTextEdit = QPlainTextEdit(self.profile_widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setStyleSheet(u"border:none;")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setMaximumBlockCount(0)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setCenterOnScroll(False)

        self.verticalLayout_4.addWidget(self.plainTextEdit)

        self.verticalLayout_4.setStretch(0, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addWidget(self.profile_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.search_lineEdit = QLineEdit(self.centralwidget)
        self.search_lineEdit.setObjectName(u"search_lineEdit")
        self.search_lineEdit.setMinimumSize(QSize(0, 30))
        self.search_lineEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.search_lineEdit.setStyleSheet(u"margin-right:5px;\n"
"margin-left:10px;\n"
"")

        self.horizontalLayout.addWidget(self.search_lineEdit)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border:1px solid rgb(48, 162, 249);\n"
"	border-radius:5px;\n"
"	background:rgba(68, 170, 248, 56);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(40, 30))
        self.pushButton_2.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(16)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 100))
        self.widget.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 45))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border:1px solid white;\n"
"border-radius:5px;\n"
"padding:5px;\n"
"background:rgb(68, 170, 248)\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border:1px solid rgb(32, 74, 135);\n"
"	border-radius:5px;\n"
"	background:rgb(48, 162, 249);\n"
"}")
        self.pushButton.setIconSize(QSize(25, 25))
        self.pushButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 3)
        self.verticalLayout_2.setStretch(3, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.post_scrollArea = QScrollArea(self.centralwidget)
        self.post_scrollArea.setObjectName(u"post_scrollArea")
        self.post_scrollArea.setStyleSheet(u"QScrollArea#post_scrollArea{border:1px solid rgb(48, 162, 249)}")
        self.post_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 700, 786))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 300))

        self.verticalLayout_3.addWidget(self.widget_2)

        self.verticalSpacer_2 = QSpacerItem(20, 459, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.post_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.post_scrollArea)

        self.horizontalLayout_2.setStretch(1, 7)
        Mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Mainwindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1111, 22))
        Mainwindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Mainwindow)
        self.statusbar.setObjectName(u"statusbar")
        Mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(Mainwindow)

        QMetaObject.connectSlotsByName(Mainwindow)
    # setupUi

    def retranslateUi(self, Mainwindow):
        Mainwindow.setWindowTitle(QCoreApplication.translate("Mainwindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Mainwindow", u"Firstname", None))
        self.label_4.setText(QCoreApplication.translate("Mainwindow", u"Lastname", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Mainwindow", u"Headline...\n"
"", None))
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("Mainwindow", u"Search ...", None))
        self.pushButton_2.setText("")
        self.label_5.setText(QCoreApplication.translate("Mainwindow", u"Suggestion", None))
        self.pushButton.setText(QCoreApplication.translate("Mainwindow", u"New post", None))
    # retranslateUi

