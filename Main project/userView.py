from ui_userView import Ui_userView
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget


class UserView(QWidget):
    on_clicked = Signal(str)

    def __init__(self, user_id, firstname, lastname, headline):
        super(UserView, self).__init__()
        self.ui = Ui_userView()
        self.ui.setupUi(self)

        self.ui.firstname_label.setText(firstname)
        self.ui.lastname_label.setText(lastname)
        self.ui.headline_plainTextEdit.setPlainText(headline)
        self.user_id = user_id

        self.ui.userView_widget.mousePressEvent = self.userView_widget_mousePressed

    @Slot()
    def userView_widget_mousePressed(self, event):
        self.on_clicked.emit(self.user_id)
