from background_com.ui_backgroundWidget import Ui_backgroundWidget
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from constants import TableColumns



class BackgroundWidget(QWidget):
    remove_background = Signal(str)
    edit_background = Signal(str, str, dict, str, str, str)

    def __init__(self, bg_id, title, env, description, start_time, end_time, is_owner):
        super(BackgroundWidget, self).__init__()
        self.ui = Ui_backgroundWidget()
        self.ui.setupUi(self)
        self.env = env
        self.id = bg_id
        self.ui.title_label.setText(title)
        self.ui.compName_label.setText(env[TableColumns.ENV_ENV_NAME])
        self.ui.description_plainTextEdit.setPlainText(description)
        self.ui.startYear_label.setText(start_time)
        print(f'start time: {start_time}')
        if end_time is not None:
            self.ui.endYear_label.setText(end_time)
        else:
            self.ui.endYear_label.setText('Now')

        self.ui.edit_pushButton.setVisible(is_owner)
        self.ui.remove_pushButton.setVisible(is_owner)

        self.ui.remove_pushButton.clicked.connect(self.remove_pushButton_onClicked)
        self.ui.edit_pushButton.clicked.connect(self.edit_pushButton_onClicked)

    def remove_pushButton_onClicked(self):
        self.remove_background.emit(self.id)

    def edit_pushButton_onClicked(self):
        print(f'self.env: {self.env}\ttype:{type(self.env)}')
        self.edit_background.emit(self.id, self.ui.title_label.text(), self.env,
                                  self.ui.startYear_label.text(), self.ui.endYear_label.text(),
                                  self.ui.description_plainTextEdit.toPlainText())
