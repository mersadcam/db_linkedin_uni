from background_com.ui_addBackground import Ui_addBackgroundDialog
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtWidgets import QApplication, QDialog, QWidget, QVBoxLayout, QLabel, QHBoxLayout


class AddBackground(QDialog):
    add_new_background = Signal(str, str, str, str, str)

    #               (title, env, start, end, description)

    def __init__(self, all_env):
        super(AddBackground, self).__init__()
        self.ui = Ui_addBackgroundDialog()
        self.ui.setupUi(self)

        self.all_env = all_env

        self.ui.save_pushButton.clicked.connect(self.save_pushButton_clicked)
        self.ui.cancel_pushButton.clicked.connect(self.cancel_pushButton_onClicked)

        env_list = []

        for env in all_env:
            env_list.append(env[0])

        items = []
        for i in range(1900, 2021):
            items.append(str(i))
        items.append('Now')

        self.ui.startTime_comboBox.addItems(items)
        self.ui.endTime_comboBox.addItems(items)
        self.ui.env_comboBox.addItems(env_list)

    def save_pushButton_clicked(self):
        title = self.ui.title_lineEdit.text()
        env = self.ui.env_comboBox.currentText()
        env = self.find_env_id_by_name(env)
        start_time = self.ui.startTime_comboBox.currentText()
        end_time = self.ui.endTime_comboBox.currentText()
        description = self.ui.description_plainTextEdit.toPlainText()
        self.add_new_background.emit(title, env, start_time, end_time, description)
        self.cancel_pushButton_onClicked()

    def find_env_id_by_name(self, env_name):
        for env in self.all_env:
            if env[0] == env_name:
                return env[1]

    def cancel_pushButton_onClicked(self):
        self.close()
