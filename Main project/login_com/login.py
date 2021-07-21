from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QApplication, QMainWindow
from login_com.ui_login import Ui_login
import sys


class Login(QMainWindow):
    on_login = Signal(str, str)
    switch_to_signup = Signal()

    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)

        self.ui.login_pushButton.clicked.connect(self.login_pushButton_onClicked)
        self.ui.signup_pushButton.clicked.connect(self.signup_pushButton_onClicked)
        self.ui.msg_label.setVisible(False)

    # Private slots:
    def login_pushButton_onClicked(self):
        email = self.ui.email_lineEdit.text()
        password = self.ui.password_lineEdit.text()
        self.on_login.emit(email, password)

    def signup_pushButton_onClicked(self):
        self.switch_to_signup.emit()

    def set_err_msg(self, msg):
        self.ui.msg_label.setVisible(True)
        self.ui.msg_label.setText(msg)

if __name__ == "__main__":
    app = QApplication([])
    window = Login()
    window.show()
    sys.exit(app.exec())
