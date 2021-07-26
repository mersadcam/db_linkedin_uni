# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userView.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources.resources_rc

class Ui_userView(object):
    def setupUi(self, userView):
        if not userView.objectName():
            userView.setObjectName(u"userView")
        userView.resize(400, 128)
        userView.setStyleSheet(u"background:rgba(248, 253, 255, 206);\n"
"color:rgb(1, 31, 54);")
        self.verticalLayout = QVBoxLayout(userView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.userView_widget = QWidget(userView)
        self.userView_widget.setObjectName(u"userView_widget")
        self.userView_widget.setMinimumSize(QSize(0, 110))
        self.userView_widget.setMaximumSize(QSize(16777215, 117))
        self.userView_widget.setStyleSheet(u"QWidget#profile_widget{border:1px solid rgb(48, 162, 249)}")
        self.horizontalLayout_4 = QHBoxLayout(self.userView_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.img_label = QLabel(self.userView_widget)
        self.img_label.setObjectName(u"img_label")
        self.img_label.setMinimumSize(QSize(95, 95))
        self.img_label.setMaximumSize(QSize(95, 95))
        self.img_label.setCursor(QCursor(Qt.PointingHandCursor))
        self.img_label.setPixmap(QPixmap(u":/images/User-Profile-PNG-Image.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(Qt.AlignCenter)
        self.img_label.setWordWrap(False)
        self.img_label.setIndent(0)

        self.horizontalLayout_4.addWidget(self.img_label)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.firstname_label = QLabel(self.userView_widget)
        self.firstname_label.setObjectName(u"firstname_label")
        font = QFont()
        font.setPointSize(11)
        self.firstname_label.setFont(font)

        self.horizontalLayout_3.addWidget(self.firstname_label)

        self.lastname_label = QLabel(self.userView_widget)
        self.lastname_label.setObjectName(u"lastname_label")
        self.lastname_label.setFont(font)

        self.horizontalLayout_3.addWidget(self.lastname_label)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.headline_plainTextEdit = QPlainTextEdit(self.userView_widget)
        self.headline_plainTextEdit.setObjectName(u"headline_plainTextEdit")
        self.headline_plainTextEdit.setStyleSheet(u"border:none;")
        self.headline_plainTextEdit.setReadOnly(True)
        self.headline_plainTextEdit.setMaximumBlockCount(0)
        self.headline_plainTextEdit.setBackgroundVisible(False)
        self.headline_plainTextEdit.setCenterOnScroll(False)

        self.verticalLayout_4.addWidget(self.headline_plainTextEdit)

        self.verticalLayout_4.setStretch(0, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_4)


        self.verticalLayout.addWidget(self.userView_widget)


        self.retranslateUi(userView)

        QMetaObject.connectSlotsByName(userView)
    # setupUi

    def retranslateUi(self, userView):
        userView.setWindowTitle(QCoreApplication.translate("userView", u"Form", None))
        self.img_label.setText("")
        self.firstname_label.setText(QCoreApplication.translate("userView", u"Firstname", None))
        self.lastname_label.setText(QCoreApplication.translate("userView", u"Lastname", None))
        self.headline_plainTextEdit.setPlainText(QCoreApplication.translate("userView", u"Headline...\n"
"", None))
    # retranslateUi

