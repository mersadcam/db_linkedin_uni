# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editAbout.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources

class Ui_EditAboutDialog(object):
    def setupUi(self, EditAboutDialog):
        if not EditAboutDialog.objectName():
            EditAboutDialog.setObjectName(u"EditAboutDialog")
        EditAboutDialog.resize(490, 378)
        EditAboutDialog.setStyleSheet(u"background:rgb(247, 252, 255);\n"
"color:rgb(1, 31, 54);\\n")
        self.verticalLayout = QVBoxLayout(EditAboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.label = QLabel(EditAboutDialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(55, 55))
        self.label.setMaximumSize(QSize(55, 55))
        self.label.setPixmap(QPixmap(u":/images/User-Profile-PNG-Image.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.firstname_label = QLabel(EditAboutDialog)
        self.firstname_label.setObjectName(u"firstname_label")
        self.firstname_label.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setPointSize(15)
        self.firstname_label.setFont(font)
        self.firstname_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.firstname_label)

        self.lastname_label = QLabel(EditAboutDialog)
        self.lastname_label.setObjectName(u"lastname_label")
        self.lastname_label.setMinimumSize(QSize(0, 25))
        self.lastname_label.setFont(font)
        self.lastname_label.setStyleSheet(u"background:rgba(248, 253, 255, 206);\n"
"color:rgb(1, 31, 54);\\n")
        self.lastname_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lastname_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(EditAboutDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_9 = QLabel(EditAboutDialog)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setPointSize(17)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"margin-top:10px")

        self.verticalLayout.addWidget(self.label_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, -1)
        self.about_plainTextEdit = QPlainTextEdit(EditAboutDialog)
        self.about_plainTextEdit.setObjectName(u"about_plainTextEdit")

        self.horizontalLayout_5.addWidget(self.about_plainTextEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(17, 37, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.cancel_pushButton = QPushButton(EditAboutDialog)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")
        self.cancel_pushButton.setMinimumSize(QSize(80, 0))
        self.cancel_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_pushButton.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background:rgb(186, 189, 182);\n"
"border:1px solid white;\n"
"border-radius:5px;\n"
"padding:5px;\n"
"}\n"
"")
        self.cancel_pushButton.setFlat(True)

        self.horizontalLayout_9.addWidget(self.cancel_pushButton)

        self.save_pushButton = QPushButton(EditAboutDialog)
        self.save_pushButton.setObjectName(u"save_pushButton")
        self.save_pushButton.setMinimumSize(QSize(80, 0))
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
        self.save_pushButton.setFlat(True)

        self.horizontalLayout_9.addWidget(self.save_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.retranslateUi(EditAboutDialog)

        QMetaObject.connectSlotsByName(EditAboutDialog)
    # setupUi

    def retranslateUi(self, EditAboutDialog):
        EditAboutDialog.setWindowTitle(QCoreApplication.translate("EditAboutDialog", u"Dialog", None))
        self.label.setText("")
        self.firstname_label.setText(QCoreApplication.translate("EditAboutDialog", u"Firstname", None))
        self.lastname_label.setText(QCoreApplication.translate("EditAboutDialog", u"Lastname", None))
        self.label_9.setText(QCoreApplication.translate("EditAboutDialog", u"About", None))
        self.about_plainTextEdit.setPlaceholderText(QCoreApplication.translate("EditAboutDialog", u"Write about yourself ...", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("EditAboutDialog", u"Cancel", None))
        self.save_pushButton.setText(QCoreApplication.translate("EditAboutDialog", u"Save", None))
    # retranslateUi

