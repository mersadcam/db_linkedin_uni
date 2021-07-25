from post_comp.ui_postWidget import Ui_postWidget
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget
from consts import Labels


class PostWidget(QWidget):
    post_liked = Signal(str)
    view_comments = Signal(str)
    new_comment = Signal(str)

    def __init__(self, post_id, content, likes_number, comments_number, firstname, lastname):
        super(PostWidget, self).__init__()

        self.ui = Ui_postWidget()
        self.ui.setupUi(self)
        self.post_id = post_id

        self.ui.like_pushButton.clicked.connect(lambda: self.post_liked.emit(self.post_id))
        self.ui.showComment_pushButton.clicked.connect(lambda: self.view_comments.emit(self.post_id))
        self.ui.comment_pushButton.clicked.connect(lambda: self.new_comment.emit(self.post_id))

        self.ui.likes_label.setText(str(likes_number) + ' ' + Labels.LIKE)
        self.ui.comments_label.setText(str(comments_number) + ' ' + Labels.COMMENT)
        self.ui.content_plainTextEdit.setPlainText(content)
        self.ui.firstname_label.setText(firstname)
        self.ui.lastname_label.setText(lastname)

    def set_post_liked(self, is_liked):
        pass
