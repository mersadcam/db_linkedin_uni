# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contactInfo.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_contactInfoDialog(object):
    def setupUi(self, contactInfoDialog):
        if not contactInfoDialog.objectName():
            contactInfoDialog.setObjectName(u"contactInfoDialog")
        contactInfoDialog.resize(526, 528)
        contactInfoDialog.setStyleSheet(u"background:rgb(247, 252, 255);\n"
"color:rgb(1, 31, 54);\\n")
        self.gridLayout = QGridLayout(contactInfoDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 10, -1, -1)
        self.label_7 = QLabel(contactInfoDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.emailAddr_lineEdit = QLineEdit(contactInfoDialog)
        self.emailAddr_lineEdit.setObjectName(u"emailAddr_lineEdit")
        self.emailAddr_lineEdit.setMaxLength(255)
        self.emailAddr_lineEdit.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.emailAddr_lineEdit)


        self.gridLayout.addLayout(self.horizontalLayout_7, 7, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.label_3 = QLabel(contactInfoDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.headline_lineEdit = QLineEdit(contactInfoDialog)
        self.headline_lineEdit.setObjectName(u"headline_lineEdit")
        self.headline_lineEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.headline_lineEdit)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.close_pushButton = QPushButton(contactInfoDialog)
        self.close_pushButton.setObjectName(u"close_pushButton")
        self.close_pushButton.setMinimumSize(QSize(80, 0))
        self.close_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_pushButton.setStyleSheet(u"QPushButton{\n"
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
        self.close_pushButton.setFlat(True)

        self.horizontalLayout_9.addWidget(self.close_pushButton)


        self.gridLayout.addLayout(self.horizontalLayout_9, 10, 0, 1, 2)

        self.label_9 = QLabel(contactInfoDialog)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"margin-top:10px")

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.label = QLabel(contactInfoDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.firstname_lineEdit = QLineEdit(contactInfoDialog)
        self.firstname_lineEdit.setObjectName(u"firstname_lineEdit")
        self.firstname_lineEdit.setEnabled(True)
        self.firstname_lineEdit.setMinimumSize(QSize(150, 0))
        self.firstname_lineEdit.setMaximumSize(QSize(150, 16777215))
        self.firstname_lineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.firstname_lineEdit)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.label_2 = QLabel(contactInfoDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background:rgba(248, 253, 255, 206);\n"
"color:rgb(1, 31, 54);\\n")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lastname_lineEdit = QLineEdit(contactInfoDialog)
        self.lastname_lineEdit.setObjectName(u"lastname_lineEdit")
        self.lastname_lineEdit.setMinimumSize(QSize(150, 0))
        self.lastname_lineEdit.setMaximumSize(QSize(150, 16777215))
        self.lastname_lineEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lastname_lineEdit)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.line = QFrame(contactInfoDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, -1)
        self.label_5 = QLabel(contactInfoDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.addr_plainTextEdit = QPlainTextEdit(contactInfoDialog)
        self.addr_plainTextEdit.setObjectName(u"addr_plainTextEdit")
        self.addr_plainTextEdit.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.addr_plainTextEdit)


        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 0, 1, 2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 10, -1, -1)
        self.label_6 = QLabel(contactInfoDialog)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.bd_year_comboBox = QComboBox(contactInfoDialog)
        self.bd_year_comboBox.addItem("")
        self.bd_year_comboBox.setObjectName(u"bd_year_comboBox")
        self.bd_year_comboBox.setEditable(True)

        self.horizontalLayout_6.addWidget(self.bd_year_comboBox)

        self.bd_month_comboBox = QComboBox(contactInfoDialog)
        self.bd_month_comboBox.addItem("")
        self.bd_month_comboBox.addItem("")
        self.bd_month_comboBox.addItem("")
        self.bd_month_comboBox.addItem("")
        self.bd_month_comboBox.addItem("")
        self.bd_month_comboBox.addItem("")
        self.bd_month_comboBox.addItem("")
        self.bd_month_comboBox.addItem("")
        self.bd_month_comboBox.addItem("")
        self.bd_month_comboBox.addItem("")
        self.bd_month_comboBox.addItem("")
        self.bd_month_comboBox.addItem("")
        self.bd_month_comboBox.setObjectName(u"bd_month_comboBox")
        self.bd_month_comboBox.setEditable(True)

        self.horizontalLayout_6.addWidget(self.bd_month_comboBox)

        self.bd_day_comboBox = QComboBox(contactInfoDialog)
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.addItem("")
        self.bd_day_comboBox.setObjectName(u"bd_day_comboBox")
        self.bd_day_comboBox.setEditable(True)

        self.horizontalLayout_6.addWidget(self.bd_day_comboBox)


        self.gridLayout.addLayout(self.horizontalLayout_6, 6, 0, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 10, -1, -1)
        self.label_4 = QLabel(contactInfoDialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.country_comboBox = QComboBox(contactInfoDialog)
        self.country_comboBox.addItem("")
        self.country_comboBox.addItem("")
        self.country_comboBox.addItem("")
        self.country_comboBox.addItem("")
        self.country_comboBox.addItem("")
        self.country_comboBox.addItem("")
        self.country_comboBox.addItem("")
        self.country_comboBox.setObjectName(u"country_comboBox")
        self.country_comboBox.setEditable(True)

        self.horizontalLayout_4.addWidget(self.country_comboBox)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 10, -1, -1)
        self.label_8 = QLabel(contactInfoDialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.link_lineEdit = QLineEdit(contactInfoDialog)
        self.link_lineEdit.setObjectName(u"link_lineEdit")
        self.link_lineEdit.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.link_lineEdit)


        self.gridLayout.addLayout(self.horizontalLayout_8, 8, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 9, 0, 1, 1)


        self.retranslateUi(contactInfoDialog)

        QMetaObject.connectSlotsByName(contactInfoDialog)
    # setupUi

    def retranslateUi(self, contactInfoDialog):
        contactInfoDialog.setWindowTitle(QCoreApplication.translate("contactInfoDialog", u"Dialog", None))
        self.label_7.setText(QCoreApplication.translate("contactInfoDialog", u"Email address:", None))
        self.emailAddr_lineEdit.setText("")
        self.label_3.setText(QCoreApplication.translate("contactInfoDialog", u"Headline", None))
        self.close_pushButton.setText(QCoreApplication.translate("contactInfoDialog", u"Close", None))
        self.label_9.setText(QCoreApplication.translate("contactInfoDialog", u"Contact info:", None))
        self.label.setText(QCoreApplication.translate("contactInfoDialog", u"Firstname", None))
        self.label_2.setText(QCoreApplication.translate("contactInfoDialog", u"Lastname", None))
        self.label_5.setText(QCoreApplication.translate("contactInfoDialog", u"Address: ", None))
        self.label_6.setText(QCoreApplication.translate("contactInfoDialog", u"Birthday:", None))
        self.bd_year_comboBox.setItemText(0, QCoreApplication.translate("contactInfoDialog", u"Year", None))

        self.bd_month_comboBox.setItemText(0, QCoreApplication.translate("contactInfoDialog", u"January", None))
        self.bd_month_comboBox.setItemText(1, QCoreApplication.translate("contactInfoDialog", u"February", None))
        self.bd_month_comboBox.setItemText(2, QCoreApplication.translate("contactInfoDialog", u"March", None))
        self.bd_month_comboBox.setItemText(3, QCoreApplication.translate("contactInfoDialog", u"April", None))
        self.bd_month_comboBox.setItemText(4, QCoreApplication.translate("contactInfoDialog", u"May", None))
        self.bd_month_comboBox.setItemText(5, QCoreApplication.translate("contactInfoDialog", u"June", None))
        self.bd_month_comboBox.setItemText(6, QCoreApplication.translate("contactInfoDialog", u"July", None))
        self.bd_month_comboBox.setItemText(7, QCoreApplication.translate("contactInfoDialog", u"August", None))
        self.bd_month_comboBox.setItemText(8, QCoreApplication.translate("contactInfoDialog", u"September", None))
        self.bd_month_comboBox.setItemText(9, QCoreApplication.translate("contactInfoDialog", u"October", None))
        self.bd_month_comboBox.setItemText(10, QCoreApplication.translate("contactInfoDialog", u"November", None))
        self.bd_month_comboBox.setItemText(11, QCoreApplication.translate("contactInfoDialog", u"December", None))

        self.bd_day_comboBox.setItemText(0, QCoreApplication.translate("contactInfoDialog", u"1", None))
        self.bd_day_comboBox.setItemText(1, QCoreApplication.translate("contactInfoDialog", u"2", None))
        self.bd_day_comboBox.setItemText(2, QCoreApplication.translate("contactInfoDialog", u"3", None))
        self.bd_day_comboBox.setItemText(3, QCoreApplication.translate("contactInfoDialog", u"4", None))
        self.bd_day_comboBox.setItemText(4, QCoreApplication.translate("contactInfoDialog", u"5", None))
        self.bd_day_comboBox.setItemText(5, QCoreApplication.translate("contactInfoDialog", u"6", None))
        self.bd_day_comboBox.setItemText(6, QCoreApplication.translate("contactInfoDialog", u"7", None))
        self.bd_day_comboBox.setItemText(7, QCoreApplication.translate("contactInfoDialog", u"8", None))
        self.bd_day_comboBox.setItemText(8, QCoreApplication.translate("contactInfoDialog", u"9", None))
        self.bd_day_comboBox.setItemText(9, QCoreApplication.translate("contactInfoDialog", u"10", None))
        self.bd_day_comboBox.setItemText(10, QCoreApplication.translate("contactInfoDialog", u"11", None))
        self.bd_day_comboBox.setItemText(11, QCoreApplication.translate("contactInfoDialog", u"12", None))
        self.bd_day_comboBox.setItemText(12, QCoreApplication.translate("contactInfoDialog", u"13", None))
        self.bd_day_comboBox.setItemText(13, QCoreApplication.translate("contactInfoDialog", u"14", None))
        self.bd_day_comboBox.setItemText(14, QCoreApplication.translate("contactInfoDialog", u"15", None))
        self.bd_day_comboBox.setItemText(15, QCoreApplication.translate("contactInfoDialog", u"16", None))
        self.bd_day_comboBox.setItemText(16, QCoreApplication.translate("contactInfoDialog", u"17", None))
        self.bd_day_comboBox.setItemText(17, QCoreApplication.translate("contactInfoDialog", u"18", None))
        self.bd_day_comboBox.setItemText(18, QCoreApplication.translate("contactInfoDialog", u"19", None))
        self.bd_day_comboBox.setItemText(19, QCoreApplication.translate("contactInfoDialog", u"20", None))
        self.bd_day_comboBox.setItemText(20, QCoreApplication.translate("contactInfoDialog", u"21", None))
        self.bd_day_comboBox.setItemText(21, QCoreApplication.translate("contactInfoDialog", u"22", None))
        self.bd_day_comboBox.setItemText(22, QCoreApplication.translate("contactInfoDialog", u"23", None))
        self.bd_day_comboBox.setItemText(23, QCoreApplication.translate("contactInfoDialog", u"24", None))
        self.bd_day_comboBox.setItemText(24, QCoreApplication.translate("contactInfoDialog", u"25", None))
        self.bd_day_comboBox.setItemText(25, QCoreApplication.translate("contactInfoDialog", u"26", None))
        self.bd_day_comboBox.setItemText(26, QCoreApplication.translate("contactInfoDialog", u"27", None))
        self.bd_day_comboBox.setItemText(27, QCoreApplication.translate("contactInfoDialog", u"28", None))
        self.bd_day_comboBox.setItemText(28, QCoreApplication.translate("contactInfoDialog", u"29", None))
        self.bd_day_comboBox.setItemText(29, QCoreApplication.translate("contactInfoDialog", u"30", None))
        self.bd_day_comboBox.setItemText(30, QCoreApplication.translate("contactInfoDialog", u"31", None))

        self.label_4.setText(QCoreApplication.translate("contactInfoDialog", u"Country:", None))
        self.country_comboBox.setItemText(0, QCoreApplication.translate("contactInfoDialog", u"Iran", None))
        self.country_comboBox.setItemText(1, QCoreApplication.translate("contactInfoDialog", u"United States of America", None))
        self.country_comboBox.setItemText(2, QCoreApplication.translate("contactInfoDialog", u"Iraq", None))
        self.country_comboBox.setItemText(3, QCoreApplication.translate("contactInfoDialog", u"Russia", None))
        self.country_comboBox.setItemText(4, QCoreApplication.translate("contactInfoDialog", u"Turkey", None))
        self.country_comboBox.setItemText(5, QCoreApplication.translate("contactInfoDialog", u"Germany", None))
        self.country_comboBox.setItemText(6, QCoreApplication.translate("contactInfoDialog", u"France", None))

        self.label_8.setText(QCoreApplication.translate("contactInfoDialog", u"Link: ", None))
    # retranslateUi

