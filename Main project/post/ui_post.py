# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'post.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc
import resources_rc

class Ui_post(object):
    def setupUi(self, post):
        if not post.objectName():
            post.setObjectName(u"post")
        post.resize(526, 528)
        self.label_Create = QLabel(post)
        self.label_Create.setObjectName(u"label_Create")
        self.label_Create.setGeometry(QRect(10, 0, 161, 51))
        self.label_Create.setStyleSheet(u"margin-top:10px;\n"
"font-size:25px;\n"
"")
        self.line = QFrame(post)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 35, 511, 51))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_questuin = QLabel(post)
        self.label_questuin.setObjectName(u"label_questuin")
        self.label_questuin.setGeometry(QRect(10, 190, 371, 71))
        self.plainTextEdit = QPlainTextEdit(post)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 240, 501, 181))
        self.postButton = QPushButton(post)
        self.postButton.setObjectName(u"postButton")
        self.postButton.setGeometry(QRect(420, 440, 93, 28))
        self.postButton.setStyleSheet(u"QPushButton{\n"
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
        self.firstname_label = QLabel(post)
        self.firstname_label.setObjectName(u"firstname_label")
        self.firstname_label.setGeometry(QRect(80, 80, 194, 50))
        self.firstname_label.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setPointSize(10)
        self.firstname_label.setFont(font)
        self.firstname_label.setStyleSheet(u"font-size:10pt")
        self.firstname_label.setAlignment(Qt.AlignCenter)
        self.lastname_label = QLabel(post)
        self.lastname_label.setObjectName(u"lastname_label")
        self.lastname_label.setGeometry(QRect(250, 80, 194, 50))
        self.lastname_label.setMinimumSize(QSize(0, 25))
        self.lastname_label.setFont(font)
        self.lastname_label.setStyleSheet(u"font-size:10pt")
        self.lastname_label.setAlignment(Qt.AlignCenter)
        self.label_pic = QLabel(post)
        self.label_pic.setObjectName(u"label_pic")
        self.label_pic.setGeometry(QRect(10, 70, 81, 61))
        self.label_pic.setPixmap(QPixmap(u"User-Profile-PNG-Image.png"))
        self.label_pic.setScaledContents(True)

        self.retranslateUi(post)

        QMetaObject.connectSlotsByName(post)
    # setupUi

    def retranslateUi(self, post):
        post.setWindowTitle(QCoreApplication.translate("post", u"Dialog", None))
        self.label_Create.setText(QCoreApplication.translate("post", u"Create a post", None))
        self.label_questuin.setText(QCoreApplication.translate("post", u"what do you want to talk about?", None))
        self.postButton.setText(QCoreApplication.translate("post", u"Post", None))
        self.firstname_label.setText(QCoreApplication.translate("post", u"Firstname", None))
        self.lastname_label.setText(QCoreApplication.translate("post", u"Lastname", None))
        self.label_pic.setText("")
    # retranslateUi

