from background_com.ui_editBackground import Ui_EditBackgroundDialog
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtWidgets import QApplication, QDialog, QWidget, QVBoxLayout, QLabel, QHBoxLayout

sample_env = [
    {'name': 'name', 'id': 'id'}
]


class EditBackground(QDialog):
    save_changes = Signal(str, str, str, str, str, str)

    #               (title, env, start, end, description)

    def __init__(self, bg_id, title, env, start, end, description, all_env):
        super(EditBackground, self).__init__()
        self.ui = Ui_EditBackgroundDialog()
        self.ui.setupUi(self)

        self.all_env = all_env
        self.bg_id = bg_id
        self.ui.save_pushButton.clicked.connect(self.save_pushButton_clicked)
        self.ui.cancel_pushButton.clicked.connect(self.cancel_pushButton_onClicked)
        self.ui.title_lineEdit.setText(title)

        env_list = []
        for env in all_env:
            env_list.append(env['name'])

        items = []
        for i in range(1900, 2021):
            items.append(str(i))
        items.append('Now')

        self.ui.startTime_comboBox.addItems(items)
        self.ui.endTime_comboBox.addItems(items)
        self.ui.env_comboBox.addItems(env_list)

        self.ui.env_comboBox.setCurrentText(env['name'])
        self.ui.startTime_comboBox.setCurrentText(start)
        self.ui.endTime_comboBox.setCurrentText(end)
        self.ui.description_plainTextEdit.setPlainText(description)

    def save_pushButton_clicked(self):
        title = self.ui.title_lineEdit.text()
        env = self.ui.env_comboBox.currentText()
        env = self.find_env_id_by_name(env)
        start_time = self.ui.startTime_comboBox.currentText()
        end_time = self.ui.endTime_comboBox.currentText()
        description = self.ui.description_plainTextEdit.toPlainText()
        self.save_changes.emit(self.bg_id, title, env, start_time, end_time, description)
        self.cancel_pushButton_onClicked()

    def find_env_id_by_name(self, env_name):
        for env in self.all_env:
            if env['name'] == env_name:
                return env['id']

    def cancel_pushButton_onClicked(self):
        self.close()
