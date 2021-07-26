# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewCommentWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc

class Ui_viewCommentWidget(object):
    def setupUi(self, viewCommentWidget):
        if not viewCommentWidget.objectName():
            viewCommentWidget.setObjectName(u"viewCommentWidget")
        viewCommentWidget.resize(554, 205)
        viewCommentWidget.setStyleSheet(u"background:rgb(246, 250, 252);\n"
"color:rgb(1, 31, 54);\\n")
        self.verticalLayout = QVBoxLayout(viewCommentWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.firstname_label = QLabel(viewCommentWidget)
        self.firstname_label.setObjectName(u"firstname_label")
        self.firstname_label.setStyleSheet(u"font-size:15pt")

        self.horizontalLayout_3.addWidget(self.firstname_label)

        self.lastname_label = QLabel(viewCommentWidget)
        self.lastname_label.setObjectName(u"lastname_label")
        self.lastname_label.setStyleSheet(u"font-size:15pt")

        self.horizontalLayout_3.addWidget(self.lastname_label)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line = QFrame(viewCommentWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.content_plainTextEdit = QPlainTextEdit(viewCommentWidget)
        self.content_plainTextEdit.setObjectName(u"content_plainTextEdit")
        self.content_plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.content_plainTextEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.likes_label = QLabel(viewCommentWidget)
        self.likes_label.setObjectName(u"likes_label")
        self.likes_label.setStyleSheet(u"color:rgb(32, 74, 135)\n"
"")

        self.horizontalLayout_2.addWidget(self.likes_label)

        self.comments_label = QLabel(viewCommentWidget)
        self.comments_label.setObjectName(u"comments_label")
        self.comments_label.setStyleSheet(u"color:rgb(32, 74, 135);\n"
"")

        self.horizontalLayout_2.addWidget(self.comments_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.like_pushButton = QPushButton(viewCommentWidget)
        self.like_pushButton.setObjectName(u"like_pushButton")
        icon = QIcon()
        icon.addFile(u":/images/like-empty.png", QSize(), QIcon.Normal, QIcon.Off)
        self.like_pushButton.setIcon(icon)
        self.like_pushButton.setIconSize(QSize(25, 25))
        self.like_pushButton.setFlat(True)

        self.horizontalLayout.addWidget(self.like_pushButton)

        self.comment_pushButton = QPushButton(viewCommentWidget)
        self.comment_pushButton.setObjectName(u"comment_pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/images/comment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comment_pushButton.setIcon(icon1)
        self.comment_pushButton.setIconSize(QSize(25, 25))
        self.comment_pushButton.setFlat(True)

        self.horizontalLayout.addWidget(self.comment_pushButton)

        self.showComment_pushButton = QPushButton(viewCommentWidget)
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


        self.retranslateUi(viewCommentWidget)

        QMetaObject.connectSlotsByName(viewCommentWidget)
    # setupUi

    def retranslateUi(self, viewCommentWidget):
        viewCommentWidget.setWindowTitle(QCoreApplication.translate("viewCommentWidget", u"Form", None))
        self.firstname_label.setText(QCoreApplication.translate("viewCommentWidget", u"Firstname", None))
        self.lastname_label.setText(QCoreApplication.translate("viewCommentWidget", u"Lastname", None))
        self.likes_label.setText(QCoreApplication.translate("viewCommentWidget", u"Likes", None))
        self.comments_label.setText(QCoreApplication.translate("viewCommentWidget", u"Comments", None))
        self.like_pushButton.setText("")
        self.comment_pushButton.setText("")
        self.showComment_pushButton.setText("")
    # retranslateUi

