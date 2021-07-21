import sys
from ui_Mainwindow import Ui_Mainwindow
from PySide6.QtWidgets import QMainWindow, QApplication, QStackedWidget
from PySide6.QtCore import Signal, Slot
from PySide6 import QtGui
from login_com.login import Login
from login_com.signup import Signup
from profile_com.profile import Profile
from db import DB
from consts import Messages, DB_NAME


class Mainwindow(QMainWindow):

    def __init__(self):
        super(Mainwindow, self).__init__()
        self.ui = Ui_Mainwindow()
        self.ui.setupUi(self)

        # Pages:
        self.login = Login()
        self.signup = Signup()
        self.profile = Profile()

        # Attr:
        self.token = None

        # Setup DB:
        self.db = DB(DB_NAME)

        # Widget handler:
        self.login_widget = self.login.centralWidget()
        self.signup_widget = self.signup.centralWidget()
        self.profile_widget = self.profile.centralWidget()
        self.home_widget = self.centralWidget()

        self.central_widget = QStackedWidget()
        self.central_widget.addWidget(self.login_widget)
        self.central_widget.addWidget(self.signup_widget)
        self.central_widget.addWidget(self.profile_widget)
        self.central_widget.addWidget(self.home_widget)

        self.setCentralWidget(self.central_widget)
        self.central_widget.setCurrentWidget(self.login_widget)

        # Connections:
        self.login.on_login.connect(self.on_login)
        self.login.switch_to_signup.connect(self.switch_to_signup)
        self.signup.switch_to_login.connect(self.switch_to_login)
        self.signup.on_signup.connect(self.on_signup)
        self.profile.profile_back_to_home.connect(self.switch_to_home)
        self.ui.profile_widget.mousePressEvent = self.switch_to_own_profile
        # self.ui.profile_widget.

    # Public slots:
    @Slot(str, str)
    def on_login(self, email: str, password: str):
        res = self.db.user.user_login(email, password)
        if not res[0]:
            self.login.set_err_msg(Messages.ERR_INVALID_EMAIL_OR_PASSWORD)
            return

        self.token = res[1]
        self.switch_to_home()

    @Slot(str, str, str, str)
    def on_signup(self, firstname, lastname, email, password):
        res = self.db.user.user_signUp(firstname, lastname, email, password)
        if not res[0]:
            self.login.set_err_msg(Messages.ERR_INVALID_EMAIL_OR_PASSWORD)
            return

        self.token = res[1]
        self.switch_to_home()

    @Slot()
    def switch_to_signup(self):
        self.central_widget.setCurrentWidget(self.signup_widget)

    @Slot()
    def switch_to_login(self):
        self.central_widget.setCurrentWidget(self.login_widget)

    @Slot()
    def switch_to_own_profile(self, event):
        print("Switch to profile")
        self.central_widget.setCurrentWidget(self.profile_widget)

    @Slot()
    def switch_to_home(self):
        self.central_widget.setCurrentWidget(self.home_widget)
        user_uuid = None
        connection_number = self.db.user.connection_numberOfConnections(user_uuid)
        profile_data = self.db.user.profile_select(user_uuid, '*')

        self.profile.set_connection_numbers(connection_number)
        # Select user by token.


if __name__ == "__main__":
    app = QApplication([])
    window = Mainwindow()
    window.show()
    sys.exit(app.exec())
