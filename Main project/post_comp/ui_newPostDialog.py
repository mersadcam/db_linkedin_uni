# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newPostDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources.resources_rc

class Ui_newPost(object):
    def setupUi(self, newPost):
        if not newPost.objectName():
            newPost.setObjectName(u"newPost")
        newPost.resize(526, 528)
        newPost.setStyleSheet(u"background:rgb(246, 250, 252);\n"
"color:rgb(1, 31, 54);\\n")
        self.verticalLayout = QVBoxLayout(newPost)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.label = QLabel(newPost)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(55, 55))
        self.label.setMaximumSize(QSize(55, 55))
        self.label.setPixmap(QPixmap(u":/images/User-Profile-PNG-Image.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.firstname_label = QLabel(newPost)
        self.firstname_label.setObjectName(u"firstname_label")
        self.firstname_label.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setPointSize(15)
        self.firstname_label.setFont(font)
        self.firstname_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.firstname_label)

        self.lastname_label = QLabel(newPost)
        self.lastname_label.setObjectName(u"lastname_label")
        self.lastname_label.setMinimumSize(QSize(0, 25))
        self.lastname_label.setFont(font)
        self.lastname_label.setStyleSheet(u"background:rgba(248, 253, 255, 206);\n"
"color:rgb(1, 31, 54);\\n")
        self.lastname_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lastname_label)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(newPost)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_Create = QLabel(newPost)
        self.label_Create.setObjectName(u"label_Create")
        self.label_Create.setStyleSheet(u"margin-top:10px;\n"
"font-size:25px;\n"
"")

        self.verticalLayout.addWidget(self.label_Create)

        self.postText_plainTextEdit = QPlainTextEdit(newPost)
        self.postText_plainTextEdit.setObjectName(u"postText_plainTextEdit")

        self.verticalLayout.addWidget(self.postText_plainTextEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.post_pushButton = QPushButton(newPost)
        self.post_pushButton.setObjectName(u"post_pushButton")
        self.post_pushButton.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.post_pushButton)

        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)

        self.retranslateUi(newPost)

        QMetaObject.connectSlotsByName(newPost)
    # setupUi

    def retranslateUi(self, newPost):
        newPost.setWindowTitle(QCoreApplication.translate("newPost", u"Dialog", None))
        self.label.setText("")
        self.firstname_label.setText(QCoreApplication.translate("newPost", u"Firstname", None))
        self.lastname_label.setText(QCoreApplication.translate("newPost", u"Lastname", None))
        self.label_Create.setText(QCoreApplication.translate("newPost", u"Create a post", None))
        self.postText_plainTextEdit.setPlaceholderText(QCoreApplication.translate("newPost", u"what do you want to talk about?", None))
        self.post_pushButton.setText(QCoreApplication.translate("newPost", u"Post", None))
    # retranslateUi

