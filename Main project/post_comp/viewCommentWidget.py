from ui_postWidget import Ui_postWidget
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget
from ui_viewCommentWidget import Ui_viewCommentWidget
from consts import Labels


class ViewCommentWidget(QWidget):
    comment_liked = Signal(str)
    view_comments = Signal(str)
    new_comment = Signal(str)

    def __init__(self, content_id, content, likes_number, comments_number, firstname, lastname):
        super(ViewCommentWidget, self).__init__()
        self.ui = Ui_viewCommentWidget()
        self.ui.setupUi(self)
        self.content_id = content_id
        self.ui.content_plainTextEdit.setPlainText(content)
        self.ui.likes_label.setText(str(likes_number) + ' ' + Labels.LIKE)
        self.ui.comments_label.setText(str(comments_number) + ' ' + Labels.COMMENT)
        self.ui.firstname_label.setText(firstname)
        self.ui.lastname_label.setText(lastname)

        self.ui.like_pushButton.clicked.connect(lambda: self.comment_liked.emit(self.content_id))
        self.ui.showComment_pushButton.clicked.connect(lambda: self.view_comments.emit(self.content_id))
        self.ui.comment_pushButton.clicked.connect(lambda: self.new_comment.emit(self.content_id))

    def set_content_liked(self, is_liked):
        pass
