# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'commentPostView.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_commentPostView(object):
    def setupUi(self, commentPostView):
        if not commentPostView.objectName():
            commentPostView.setObjectName(u"commentPostView")
        commentPostView.resize(598, 818)
        self.verticalLayout = QVBoxLayout(commentPostView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainContent_widget = QWidget(commentPostView)
        self.mainContent_widget.setObjectName(u"mainContent_widget")

        self.verticalLayout.addWidget(self.mainContent_widget)

        self.comment_scrollArea = QScrollArea(commentPostView)
        self.comment_scrollArea.setObjectName(u"comment_scrollArea")
        self.comment_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 578, 439))
        self.comment_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.comment_scrollArea)

        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 5)

        self.retranslateUi(commentPostView)

        QMetaObject.connectSlotsByName(commentPostView)
    # setupUi

    def retranslateUi(self, commentPostView):
        commentPostView.setWindowTitle(QCoreApplication.translate("commentPostView", u"Dialog", None))
    # retranslateUi

