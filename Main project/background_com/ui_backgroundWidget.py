# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'backgroundWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_backgroundWidget(object):
    def setupUi(self, backgroundWidget):
        if not backgroundWidget.objectName():
            backgroundWidget.setObjectName(u"backgroundWidget")
        backgroundWidget.resize(1080, 198)
        backgroundWidget.setStyleSheet(u"QWidget#backgroundWidget{\n"
"border:1px solid rgb(48, 162, 249);\n"
"border-radius:10px;\n"
"background:rgba(248, 253, 255, 206);\n"
"color:rgb(1, 31, 54);\n"
"}")
        self.verticalLayout = QVBoxLayout(backgroundWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.title_label = QLabel(backgroundWidget)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)

        self.verticalLayout.addWidget(self.title_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(backgroundWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.compName_label = QLabel(backgroundWidget)
        self.compName_label.setObjectName(u"compName_label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.compName_label.setFont(font1)

        self.horizontalLayout.addWidget(self.compName_label)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(backgroundWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.startYear_label = QLabel(backgroundWidget)
        self.startYear_label.setObjectName(u"startYear_label")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.startYear_label.setFont(font2)
        self.startYear_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.startYear_label)

        self.label_5 = QLabel(backgroundWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.endYear_label = QLabel(backgroundWidget)
        self.endYear_label.setObjectName(u"endYear_label")
        self.endYear_label.setFont(font2)
        self.endYear_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.endYear_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.setStretch(4, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.description_plainTextEdit = QPlainTextEdit(backgroundWidget)
        self.description_plainTextEdit.setObjectName(u"description_plainTextEdit")

        self.verticalLayout.addWidget(self.description_plainTextEdit)


        self.retranslateUi(backgroundWidget)

        QMetaObject.connectSlotsByName(backgroundWidget)
    # setupUi

    def retranslateUi(self, backgroundWidget):
        backgroundWidget.setWindowTitle(QCoreApplication.translate("backgroundWidget", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("backgroundWidget", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("backgroundWidget", u"In", None))
        self.compName_label.setText(QCoreApplication.translate("backgroundWidget", u"Apple company", None))
        self.label_3.setText(QCoreApplication.translate("backgroundWidget", u"From", None))
        self.startYear_label.setText(QCoreApplication.translate("backgroundWidget", u"start_year", None))
        self.label_5.setText(QCoreApplication.translate("backgroundWidget", u"to", None))
        self.endYear_label.setText(QCoreApplication.translate("backgroundWidget", u"end_year", None))
    # retranslateUi

