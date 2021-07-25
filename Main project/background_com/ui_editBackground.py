# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editBackground.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources.resources_rc

class Ui_EditBackgroundDialog(object):
    def setupUi(self, EditBackgroundDialog):
        if not EditBackgroundDialog.objectName():
            EditBackgroundDialog.setObjectName(u"EditBackgroundDialog")
        EditBackgroundDialog.resize(358, 378)
        EditBackgroundDialog.setStyleSheet(u"background:rgb(247, 252, 255);\n"
"color:rgb(1, 31, 54);\\n")
        self.verticalLayout = QVBoxLayout(EditBackgroundDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(EditBackgroundDialog)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setPointSize(17)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"margin-top:10px")

        self.verticalLayout.addWidget(self.label_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(EditBackgroundDialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.title_lineEdit = QLineEdit(EditBackgroundDialog)
        self.title_lineEdit.setObjectName(u"title_lineEdit")

        self.horizontalLayout_5.addWidget(self.title_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(EditBackgroundDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.env_comboBox = QComboBox(EditBackgroundDialog)
        self.env_comboBox.setObjectName(u"env_comboBox")

        self.horizontalLayout.addWidget(self.env_comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(EditBackgroundDialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.startTime_comboBox = QComboBox(EditBackgroundDialog)
        self.startTime_comboBox.setObjectName(u"startTime_comboBox")

        self.horizontalLayout_4.addWidget(self.startTime_comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(EditBackgroundDialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.endTime_comboBox = QComboBox(EditBackgroundDialog)
        self.endTime_comboBox.setObjectName(u"endTime_comboBox")

        self.horizontalLayout_3.addWidget(self.endTime_comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(EditBackgroundDialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.description_plainTextEdit = QPlainTextEdit(EditBackgroundDialog)
        self.description_plainTextEdit.setObjectName(u"description_plainTextEdit")

        self.horizontalLayout_2.addWidget(self.description_plainTextEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.cancel_pushButton = QPushButton(EditBackgroundDialog)
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

        self.save_pushButton = QPushButton(EditBackgroundDialog)
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


        self.retranslateUi(EditBackgroundDialog)

        QMetaObject.connectSlotsByName(EditBackgroundDialog)
    # setupUi

    def retranslateUi(self, EditBackgroundDialog):
        EditBackgroundDialog.setWindowTitle(QCoreApplication.translate("EditBackgroundDialog", u"Dialog", None))
        self.label_9.setText(QCoreApplication.translate("EditBackgroundDialog", u"Edit background", None))
        self.label_4.setText(QCoreApplication.translate("EditBackgroundDialog", u"Title", None))
        self.label.setText(QCoreApplication.translate("EditBackgroundDialog", u"Environment", None))
        self.label_2.setText(QCoreApplication.translate("EditBackgroundDialog", u"Start time", None))
        self.label_3.setText(QCoreApplication.translate("EditBackgroundDialog", u"End time", None))
        self.label_5.setText(QCoreApplication.translate("EditBackgroundDialog", u"Description", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("EditBackgroundDialog", u"Cancel", None))
        self.save_pushButton.setText(QCoreApplication.translate("EditBackgroundDialog", u"Save", None))
    # retranslateUi

