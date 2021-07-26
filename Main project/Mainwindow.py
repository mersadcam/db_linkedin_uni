import sys
from ui_Mainwindow import Ui_Mainwindow
from PySide6.QtWidgets import QMainWindow, QApplication, QStackedWidget, QWidget, QVBoxLayout
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import Qt
from PySide6 import QtGui
from login_com.login import Login
from login_com.signup import Signup
from skill_com.skills import Skills
from post_com.postWidget import PostWidget
from post_com.newCommentDialog import NewComment
from post_com.newPostDialog import NewPost
from post_com.commentPostView import CommentPostView
from profile_com.profile import Profile
from userView import UserView
from db import DB
from consts import Messages, DB_NAME, debug, Columns
import datetime
from constants import TableColumns
from background_com.background import Background


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
        self.background = Background()

        # Attr:
        self.own_uuid = None
        self.own_user_data = None
        self.own_profile_data = None
        self.other_profile_data = None
        self.other_user_data = None
        self.new_comment = None
        self.new_post = None
        self.comment_post_view = None

        # Setup DB:
        self.db = DB(DB_NAME)

        # Widget handler:
        self.login_widget = self.login.centralWidget()
        self.signup_widget = self.signup.centralWidget()
        self.profile_widget = self.profile.centralWidget()
        self.home_widget = self.centralWidget()
        self.skills_widget = self.skills.centralWidget()
        self.bg_widget = self.background.centralWidget()

        self.central_widget = QStackedWidget()
        self.central_widget.addWidget(self.login_widget)
        self.central_widget.addWidget(self.signup_widget)
        self.central_widget.addWidget(self.profile_widget)
        self.central_widget.addWidget(self.home_widget)
        self.central_widget.addWidget(self.skills_widget)
        self.central_widget.addWidget(self.bg_widget)

        self.setCentralWidget(self.central_widget)
        self.central_widget.setCurrentWidget(self.login_widget)

        # Connections:
        self.ui.newPost_pushButton.clicked.connect(self.newPost_pushButton_onClicked)
        self.login.on_login.connect(self.on_login)
        self.login.switch_to_signup.connect(self.switch_to_signup)
        self.signup.switch_to_login.connect(self.switch_to_login)
        self.signup.on_signup.connect(self.on_signup)
        self.profile.switch_to_home.connect(self.switch_to_home)
        self.ui.profile_widget.mousePressEvent = self.switch_to_own_profile
        self.profile.editInfo.connect(self.editUserProfile)
        self.profile.change_about.connect(self.editAbout)
        self.skills.switch_to_profile.connect(self.switch_to_profile)
        self.profile.switch_to_bg.connect(self.switch_to_bg)
        self.profile.switch_to_skills.connect(self.switch_to_skills)
        self.profile.connect_to.connect(self.connect_users)
        self.skills.skill_edited.connect(self.save_skill_changes)
        self.background.remove_background.connect(self.remove_background)
        self.background.new_background.connect(self.new_background)
        self.background.save_background_change.connect(self.edit_background)
        self.background.switch_to_profile.connect(self.switch_to_profile)
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


        self.update_network_area()
        self.update_post_area()
        self.switch_to_home()

    def update_network_area(self):

        network_users = self.db.user.connection_get_user_network_info(self.own_uuid)

        v_widget = QWidget()
        v_layout = QVBoxLayout()
        v_layout.setAlignment(Qt.AlignTop)

        for user in network_users:
            user_view_widget = UserView(user[TableColumns.PROFILE_USER_UUID],
                                        user[TableColumns.PROFILE_FIRST_NAME],
                                        user[TableColumns.PROFILE_LAST_NAME],
                                        user[TableColumns.PROFILE_HEADLINE])
            v_layout.addWidget(user_view_widget)

        v_widget.setLayout(v_layout)
        self.ui.userNetwork_scrollArea.setWidget(v_widget)


    @Slot(str, str, str, str)
    def on_signup(self, firstname, lastname, email, password):
        res = self.db.user.user_signUp(firstname, lastname, email, password)
        if not res[0]:
            self.signup.set_err_msg(Messages.ERR_INVALID_EMAIL_OR_PASSWORD)
            return

        token = res[1]
        self.own_uuid = self.db.user.user_get_uuid_by_token(token)[1]
        self.own_user_data = self.db.user.user_select(self.own_uuid)
        self.own_profile_data = self.db.user.profile_select(self.own_uuid)
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
        number_of_conn = self.db.user.connection_numberOfConnections(self.own_uuid)
        self.profile.set_connection_numbers(number_of_conn)
        self.profile.set_name(self.own_profile_data[Columns.FIRSTNAME],
                              self.own_profile_data[Columns.LASTNAME])
        self.profile.set_headline_label(self.own_profile_data[Columns.HEADLINE])
        self.profile.set_about_content(self.own_profile_data[Columns.ABOUT])
        self.profile.set_contact_info(self.own_user_data[Columns.EMAIL], self.own_profile_data[Columns.ADDR],
                                      self.own_profile_data[Columns.BIRTHDAY], self.own_profile_data[Columns.LINK])
        self.central_widget.setCurrentWidget(self.profile_widget)

    @Slot(str)
    def switch_to_profile(self, user_id):
        if user_id == self.own_uuid:
            self.switch_to_own_profile(None)
        else:
            self.profile.setup(user_id, False)
            self.other_profile_data = self.db.user.profile_szelect(user_id)
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
        debug(all_skills=all_skills, user_skills=user_skills)
        if self.own_uuid == user_id:
            profile_data = self.own_profile_data
        else:
            profile_data = self.other_profile_data

        self.skills.setup(user_id, self.own_uuid == user_id, profile_data[Columns.FIRSTNAME],
                          profile_data[Columns.LASTNAME], user_skills, all_skills)
        self.central_widget.setCurrentWidget(self.skills_widget)

    @Slot(str, list, list)
    def save_skill_changes(self, user_id, added_skills, removed_skills):
        res_insert = self.db.user.skill_insert_user_skill(user_id, added_skills)
        res_delete = self.db.user.skill_remove_user_skills(user_id, removed_skills)
        debug(res_insert=res_insert, added_skills=added_skills, removed_skills=removed_skills, res_delete=res_delete)

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
        self.own_profile_data = self.db.user.profile_select(self.own_uuid)
        self.own_user_data = self.db.user.user_select(self.own_uuid)
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

    @Slot(str)
    def connect_users(self, other_id):
        self.db.user.connection_add(self.own_uuid, other_id)

    @Slot(str)
    def new_comment(self, content_id):
        self.new_comment = NewComment(content_id)
        self.new_comment.new_comment.connect(self.save_new_comment)
        self.new_comment.show()

    @Slot(str, str)
    def save_new_comment(self, content_id, content):
        self.db.content.comment_add(content, content_id, self.own_uuid)

    def newPost_pushButton_onClicked(self):
        self.new_post = NewPost(self.own_profile_data[TableColumns.PROFILE_FIRST_NAME],
                                self.own_profile_data[TableColumns.PROFILE_LAST_NAME])
        self.new_post.new_post.connect(self.save_new_post)
        self.new_post.show()

    @Slot(str)
    def save_new_post(self, content):
        self.db.content.post_add(content, self.own_uuid)

    def update_post_area(self):
        posts = self.db.content.post_select_userPosts(self.own_uuid)

        v_widget = QWidget()
        v_layout = QVBoxLayout()
        v_layout.setAlignment(Qt.AlignTop)

        for post in posts:
            post = PostWidget(post[TableColumns.CONTENT_ID], post[TableColumns.POST_CONTENT],
                              post[TableColumns.CONTENT_NUMBER_OF_LIKES],
                              post[TableColumns.CONTENT_NUMBER_OF_COMMENTS],
                              post[TableColumns.CONTENT_OWNER][TableColumns.CONTENT_OWNER_FNAME],
                              post[TableColumns.CONTENT_OWNER][TableColumns.CONTENT_OWNER_LNAME])
            # need firstname and lastname in this constructor
            post.post_liked.connect(self.like_post)
            post.new_comment.connect(self.new_comment)
            post.view_comments.connect(self.view_comments)
            v_layout.addWidget(post)

        v_widget.setLayout(v_layout)
        self.ui.post_scrollArea.setWidget(v_widget)

    @Slot(str)
    def like_post(self, content_id):
        self.db.content.like_insert(content_id, self.own_uuid)

    @Slot(str)
    def view_comments(self, content_id):
        # content, comments, content_is_post, is_liked, firstname, lastname
        content = {}
        comments = self.db.content.content_select_content_comments(content_id)
        user_uuid = self.db.content.content_get_user_uuid_by_content(content_id)
        profile = self.db.user.profile_select(user_uuid)
        content_is_post = True
        is_liked = True

        self.comment_post_view = CommentPostView(content, comments,
                                                 content_is_post, is_liked,
                                                 profile[TableColumns.PROFILE_FIRST_NAME],
                                                 profile[TableColumns.PROFILE_LAST_NAME])
        self.show()

    @Slot(str)
    def switch_to_bg(self, user_id):
        bgs = self.db.user.background_get_all(user_id)
        all_envs = self.db.user.env_get_all_envs()
        self.background.setup(user_id, user_id == self.own_uuid, bgs, all_envs)
        self.central_widget.setCurrentWidget(self.bg_widget)

    @Slot(str)
    def remove_background(self, bg_id):
        self.db.user.background_delete(bg_id)
        bgs = self.db.user.background_get_all(self.own_uuid)
        self.background.update_base_on_changes(bgs)

    @Slot(str, str, str, str, str)
    def new_background(self, title, env, start, end, description):
        self.db.user.background_insert(self.own_uuid, env, start, end, description, title)
        bgs = self.db.user.background_get_all(self.own_uuid)
        self.background.update_base_on_changes(bgs)

    @Slot(str, str, str, str, str, str)
    def edit_background(self, bg_id, title, env_id, start_time, end_time, description):
        res = self.db.user.background_update(bg_id, env_id, start_time, end_time, description, title)
        print(f'Result: {res}')
        bgs = self.db.user.background_get_all(self.own_uuid)
        self.background.update_base_on_changes(bgs)


if __name__ == "__main__":
    app = QApplication([])
    window = Mainwindow()
    window.show()
    sys.exit(app.exec())
