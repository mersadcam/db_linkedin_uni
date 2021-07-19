from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Slot
import datetime
from profile_com.editInfo import Country
from profile_com.ui_contactInfo import Ui_contactInfoDialog


class ContactInfo(QDialog):
    def __init__(self):
        super(ContactInfo, self).__init__()
        self.ui = Ui_contactInfoDialog()
        self.ui.setupUi(self)

        self.ui.close_pushButton.clicked.connect(self.close_pushButton_onClicked)

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
    def close_pushButton_onClicked(self):
        self.hide()
