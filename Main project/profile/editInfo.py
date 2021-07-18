from ui_editInfo import Ui_EditInfoDialog
from PySide6.QtWidgets import QDialog
from PySide2.QtCore import QObject, Signal, Slot
import enum
import datetime


class Country(enum.Enum):
    IRAN = 0
    USA = 1
    IRAQ = 2
    RUSSIA = 3
    TURKEY = 4
    GERMAN = 5
    FRANCE = 6

    @staticmethod
    def case(inp):
        if inp == 0 or inp == "Iran":
            return Country.IRAN
        if inp == 1 or inp == "United States of America":
            return Country.USA
        if inp == 2 or inp == "Iraq":
            return Country.IRAQ
        if inp == 3 or inp == "Russia":
            return Country.RUSSIA
        if inp == 4 or inp == "Turkey":
            return Country.TURKEY
        if inp == 5 or inp == "Germany":
            return Country.GERMAN
        return Country.FRANCE

    # @staticmethod
    # def by_index(index):
    #     if index == 0:
    #         return Country.IRAN
    #     if index == 1:
    #         return Country.IRAQ
    #     if index == 2:
    #         return Country.USA
    #     if index == 3:
    #         return Country.RUSSIA
    #     if index == 4:
    #         return Country.TURKEY
    #     if index == 5:
    #         return Country.GERMAN
    #     if index == 6:
    #         return Country.FRANCE


class EditInfo(QDialog):
    edit_saved = Signal(str, str, str, int, str, datetime.datetime, str, str)

    def __init__(self):
        super(EditInfo, self).__init__()
        self.ui = Ui_EditInfoDialog()
        self.ui.setupUi(self)

        for i in range(1800, 2022):
            self.ui.bd_year_comboBox.setItemText(i - 1800, str(i))

        self.ui.cancel_pushButton.clicked.connect(self.cancel_pushButton_onClicked)
        self.ui.save_pushButton.clicked.connect(self.save_pushButton_onClicked)

    def fill_fields(self, firstname, lastname, headline, country,
                    addr, birthday: datetime.datetime, email_addr, link):
        ui = self.ui
        ui.firstname_lineEdit.setText(firstname)
        ui.lastname_lineEdit.setText(lastname)
        ui.country_comboBox.setCurrentIndex(country.value)
        ui.headline_lineEdit.setText(headline)
        ui.addr_plainTextEdit.setPlainText(addr)

        # birthday
        if birthday is not None:
            ui.bd_year_comboBox.setCurrentText(str(birthday.year))
            ui.bd_month_comboBox.setCurrentText(str(birthday.month))
            ui.bd_day_comboBox.setCurrentText(str(birthday.day))
        if email_addr is not None:
            ui.emailAddr_lineEdit.setText(email_addr)
        if link is not None:
            ui.link_lineEdit.setText(link)

    @Slot()
    def save_pushButton_onClicked(self):
        ui = self.ui
        firstname = ui.firstname_lineEdit.text()
        lastname = ui.lastname_lineEdit.text()
        country = Country.case(ui.country_comboBox.currentIndex())
        headline = ui.headline_lineEdit.text()
        addr = ui.addr_plainTextEdit.toPlainText()
        birthday = datetime.datetime(int(ui.bd_year_comboBox.currentText()),
                                     ui.bd_month_comboBox.currentIndex() + 1, int(ui.bd_day_comboBox.currentText()))
        email_addr = ui.emailAddr_lineEdit.text()
        link = ui.link_lineEdit.text()
        self.edit_saved.emit(firstname, lastname, headline, country, addr, birthday, email_addr, link)
        self.cancel_pushButton_onClicked()

    @Slot()
    def cancel_pushButton_onClicked(self):
        self.hide()
