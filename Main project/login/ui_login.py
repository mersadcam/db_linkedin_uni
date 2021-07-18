# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(557, 571)
        login.setStyleSheet(u"background:rgba(248, 253, 255, 206);\n"
"color:rgb(1, 31, 54);\\n")
        self.label_login = QLabel(login)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setGeometry(QRect(90, 40, 401, 91))
        self.label_login.setStyleSheet(u"color:rgb(52,52,52);font-size:28pt")
        self.label_email = QLabel(login)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setGeometry(QRect(20, 190, 71, 20))
        self.label_email.setStyleSheet(u"font-size:15pt ;color:rgb(52, 52, 52)")
        self.email = QLineEdit(login)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(170, 180, 331, 41))
        self.email.setStyleSheet(u"font-size:14pt;color:rgb(52,52 , 52)")
        self.label_password = QLabel(login)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(20, 270, 121, 31))
        self.label_password.setStyleSheet(u"font-size:15pt ;color:rgb(52, 52, 52\n"
")")
        self.password = QLineEdit(login)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(170, 260, 331, 41))
        self.password.setStyleSheet(u"font-size:14pt;color:rgb(52,52 , 52)")
        self.loginbutton = QPushButton(login)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(170, 320, 331, 41))
        self.loginbutton.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background:rgb(186, 189, 182);\n"
"border:1px solid white;\n"
"border-radius:5px;\n"
"padding:5px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border:1px solid rgb(32, 74, 135);\n"
"	border-radius:5px;\n"
"	background:rgb(186, 189, 182);\n"
"}\n"
"")
        self.signup_button = QPushButton(login)
        self.signup_button.setObjectName(u"signup_button")
        self.signup_button.setGeometry(QRect(390, 470, 101, 41))
        self.signup_button.setStyleSheet(u"QPushButton{\n"
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
        self.label_dont_have_acc = QLabel(login)
        self.label_dont_have_acc.setObjectName(u"label_dont_have_acc")
        self.label_dont_have_acc.setGeometry(QRect(240, 480, 141, 16))
        self.label_dont_have_acc.setStyleSheet(u"color: rgb(52, 52, 52);")

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Dialog", None))
        self.label_login.setText(QCoreApplication.translate("login", u"Login to Linkedin", None))
        self.label_email.setText(QCoreApplication.translate("login", u"Email", None))
        self.label_password.setText(QCoreApplication.translate("login", u"password", None))
        self.loginbutton.setText(QCoreApplication.translate("login", u"login", None))
        self.signup_button.setText(QCoreApplication.translate("login", u"Sign up", None))
        self.label_dont_have_acc.setText(QCoreApplication.translate("login", u"Don't have an account?", None))
    # retranslateUi

