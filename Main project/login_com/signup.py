import sys
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QApplication, QMainWindow
from login_com.ui_signup import Ui_signup


class Signup(QMainWindow):
    on_signup = Signal(str, str, str, str)
    switch_to_login = Signal()

    def __init__(self):
        super(Signup, self).__init__()
        self.ui = Ui_signup()
        self.ui.setupUi(self)

        self.ui.signup_pushButton.clicked.connect(self.signup_pushButton_onClicked)
        self.ui.login_pushButton.clicked.connect(self.login_pushButton_onClicked)
        self.ui.msg_label.setVisible(False)
    @Slot()
    def signup_pushButton_onClicked(self):
        # print("signup")
        firstname = self.ui.firstname_lineEdit.text()
        lastname = self.ui.lastname_lineEdit.text()
        email = self.ui.email_lineEdit.text()
        password = self.ui.password_lineEdit.text()

        self.on_signup.emit(firstname, lastname, email, password)

    @Slot()
    def login_pushButton_onClicked(self):
        print('switch to login_com')
        self.switch_to_login.emit()

    def set_err_msg(self, msg):
        self.ui.msg_label.setText(msg)
        self.ui.msg_label.setVisible(True)

if __name__ == "__main__":
    app = QApplication([])
    window = Signup()
    window.show()
    sys.exit(app.exec())
