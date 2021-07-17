# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_signup(object):
    def setupUi(self, signup):
        if not signup.objectName():
            signup.setObjectName(u"signup")
        signup.resize(545, 595)
        signup.setStyleSheet(u"background:rgba(248, 253, 255, 206);\n"
"color:rgb(1, 31, 54);\n"
"")
        self.label_signup = QLabel(signup)
        self.label_signup.setObjectName(u"label_signup")
        self.label_signup.setGeometry(QRect(80, 50, 401, 91))
        self.label_signup.setStyleSheet(u"color:rgb(52,52,52);font-size:28pt")
        self.label_firstname = QLabel(signup)
        self.label_firstname.setObjectName(u"label_firstname")
        self.label_firstname.setGeometry(QRect(20, 190, 131, 20))
        self.label_firstname.setStyleSheet(u"font-size:15pt ;color:rgb(52, 52, 52)")
        self.Firstname = QLineEdit(signup)
        self.Firstname.setObjectName(u"Firstname")
        self.Firstname.setGeometry(QRect(170, 180, 331, 41))
        self.Firstname.setStyleSheet(u"font-size:14pt;color:rgb(52, 52, 52)")
        self.label_lastname = QLabel(signup)
        self.label_lastname.setObjectName(u"label_lastname")
        self.label_lastname.setGeometry(QRect(20, 260, 131, 31))
        self.label_lastname.setStyleSheet(u"font-size:15pt ;color:rgb(52, 52, 52)")
        self.Lastname = QLineEdit(signup)
        self.Lastname.setObjectName(u"Lastname")
        self.Lastname.setGeometry(QRect(170, 250, 331, 41))
        self.Lastname.setStyleSheet(u"font-size:14pt;color:rgb(52, 52, 52)")
        self.signupbutton = QPushButton(signup)
        self.signupbutton.setObjectName(u"signupbutton")
        self.signupbutton.setGeometry(QRect(170, 460, 331, 41))
        self.signupbutton.setStyleSheet(u"QPushButton{\n"
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
        self.Email = QLineEdit(signup)
        self.Email.setObjectName(u"Email")
        self.Email.setGeometry(QRect(170, 320, 331, 41))
        self.Email.setStyleSheet(u"font-size:14pt;color:rgb(52, 52, 52)")
        self.label_email = QLabel(signup)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setGeometry(QRect(20, 330, 121, 31))
        self.label_email.setStyleSheet(u"font-size:15pt ;color:rgb(52, 52, 52)")
        self.password = QLineEdit(signup)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(170, 390, 331, 41))
        self.password.setStyleSheet(u"font-size:14pt;color:rgb(52, 52, 52)")
        self.label_password = QLabel(signup)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(20, 400, 121, 31))
        self.label_password.setStyleSheet(u"font-size:15pt ;color:rgb(52, 52, 52)")

        self.retranslateUi(signup)

        QMetaObject.connectSlotsByName(signup)
    # setupUi

    def retranslateUi(self, signup):
        signup.setWindowTitle(QCoreApplication.translate("signup", u"Dialog", None))
        self.label_signup.setText(QCoreApplication.translate("signup", u"Sign up to Linkedin", None))
        self.label_firstname.setText(QCoreApplication.translate("signup", u"First name", None))
        self.label_lastname.setText(QCoreApplication.translate("signup", u"Last name", None))
        self.signupbutton.setText(QCoreApplication.translate("signup", u"sign up", None))
        self.label_email.setText(QCoreApplication.translate("signup", u"Email", None))
        self.label_password.setText(QCoreApplication.translate("signup", u"Password", None))
    # retranslateUi

