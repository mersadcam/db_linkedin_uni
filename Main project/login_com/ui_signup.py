# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_signup(object):
    def setupUi(self, signup):
        if not signup.objectName():
            signup.setObjectName(u"signup")
        signup.resize(585, 600)
        signup.setMinimumSize(QSize(585, 600))
        signup.setMaximumSize(QSize(585, 600))
        signup.setStyleSheet(u"background:rgb(247, 252, 255);\n"
"color:rgb(1, 31, 54);\n"
"")
        self.centralwidget = QWidget(signup)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(25, 15, 25, 15)
        self.label_signup = QLabel(self.centralwidget)
        self.label_signup.setObjectName(u"label_signup")
        font = QFont()
        font.setFamilies([u"Fira Sans"])
        font.setPointSize(28)
        font.setItalic(True)
        self.label_signup.setFont(font)
        self.label_signup.setStyleSheet(u"color:rgb(52,52,52);font-size:28pt")
        self.label_signup.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_signup)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.firstname_lineEdit = QLineEdit(self.centralwidget)
        self.firstname_lineEdit.setObjectName(u"firstname_lineEdit")
        self.firstname_lineEdit.setMinimumSize(QSize(0, 38))
        self.firstname_lineEdit.setStyleSheet(u"font-size:14pt;color:rgb(52, 52, 52)")

        self.gridLayout.addWidget(self.firstname_lineEdit, 0, 1, 1, 1)

        self.label_password = QLabel(self.centralwidget)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setStyleSheet(u"font-size:15pt ;color:rgb(52, 52, 52)")

        self.gridLayout.addWidget(self.label_password, 3, 0, 1, 1)

        self.label_firstname = QLabel(self.centralwidget)
        self.label_firstname.setObjectName(u"label_firstname")
        self.label_firstname.setStyleSheet(u"font-size:15pt ;color:rgb(52, 52, 52)")

        self.gridLayout.addWidget(self.label_firstname, 0, 0, 1, 1)

        self.label_lastname = QLabel(self.centralwidget)
        self.label_lastname.setObjectName(u"label_lastname")
        self.label_lastname.setStyleSheet(u"font-size:15pt ;color:rgb(52, 52, 52)")

        self.gridLayout.addWidget(self.label_lastname, 1, 0, 1, 1)

        self.email_lineEdit = QLineEdit(self.centralwidget)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setMinimumSize(QSize(0, 38))
        self.email_lineEdit.setStyleSheet(u"font-size:14pt;color:rgb(52, 52, 52)")

        self.gridLayout.addWidget(self.email_lineEdit, 2, 1, 1, 1)

        self.label_email = QLabel(self.centralwidget)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setStyleSheet(u"font-size:15pt ;color:rgb(52, 52, 52)")

        self.gridLayout.addWidget(self.label_email, 2, 0, 1, 1)

        self.lastname_lineEdit = QLineEdit(self.centralwidget)
        self.lastname_lineEdit.setObjectName(u"lastname_lineEdit")
        self.lastname_lineEdit.setMinimumSize(QSize(0, 38))
        self.lastname_lineEdit.setStyleSheet(u"font-size:14pt;color:rgb(52, 52, 52)")

        self.gridLayout.addWidget(self.lastname_lineEdit, 1, 1, 1, 1)

        self.password_lineEdit = QLineEdit(self.centralwidget)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setMinimumSize(QSize(0, 38))
        self.password_lineEdit.setStyleSheet(u"font-size:14pt;color:rgb(52, 52, 52)")
        self.password_lineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.password_lineEdit, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(17, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.signup_pushButton = QPushButton(self.centralwidget)
        self.signup_pushButton.setObjectName(u"signup_pushButton")
        self.signup_pushButton.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setPointSize(17)
        self.signup_pushButton.setFont(font1)
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

        self.verticalLayout.addWidget(self.signup_pushButton)

        self.verticalSpacer_2 = QSpacerItem(524, 26, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.login_pushButton = QPushButton(self.centralwidget)
        self.login_pushButton.setObjectName(u"login_pushButton")
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

        self.horizontalLayout.addWidget(self.login_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        signup.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(signup)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 585, 22))
        signup.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(signup)
        self.statusbar.setObjectName(u"statusbar")
        signup.setStatusBar(self.statusbar)

        self.retranslateUi(signup)

        QMetaObject.connectSlotsByName(signup)
    # setupUi

    def retranslateUi(self, signup):
        signup.setWindowTitle(QCoreApplication.translate("signup", u"MainWindow", None))
        self.label_signup.setText(QCoreApplication.translate("signup", u"Sign up to Linkedin", None))
        self.label_password.setText(QCoreApplication.translate("signup", u"Password", None))
        self.label_firstname.setText(QCoreApplication.translate("signup", u"First name", None))
        self.label_lastname.setText(QCoreApplication.translate("signup", u"Last name", None))
        self.label_email.setText(QCoreApplication.translate("signup", u"Email", None))
        self.signup_pushButton.setText(QCoreApplication.translate("signup", u"sign up", None))
        self.label.setText(QCoreApplication.translate("signup", u"Do you have account?", None))
        self.login_pushButton.setText(QCoreApplication.translate("signup", u"Login", None))
    # retranslateUi

