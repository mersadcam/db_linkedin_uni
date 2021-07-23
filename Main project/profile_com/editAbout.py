from profile_com.ui_editAbout import Ui_EditAboutDialog
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal, Slot


class EditAbout_Dialog(QDialog):
    about_changed = Signal(str)

    def __init__(self):
        super(EditAbout_Dialog, self).__init__()
        self.ui = Ui_EditAboutDialog()
        self.ui.setupUi(self)

        self.ui.save_pushButton.clicked.connect(self.save_pushButton_onClicked)
        self.ui.cancel_pushButton.clicked.connect(self.cancel_pushButton_onClicked)

    def fill_field(self, firstname, lastname, about):
        self.ui.firstname_label.setText(firstname)
        self.ui.lastname_label.setText(lastname)
        self.ui.about_plainTextEdit.setPlainText(about)

    @Slot()
    def cancel_pushButton_onClicked(self):
        self.hide()

    @Slot()
    def save_pushButton_onClicked(self):
        about = self.ui.about_plainTextEdit.toPlainText()
        if about.replace(' ', '') != "":
            self.about_changed.emit(about)

        self.cancel_pushButton_onClicked()

