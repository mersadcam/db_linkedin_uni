import sys
from ui_Mainwindow import Ui_Mainwindow
from PySide6.QtWidgets import QMainWindow, QApplication, QStackedWidget
from PySide6.QtCore import Signal, Slot
from PySide6 import QtGui
from login_com.login import Login
from login_com.signup import Signup
from skill_com.skills import Skills
from profile_com.profile import Profile
from db import DB
from consts import Messages, DB_NAME, debug, Columns
import datetime
import constants


class Mainwindow(QMainWindow):

    def __init__(self):
        super(Mainwindow, self).__init__()
        self.ui = Ui_Mainwindow()
        self.ui.setupUi(self)

        # Pages:
        self.login = Login()
        self.signup = Signup()
        self.profile = Profile()
        self.skills = Skills()

        # Attr:
        self.own_uuid = None
        self.own_user_data = None
        self.own_profile_data = None
        self.other_profile_data = None
        self.other_user_data = None

        # Setup DB:
        self.db = DB(DB_NAME)

        # Widget handler:
        self.login_widget = self.login.centralWidget()
        self.signup_widget = self.signup.centralWidget()
        self.profile_widget = self.profile.centralWidget()
        self.home_widget = self.centralWidget()
        self.skills_widget = self.centralWidget()

        self.central_widget = QStackedWidget()
        self.central_widget.addWidget(self.login_widget)
        self.central_widget.addWidget(self.signup_widget)
        self.central_widget.addWidget(self.profile_widget)
        self.central_widget.addWidget(self.home_widget)
        self.central_widget.addWidget(self.skills_widget)

        self.setCentralWidget(self.central_widget)
        self.central_widget.setCurrentWidget(self.login_widget)

        # Connections:
        self.login.on_login.connect(self.on_login)
        self.login.switch_to_signup.connect(self.switch_to_signup)
        self.signup.switch_to_login.connect(self.switch_to_login)
        self.signup.on_signup.connect(self.on_signup)
        self.profile.profile_back_to_home.connect(self.switch_to_home)
        self.ui.profile_widget.mousePressEvent = self.switch_to_own_profile
        self.profile.editInfo.connect(self.editUserProfile)
        self.profile.change_about.connect(self.editAbout)
        self.skills.switch_to_profile.connect(self.switch_to_profile)
        self.profile.switch_to_skills.connect(self.switch_to_skills)
        self.skills.skill_edited.connect(self.save_skill_changes)
        # self.ui.profile_widget.

    # Public slots:
    @Slot(str, str)
    def on_login(self, email: str, password: str):
        res = self.db.user.user_login(email, password)
        print(f'Res: {res}')
        if not res[0]:
            self.login.set_err_msg(Messages.ERR_INVALID_EMAIL_OR_PASSWORD)
            return

        token = res[1]
        debug(user_data=self.own_user_data, own_uuid=self.own_uuid, profile_data=self.own_profile_data)
        self.own_uuid = self.db.user.user_get_uuid_by_token(token)[1]
        self.own_user_data = self.db.user.user_select(self.own_uuid)
        self.own_profile_data = self.db.user.profile_select(self.own_uuid)
        self.switch_to_home()

    @Slot(str, str, str, str)
    def on_signup(self, firstname, lastname, email, password):
        res = self.db.user.user_signUp(firstname, lastname, email, password)
        if not res[0]:
            self.signup.set_err_msg(Messages.ERR_INVALID_EMAIL_OR_PASSWORD)
            return

        token = res[1]
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
        self.profile.setup(self.own_uuid, True)
        self.profile.set_connection_numbers(self.own_profile_data['profile_number_of_connections'])
        self.profile.set_name(self.own_profile_data[Columns.FIRSTNAME],
                              self.own_profile_data[Columns.LASTNAME])
        self.profile.set_headline_label(self.own_profile_data[Columns.HEADLINE])
        self.profile.set_about_content(self.own_profile_data[Columns.ABOUT])
        self.profile.set_contact_info(self.own_profile_data[Columns.EMAIL], self.own_profile_data[Columns.ADDR],
                                      self.own_profile_data[Columns.BIRTHDAY], self.own_profile_data[Columns.LINK])
        self.central_widget.setCurrentWidget(self.profile_widget)

    @Slot(str)
    def switch_to_profile(self, user_id):
        if user_id == self.own_uuid:
            self.switch_to_own_profile()
        else:
            self.profile.setup(user_id, False)
            self.other_profile_data = self.db.user.profile_select(user_id)
            self.other_user_data = self.db.user.user_select(user_id)
            self.profile.set_connection_numbers(self.other_profile_data['profile_number_of_connections'])
            self.profile.set_name(self.other_profile_data[Columns.FIRSTNAME], self.other_profile_data[Columns.LASTNAME])
            self.profile.set_headline_label(self.other_profile_data[Columns.HEADLINE])
            self.profile.set_about_content(self.other_profile_data[Columns.ABOUT])
            self.profile.set_contact_info(self.other_user_data[Columns.EMAIL], self.other_profile_data[Columns.ADDR],
                                          self.other_profile_data[Columns.BIRTHDAY],
                                          self.other_profile_data[Columns.LINK])
            self.central_widget.setCurrentWidget(self.profile_widget)

    @Slot(str)
    def switch_to_skills(self, user_id):
        all_skills = self.db.user.skill_get_all_skills()
        user_skills = self.db.user.skill_get_all_user_skills(user_id)
        self.skills.setup(user_id, self.own_uuid == user_id, self.other_profile_data[Columns.FIRSTNAME],
                          self.other_profile_data[Columns.LASTNAME], user_skills, all_skills)
        self.central_widget.setCurrentWidget(self.skills_widget)

    @Slot(str, list, list)
    def save_skill_changes(self, user_id, added_skills, removed_skills):
        self.db.user.skill_insert_user_skill(user_id, added_skills)
        self.db.user.skill_remove_user_skills(user_id, removed_skills)

    @Slot()
    def switch_to_home(self):
        debug(user_data=self.own_user_data, own_uuid=self.own_uuid, profile_data=self.own_profile_data)
        self.ui.firstname_label.setText(self.own_profile_data[Columns.FIRSTNAME])
        self.ui.lastname_label.setText(self.own_profile_data[Columns.LASTNAME])

        if self.own_profile_data[Columns.HEADLINE] is None:
            self.ui.headline_plainTextEdit.setPlainText(Messages.DEFAULT_HEAD_LINE)
        else:
            self.ui.headline_plainTextEdit.setPlainText(self.own_profile_data[Columns.HEADLINE])

        self.central_widget.setCurrentWidget(self.home_widget)

    @Slot(str, str, str, int, str, datetime.datetime, str, str)
    def editUserProfile(self, firstname, lastname, headline,
                        country, addr, birthday, email_addr, link):
        self.db.user.profile_update(user_uuid=self.own_uuid, profile_first_name=firstname, profile_last_name=lastname,
                                    profile_headline=headline, profile_country=country, profile_birthday=birthday,
                                    profile_address=addr, profile_about=None)
        if email_addr != self.own_user_data[Columns.EMAIL]:
            self.db.user.user_update(self.own_uuid, email_addr)

        self.own_profile_data[Columns.FIRSTNAME] = firstname
        self.own_profile_data[Columns.LASTNAME] = lastname
        self.own_profile_data[Columns.HEADLINE] = headline
        self.own_profile_data[Columns.COUNTRY] = country
        self.own_profile_data[Columns.BIRTHDAY] = birthday
        self.own_profile_data[Columns.ADDR] = addr
        self.own_user_data[Columns.EMAIL] = email_addr
        # self.own_user_data[Columns.LINK] = link

    @Slot(str)
    def editAbout(self, about: str):
        if about is not None:
            self.db.user.profile_update(self.own_uuid, profile_about=about)
            self.own_profile_data[Columns.ABOUT] = about


if __name__ == "__main__":
    app = QApplication([])
    window = Mainwindow()
    window.show()
    sys.exit(app.exec())
