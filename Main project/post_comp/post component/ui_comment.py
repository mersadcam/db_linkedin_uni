# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comment.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_comment(object):
    def setupUi(self, comment):
        if not comment.objectName():
            comment.setObjectName(u"comment")
        comment.resize(534, 448)
        self.label_comment = QLabel(comment)
        self.label_comment.setObjectName(u"label_comment")
        self.label_comment.setGeometry(QRect(10, 0, 121, 51))
        self.label_comment.setStyleSheet(u"font-size:15pt")
        self.line = QFrame(comment)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 25, 531, 51))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.Text_post = QPlainTextEdit(comment)
        self.Text_post.setObjectName(u"Text_post")
        self.Text_post.setGeometry(QRect(10, 70, 511, 301))
        self.ok_Button = QPushButton(comment)
        self.ok_Button.setObjectName(u"ok_Button")
        self.ok_Button.setGeometry(QRect(442, 380, 81, 28))
        self.ok_Button.setStyleSheet(u"QPushButton{\n"
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

        self.retranslateUi(comment)

        QMetaObject.connectSlotsByName(comment)
    # setupUi

    def retranslateUi(self, comment):
        comment.setWindowTitle(QCoreApplication.translate("comment", u"Dialog", None))
        self.label_comment.setText(QCoreApplication.translate("comment", u"Comment", None))
        self.ok_Button.setText(QCoreApplication.translate("comment", u"Ok", None))
    # retranslateUi

