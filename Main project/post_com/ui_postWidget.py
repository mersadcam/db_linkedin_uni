# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'postWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources.resources_rc

class Ui_postWidget(object):
    def setupUi(self, postWidget):
        if not postWidget.objectName():
            postWidget.setObjectName(u"postWidget")
        postWidget.resize(526, 528)
        postWidget.setStyleSheet(u"background:rgba(248, 253, 255, 206);\n"
"color:rgb(1, 31, 54);\n"
"")
        self.verticalLayout_2 = QVBoxLayout(postWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(postWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget#widget{\n"
"border:5px solid rgba(68, 170, 248, 35);\n"
"border-radius:10px;\n"
"color:rgb(1, 31, 54);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.firstname_label = QLabel(self.widget)
        self.firstname_label.setObjectName(u"firstname_label")
        self.firstname_label.setStyleSheet(u"font-size:15pt")

        self.horizontalLayout_3.addWidget(self.firstname_label)

        self.lastname_label = QLabel(self.widget)
        self.lastname_label.setObjectName(u"lastname_label")
        self.lastname_label.setStyleSheet(u"font-size:15pt")

        self.horizontalLayout_3.addWidget(self.lastname_label)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.content_plainTextEdit = QPlainTextEdit(self.widget)
        self.content_plainTextEdit.setObjectName(u"content_plainTextEdit")
        self.content_plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.content_plainTextEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.likes_label = QLabel(self.widget)
        self.likes_label.setObjectName(u"likes_label")
        self.likes_label.setStyleSheet(u"color:rgb(32, 74, 135)\n"
"")

        self.horizontalLayout_2.addWidget(self.likes_label)

        self.comments_label = QLabel(self.widget)
        self.comments_label.setObjectName(u"comments_label")
        self.comments_label.setStyleSheet(u"color:rgb(32, 74, 135);\n"
"")

        self.horizontalLayout_2.addWidget(self.comments_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.like_pushButton = QPushButton(self.widget)
        self.like_pushButton.setObjectName(u"like_pushButton")
        icon = QIcon()
        icon.addFile(u":/images/like-empty.png", QSize(), QIcon.Normal, QIcon.Off)
        self.like_pushButton.setIcon(icon)
        self.like_pushButton.setIconSize(QSize(25, 25))
        self.like_pushButton.setFlat(True)

        self.horizontalLayout.addWidget(self.like_pushButton)

        self.comment_pushButton = QPushButton(self.widget)
        self.comment_pushButton.setObjectName(u"comment_pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/images/comment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comment_pushButton.setIcon(icon1)
        self.comment_pushButton.setIconSize(QSize(25, 25))
        self.comment_pushButton.setFlat(True)

        self.horizontalLayout.addWidget(self.comment_pushButton)

        self.showComment_pushButton = QPushButton(self.widget)
        self.showComment_pushButton.setObjectName(u"showComment_pushButton")
        self.showComment_pushButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/images/eye.png", QSize(), QIcon.Normal, QIcon.Off)
        self.showComment_pushButton.setIcon(icon2)
        self.showComment_pushButton.setIconSize(QSize(25, 24))
        self.showComment_pushButton.setFlat(True)

        self.horizontalLayout.addWidget(self.showComment_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(postWidget)

        QMetaObject.connectSlotsByName(postWidget)
    # setupUi

    def retranslateUi(self, postWidget):
        postWidget.setWindowTitle(QCoreApplication.translate("postWidget", u"Form", None))
        self.firstname_label.setText(QCoreApplication.translate("postWidget", u"Firstname", None))
        self.lastname_label.setText(QCoreApplication.translate("postWidget", u"Lastname", None))
        self.likes_label.setText(QCoreApplication.translate("postWidget", u"Likes", None))
        self.comments_label.setText(QCoreApplication.translate("postWidget", u"Comments", None))
        self.like_pushButton.setText("")
        self.comment_pushButton.setText("")
        self.showComment_pushButton.setText("")
    # retranslateUi

