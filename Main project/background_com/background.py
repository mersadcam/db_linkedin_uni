from ui_background import Ui_background
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from skill_com.editSkills import EditSkills
from consts import debug
from background_com.backgroundWidget import BackgroundWidget


class Background(QMainWindow):
    switch_to_profile = Signal(str)

    def __init__(self, user_id, owner, firstname, lastname, backgrounds):
        super(Background, self).__init__()
        self.ui = Ui_background()
        self.ui.setupUi(self)

        self.ui.back_pushButton.clicked.connect(lambda: self.switch_to_profile(user_id))
        self.ui.edit_pushButton.setVisible(owner)

        v_widget = QWidget()
        v_layout = QVBoxLayout()
        v_layout.setAlignment(Qt.AlignTop)

        for background in backgrounds:
            background_widget = BackgroundWidget()
            label.setCursor(Qt.PointingHandCursor)
            label.setFont(font)
            label.setText(skill[0])
            label.setStyleSheet(label_style_sheet)
            label.setMinimumHeight(60)
            label.setObjectName(skill[1])
            v_layout.addWidget(label)

        v_widget.setLayout(v_layout)
        self.ui.scrollArea.setWidget(v_widget)
