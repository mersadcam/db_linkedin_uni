from ui_backgroundWidget import Ui_backgroundWidget
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from editBackground import EditBackground


class BackgroundWidget(QWidget):
    remove_background = Signal(str)
    edit_background = Signal(str, str, str, str, str)

    def __init__(self, title, env, description, start_time, end_time, all_env, is_owner):
        super(BackgroundWidget, self).__init__()
        self.ui = Ui_backgroundWidget()
        self.ui.setupUi(self)

        self.env = env
        self.ui.title_label.setText(title)
        self.ui.compName_label.setText('env name')
        self.ui.description_plainTextEdit.setPlainText(description)
        self.ui.startYear_label.setText(start_time)
        if end_time is not None:
            self.ui.endYear_label.setText(end_time)
        else:
            self.ui.endYear_label.setText('Now')

        self.ui.edit_pushButton.setVisible(is_owner)
        self.ui.remove_pushButton.setVisible(is_owner)

        self.ui.remove_pushButton.clicked.connect(self.remove_pushButton)

    def remove_pushButton_onClicked(self):
        self.remove_background.emit(self.env['id'])

    def edit_pushButton_onClicked(self):
        self.edit_background.emit(self.ui.title_label.text(), self.env,
                                  self.ui.startYear_label.text(), self.ui.endYear_label.text(),
                                  self.ui.description_plainTextEdit.toPlainText())
