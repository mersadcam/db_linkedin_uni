# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newCommentDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_newComment(object):
    def setupUi(self, newComment):
        if not newComment.objectName():
            newComment.setObjectName(u"newComment")
        newComment.resize(534, 448)
        self.verticalLayout = QVBoxLayout(newComment)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_comment = QLabel(newComment)
        self.label_comment.setObjectName(u"label_comment")
        self.label_comment.setStyleSheet(u"font-size:15pt")

        self.verticalLayout.addWidget(self.label_comment)

        self.line = QFrame(newComment)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.content_plainTextEdit = QPlainTextEdit(newComment)
        self.content_plainTextEdit.setObjectName(u"content_plainTextEdit")

        self.verticalLayout.addWidget(self.content_plainTextEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_pushButton = QPushButton(newComment)
        self.save_pushButton.setObjectName(u"save_pushButton")
        self.save_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_pushButton.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.save_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(newComment)

        QMetaObject.connectSlotsByName(newComment)
    # setupUi

    def retranslateUi(self, newComment):
        newComment.setWindowTitle(QCoreApplication.translate("newComment", u"Dialog", None))
        self.label_comment.setText(QCoreApplication.translate("newComment", u"Comment", None))
        self.save_pushButton.setText(QCoreApplication.translate("newComment", u"Save", None))
    # retranslateUi

