# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'post_component.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons

class Ui_post_component(object):
    def setupUi(self, post_component):
        if not post_component.objectName():
            post_component.setObjectName(u"post_component")
        post_component.resize(526, 528)
        self.label_post = QLabel(post_component)
        self.label_post.setObjectName(u"label_post")
        self.label_post.setGeometry(QRect(10, 100, 501, 151))
        self.label_firstname = QLabel(post_component)
        self.label_firstname.setObjectName(u"label_firstname")
        self.label_firstname.setGeometry(QRect(20, 20, 181, 41))
        self.label_firstname.setStyleSheet(u"font-size:15pt")
        self.label_lastname = QLabel(post_component)
        self.label_lastname.setObjectName(u"label_lastname")
        self.label_lastname.setGeometry(QRect(220, 20, 211, 41))
        self.label_lastname.setStyleSheet(u"font-size:15pt")
        self.label_num_likes = QLabel(post_component)
        self.label_num_likes.setObjectName(u"label_num_likes")
        self.label_num_likes.setGeometry(QRect(10, 280, 141, 31))
        self.label_num_likes.setStyleSheet(u"color:rgb(255, 185, 8);\n"
"font-size:10pt")
        self.label_value_num_likes = QLabel(post_component)
        self.label_value_num_likes.setObjectName(u"label_value_num_likes")
        self.label_value_num_likes.setGeometry(QRect(160, 280, 121, 31))
        self.label_num_comments = QLabel(post_component)
        self.label_num_comments.setObjectName(u"label_num_comments")
        self.label_num_comments.setGeometry(QRect(10, 320, 171, 16))
        self.label_num_comments.setStyleSheet(u"color:rgb(255, 185, 8);\n"
"font-size:10pt;")
        self.label_value_num_comments = QLabel(post_component)
        self.label_value_num_comments.setObjectName(u"label_value_num_comments")
        self.label_value_num_comments.setGeometry(QRect(190, 320, 111, 20))
        self.likeButton = QPushButton(post_component)
        self.likeButton.setObjectName(u"likeButton")
        self.likeButton.setGeometry(QRect(10, 350, 51, 51))
        icon = QIcon()
        icon.addFile(u":/like.png", QSize(), QIcon.Normal, QIcon.Off)
        self.likeButton.setIcon(icon)
        self.likeButton.setIconSize(QSize(40, 40))
        self.line = QFrame(post_component)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 70, 621, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.commentButton = QPushButton(post_component)
        self.commentButton.setObjectName(u"commentButton")
        self.commentButton.setGeometry(QRect(70, 350, 51, 51))
        icon1 = QIcon()
        icon1.addFile(u":/comment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commentButton.setIcon(icon1)
        self.commentButton.setIconSize(QSize(40, 40))
        self.show_commentButton = QPushButton(post_component)
        self.show_commentButton.setObjectName(u"show_commentButton")
        self.show_commentButton.setGeometry(QRect(10, 410, 111, 31))
        self.show_commentButton.setStyleSheet(u"QPushButton{\n"
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

        self.retranslateUi(post_component)

        QMetaObject.connectSlotsByName(post_component)
    # setupUi

    def retranslateUi(self, post_component):
        post_component.setWindowTitle(QCoreApplication.translate("post_component", u"Form", None))
        self.label_post.setText(QCoreApplication.translate("post_component", u"post", None))
        self.label_firstname.setText(QCoreApplication.translate("post_component", u"Firstname", None))
        self.label_lastname.setText(QCoreApplication.translate("post_component", u"Lastname", None))
        self.label_num_likes.setText(QCoreApplication.translate("post_component", u"number of likes:", None))
        self.label_value_num_likes.setText("")
        self.label_num_comments.setText(QCoreApplication.translate("post_component", u"number of comments:", None))
        self.label_value_num_comments.setText("")
        self.likeButton.setText("")
        self.commentButton.setText("")
        self.show_commentButton.setText(QCoreApplication.translate("post_component", u"show comment", None))
    # retranslateUi

