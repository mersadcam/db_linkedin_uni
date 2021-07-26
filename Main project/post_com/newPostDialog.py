from post_com.ui_newPostDialog import Ui_newPost
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal, Slot


class NewPost(QDialog):
    new_post = Signal(str)

    def __init__(self, firstname, lastname):
        super(NewPost, self).__init__()
        self.ui = Ui_newPost()
        self.ui.setupUi(self)

        self.ui.firstname_label.setText(firstname)
        self.ui.lastname_label.setText(lastname)
        self.ui.post_pushButton.clicked.connect(self.post_pushButton_onClicked)

    def post_pushButton_onClicked(self, content):
        self.new_post.emit(content)
        self.close()
