# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editSkills.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources.resources_rc

class Ui_EditSkillsDialog(object):
    def setupUi(self, EditSkillsDialog):
        if not EditSkillsDialog.objectName():
            EditSkillsDialog.setObjectName(u"EditSkillsDialog")
        EditSkillsDialog.resize(490, 378)
        EditSkillsDialog.setStyleSheet(u"background:rgb(247, 252, 255);\n"
"color:rgb(1, 31, 54);\\n")
        self.verticalLayout = QVBoxLayout(EditSkillsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.label = QLabel(EditSkillsDialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(55, 55))
        self.label.setMaximumSize(QSize(55, 55))
        self.label.setPixmap(QPixmap(u":/images/User-Profile-PNG-Image.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.firstname_label = QLabel(EditSkillsDialog)
        self.firstname_label.setObjectName(u"firstname_label")
        self.firstname_label.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setPointSize(15)
        self.firstname_label.setFont(font)
        self.firstname_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.firstname_label)

        self.lastname_label = QLabel(EditSkillsDialog)
        self.lastname_label.setObjectName(u"lastname_label")
        self.lastname_label.setMinimumSize(QSize(0, 25))
        self.lastname_label.setFont(font)
        self.lastname_label.setStyleSheet(u"background:rgba(248, 253, 255, 206);\n"
"color:rgb(1, 31, 54);\\n")
        self.lastname_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lastname_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(EditSkillsDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_9 = QLabel(EditSkillsDialog)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setPointSize(17)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"margin-top:10px")

        self.verticalLayout.addWidget(self.label_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.skills_comboBox = QComboBox(EditSkillsDialog)
        self.skills_comboBox.setObjectName(u"skills_comboBox")

        self.horizontalLayout_2.addWidget(self.skills_comboBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.add_pushButton = QPushButton(EditSkillsDialog)
        self.add_pushButton.setObjectName(u"add_pushButton")
        self.add_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/images/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_pushButton.setIcon(icon)
        self.add_pushButton.setIconSize(QSize(25, 25))
        self.add_pushButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.add_pushButton)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.scrollArea = QScrollArea(EditSkillsDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 470, 96))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalSpacer = QSpacerItem(17, 37, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.cancel_pushButton = QPushButton(EditSkillsDialog)
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

        self.save_pushButton = QPushButton(EditSkillsDialog)
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


        self.retranslateUi(EditSkillsDialog)

        QMetaObject.connectSlotsByName(EditSkillsDialog)
    # setupUi

    def retranslateUi(self, EditSkillsDialog):
        EditSkillsDialog.setWindowTitle(QCoreApplication.translate("EditSkillsDialog", u"Dialog", None))
        self.label.setText("")
        self.firstname_label.setText(QCoreApplication.translate("EditSkillsDialog", u"Firstname", None))
        self.lastname_label.setText(QCoreApplication.translate("EditSkillsDialog", u"Lastname", None))
        self.label_9.setText(QCoreApplication.translate("EditSkillsDialog", u"Edit skills", None))
        self.add_pushButton.setText("")
        self.cancel_pushButton.setText(QCoreApplication.translate("EditSkillsDialog", u"Cancel", None))
        self.save_pushButton.setText(QCoreApplication.translate("EditSkillsDialog", u"Save", None))
    # retranslateUi

