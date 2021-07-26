from ui_commentPostView import Ui_commentPostView
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QDialog, QLayout, QWidget, QVBoxLayout
from PySide6.QtGui import Qt
from post_com.postWidget import PostWidget
from post_com.viewCommentWidget import ViewCommentWidget
from constants import TableColumns


class CommentPostView(QDialog):
    def __init__(self, content, comments, content_is_post, is_liked, firstname, lastname):
        super(CommentPostView, self).__init__()
        self.ui = Ui_commentPostView()
        self.ui.setupUi(self)

        self.content = content
        self.comments = comments

        if content_is_post:
            main_content_widget = PostWidget(content[TableColumns.POST_CONTENT_ID],
                                             content[TableColumns.POST_CONTENT],
                                             content[TableColumns.CONTENT_LIKES_NUMBER],
                                             content[TableColumns.CONTENT_COMMENTS_NUMBER],
                                             firstname, lastname)
        else:
            main_content_widget = ViewCommentWidget(content[TableColumns.COMMENT_CONTENT_ID],
                                                    content[TableColumns.COMMENT_CONTENT],
                                                    content[TableColumns.CONTENT_LIKES_NUMBER],
                                                    content[TableColumns.CONTENT_COMMENTS_NUMBER],
                                                    firstname, lastname)

        main_content_widget.ui.showComment_pushButton.setVisible(False)

        main_content_layout = QLayout()
        main_content_layout.addWidget(content)
        self.ui.mainContent_widget.setLayout(main_content_layout)

        v_widget = QWidget()
        v_layout = QVBoxLayout()
        v_layout.setAlignment(Qt.AlignTop)

        for comment in self.comments:
            # need to have firstname and lastname in this method.
            commentWidget = ViewCommentWidget()
            v_layout.addWidget(comment)

        v_widget.setLayout(v_layout)
        self.ui.scrollArea.setWidget(v_widget)
