from ui_backgroundWidget import Ui_backgroundWidget
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout


class BackgroundWidget(QWidget):
    def __init__(self, title, comp_name, description, start_time, end_time):
        super(BackgroundWidget, self).__init__()
        self.ui = Ui_backgroundWidget()
        self.ui.setupUi(self)

        self.ui.title_label.setText(title)
        self.ui.compName_label.setText(comp_name)
        self.ui.description_plainTextEdit.setPlainText(description)
        self.ui.startYear_label.setText(start_time)
        if end_time is not None:
            self.ui.endYear_label.setText(end_time)
        else:
            self.ui.endYear_label.setText('Now')
