from post_comp.ui_newCommentDialog import Ui_newComment
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal, Slot


class NewComment(QDialog):
    new_comment = Signal(str, str)

    def __init__(self, content_id):
        super(NewComment, self).__init__()
        self.ui = Ui_newComment()
        self.ui.setupUi(self)
        self.content_id = content_id
        self.ui.save_pushButton.clicked.connect(self.save_pushButton_onClicked)

    def save_pushButton_onClicked(self):
        content = self.ui.content_plainTextEdit.toPlainText()
        self.new_comment.emit(self.content_id, content)
