from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from PySide6.QtCore import QObject, Signal, Slot
from ui_profile import Ui_Profile
from editInfo import EditInfo, Country
from contactInfo import ContactInfo
from editAbout import EditAbout_Dialog
import sys
import datetime

data = {
    "about-content": '''
    Full-Stack Developer
    Interested in Cyber-security and Network
    '''
}


class Profile(QMainWindow):
    editInfo = Signal(str, str, str, int, str, datetime.datetime, str, str)
    change_about = Signal(str)

    def __init__(self):
        super(Profile, self).__init__()
        self.ui = Ui_Profile()
        self.ui.setupUi(self)

        self.editInfo_dialog = EditInfo()
        self.contactInfo_dialog = ContactInfo()
        self.editAbout_dialog = EditAbout_Dialog()

        self.contact_info_email = None
        self.contact_info_addr = None
        self.contact_info_bd = None
        self.contact_info_link = None

        # Connections:
        self.ui.editInfo_pushButton.clicked.connect(self.editInfo_pushButton_onClicked)
        self.ui.contactInfo_pushButton.clicked.connect(self.contactInfo_pushButton_onClicked)
        self.ui.editAbout_pushButton.clicked.connect(self.editAbout_pushButton_onClicked)
        self.editInfo_dialog.edit_saved.connect(self.info_edited)
        self.editAbout_dialog.about_changed.connect(self.about_changed)

    # public method
    def set_contact_info(self, email, addr, birthday, link):
        self.contact_info_link = link
        self.contact_info_email = email
        self.contact_info_addr = addr
        self.contact_info_bd = birthday

    # Ui set Methods:
    def set_connection_numbers(self, connection_numbers):
        text = self.ui.connections_pushButton.text()
        self.ui.connections_pushButton.setText(f"{connection_numbers} {text}")

    def set_country(self, country):
        self.ui.country_label.setText(country)

    def set_name(self, first_name, last_name):
        self.ui.firstName_label.setText(first_name)
        self.ui.lastName_label.setText(last_name)

    def set_about_content(self, about_content):
        self.ui.aboutContent_label.setText(about_content)

    def set_headline_label(self, headline):
        self.ui.headline_label.setText(headline)

    # Public slots:
    @Slot(str, str, str, int, str, datetime.datetime, str, str)
    def info_edited(self, firstname, lastname, headline,
                    country, addr, birthday, email_addr, link):
        # This one should be connected to center class slot
        self.editInfo.emit(firstname, lastname, headline, country, addr,
                           birthday, addr, birthday, email_addr, link)
        # If data changed successfully, changes will be showed by center class

    @Slot(str)
    def about_changed(self, about):
        self.change_about.emit(about)

    # Private slots:
    @Slot()
    def editAbout_pushButton_onClicked(self):
        self.editAbout_dialog.fill_field(self.ui.firstName_label.text(),
                                         self.ui.lastName_label.text(),self.ui.aboutContent_label.text())
        self.editAbout_dialog.show()

    @Slot()
    def editInfo_pushButton_onClicked(self):
        ui = self.ui
        firstname = ui.firstName_label.text()
        lastname = ui.lastName_label.text()
        headline = ui.headline_label.text()
        country = Country.case(ui.country_label.text())
        self.editInfo_dialog.fill_fields(firstname, lastname, headline, country, self.contact_info_addr,
                                         self.contact_info_bd, self.contact_info_email, self.contact_info_link)

        self.editInfo_dialog.show()

    @Slot()
    def skills_pushButton_onClicked(self):
        pass

    @Slot()
    def background_pushButton_onClicked(self):
        pass

    @Slot()
    def accomp_pushButton_onClicked(self):
        pass

    @Slot()
    def contactInfo_pushButton_onClicked(self):
        ui = self.ui
        firstname = ui.firstName_label.text()
        lastname = ui.lastName_label.text()
        headline = ui.headline_label.text()
        country = Country.case(ui.country_label.text())

        self.contactInfo_dialog.fill_fields(firstname, lastname, headline, country, self.contact_info_addr,
                                            self.contact_info_bd, self.contact_info_email, self.contact_info_link)
        self.contactInfo_dialog.show()

    @Slot()
    def connections_pushButton_onClicked(self):
        pass


if __name__ == "__main__":
    app = QApplication([])
    window = Profile()
    window.show()
    sys.exit(app.exec())
