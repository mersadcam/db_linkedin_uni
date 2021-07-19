import sys
from ui_Mainwindow import Ui_Mainwindow
from PySide6.QtWidgets import QMainWindow, QApplication, QStackedWidget
from PySide6.QtCore import Signal, Slot
from PySide6 import QtGui
from login_com.login import Login
from login_com.signup import Signup
from profile_com.profile import Profile
from DB_pkg import db


class Mainwindow(QMainWindow):

    def __init__(self):
        super(Mainwindow, self).__init__()
        self.ui = Ui_Mainwindow()
        self.ui.setupUi(self)

        self.login = Login()
        self.signup = Signup()
        self.profile = Profile()

        # Setup DB:


        # Widget handler:
        self.login_widget = self.login.centralWidget()
        self.signup_widget = self.signup.centralWidget()
        self.profile_widget = self.profile.centralWidget()

        self.central_widget = QStackedWidget()
        self.central_widget.addWidget(self.login_widget)
        self.central_widget.addWidget(self.signup_widget)
        self.central_widget.addWidget(self.profile_widget)

        self.setCentralWidget(self.central_widget)
        self.central_widget.setCurrentWidget(self.login_widget)

        # Connections:
        self.login.on_login.connect(self.on_login)
        self.login.switch_to_signup.connect(self.login_to_signup)
        self.signup.switch_to_login.connect(self.signup_to_login)
        self.signup.on_signup.connect(self.on_signup)

    # Public slots:
    @Slot(str, str)
    def on_login(self, email: str, password: str):
        print("Login:")
        print(f"Email: {email}\nPassword: {password}")

    @Slot(str, str, str, str)
    def on_signup(self, firstname, lastname, email, password):
        print("Signup\n")
        print(f"Firstname:{firstname}\nLastname: {lastname}\nEmail: {email}\nPassword: {password}")

    @Slot()
    def login_to_signup(self):
        self.central_widget.setCurrentWidget(self.signup_widget)

    @Slot()
    def signup_to_login(self):
        self.central_widget.setCurrentWidget(self.login_widget)


if __name__ == "__main__":
    app = QApplication([])
    window = Mainwindow()
    window.show()
    sys.exit(app.exec())
