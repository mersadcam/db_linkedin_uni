# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(585, 600)
        login.setMinimumSize(QSize(585, 600))
        login.setMaximumSize(QSize(585, 600))
        login.setStyleSheet(u"background:rgb(247, 252, 255);\n"
"color:rgb(1, 31, 54);\\n")
        self.centralwidget = QWidget(login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(25, 15, 25, 15)
        self.label_login = QLabel(self.centralwidget)
        self.label_login.setObjectName(u"label_login")
        font = QFont()
        font.setFamilies([u"Fira Sans"])
        font.setPointSize(28)
        font.setItalic(True)
        self.label_login.setFont(font)
        self.label_login.setStyleSheet(u"font-size:28pt;\n"
"background:rgba(248, 253, 255, 206);\n"
"color:rgb(1, 31, 54);")
        self.label_login.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_login)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.label_email = QLabel(self.centralwidget)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setStyleSheet(u"font-size:15pt ;color:rgb(52, 52, 52)")

        self.gridLayout.addWidget(self.label_email, 0, 0, 1, 1)

        self.label_password = QLabel(self.centralwidget)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setStyleSheet(u"font-size:15pt ;color:rgb(52, 52, 52\n"
")")

        self.gridLayout.addWidget(self.label_password, 1, 0, 1, 2)

        self.password_lineEdit = QLineEdit(self.centralwidget)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setMinimumSize(QSize(0, 38))
        self.password_lineEdit.setStyleSheet(u"font-size:14pt;color:rgb(52,52 , 52)")
        self.password_lineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.password_lineEdit, 1, 2, 1, 1)

        self.email_lineEdit = QLineEdit(self.centralwidget)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setMinimumSize(QSize(0, 38))
        self.email_lineEdit.setStyleSheet(u"font-size:14pt;color:rgb(52,52 , 52)")

        self.gridLayout.addWidget(self.email_lineEdit, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.msg_label = QLabel(self.centralwidget)
        self.msg_label.setObjectName(u"msg_label")
        font1 = QFont()
        font1.setPointSize(12)
        self.msg_label.setFont(font1)
        self.msg_label.setStyleSheet(u"color:red")

        self.verticalLayout.addWidget(self.msg_label)

        self.verticalSpacer_2 = QSpacerItem(17, 53, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.login_pushButton = QPushButton(self.centralwidget)
        self.login_pushButton.setObjectName(u"login_pushButton")
        self.login_pushButton.setMinimumSize(QSize(0, 50))
        self.login_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_pushButton.setStyleSheet(u"QPushButton{\n"
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
        self.login_pushButton.setFlat(True)

        self.verticalLayout.addWidget(self.login_pushButton)

        self.verticalSpacer = QSpacerItem(17, 52, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_dont_have_acc = QLabel(self.centralwidget)
        self.label_dont_have_acc.setObjectName(u"label_dont_have_acc")
        self.label_dont_have_acc.setStyleSheet(u"color: rgb(52, 52, 52);")

        self.horizontalLayout_3.addWidget(self.label_dont_have_acc)

        self.signup_pushButton = QPushButton(self.centralwidget)
        self.signup_pushButton.setObjectName(u"signup_pushButton")
        self.signup_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.signup_pushButton.setStyleSheet(u"QPushButton{\n"
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
        self.signup_pushButton.setFlat(True)

        self.horizontalLayout_3.addWidget(self.signup_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        login.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(login)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 585, 22))
        login.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(login)
        self.statusbar.setObjectName(u"statusbar")
        login.setStatusBar(self.statusbar)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"MainWindow", None))
        self.label_login.setText(QCoreApplication.translate("login", u"Login to Linkedin", None))
        self.label_email.setText(QCoreApplication.translate("login", u"Email", None))
        self.label_password.setText(QCoreApplication.translate("login", u"password", None))
        self.msg_label.setText(QCoreApplication.translate("login", u"Invalid email or password.", None))
        self.login_pushButton.setText(QCoreApplication.translate("login", u"login", None))
        self.label_dont_have_acc.setText(QCoreApplication.translate("login", u"Don't have an account?", None))
        self.signup_pushButton.setText(QCoreApplication.translate("login", u"Sign up", None))
    # retranslateUi

