from background_com.ui_background import Ui_background
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from background_com.editBackground import EditBackground
from background_com.addBackground import AddBackground
from consts import debug
from constants import TableColumns
from background_com.backgroundWidget import BackgroundWidget

style_sheet = '''
QWidget#backgroundWidget{
border:2px solid rgb(48, 162, 249);
border-radius:10px;
background:rgba(248, 253, 255, 206);
color:rgb(1, 31, 54);
}
'''


class Background(QMainWindow):
    switch_to_profile = Signal(str)
    save_background_change = Signal(str, str, str, str, str, str)
    remove_background = Signal(str)
    new_background = Signal(str, str, str, str, str)

    def __init__(self):
        super(Background, self).__init__()
        self.ui = Ui_background()
        self.ui.setupUi(self)
        self.all_env = None
        self.is_owner = None
        self.all_backgrounds = None
        self.ui.add_pushButton.clicked.connect(self.add_pushButton_onClicked)
        self.add_background_dialog = None
        self.edit_background_dialog = None

    def setup(self, user_id, is_owner, backgrounds, all_env):
        self.all_env = all_env
        self.is_owner = is_owner
        self.ui.add_pushButton.setVisible(self.is_owner)
        self.all_backgrounds = backgrounds
        self.update_scroll_area()
        self.ui.back_pushButton.clicked.connect(lambda: self.switch_to_profile.emit(user_id))

    def update_scroll_area(self):
        v_widget = QWidget()
        v_layout = QVBoxLayout()
        v_layout.setAlignment(Qt.AlignTop)

        for background in self.all_backgrounds:
            background_widget = BackgroundWidget(background[TableColumns.BACKGROUND_BG_ID],
                                                 background[TableColumns.BACKGROUND_TITLE],
                                                 background[TableColumns.BACKGROUND_ENV],
                                                 background[TableColumns.BACKGROUND_DESCRIPTION],
                                                 background[TableColumns.BACKGROUND_START_DATE],
                                                 background[TableColumns.BACKGROUND_END_DATE],
                                                 self.is_owner)
            background_widget.setStyleSheet(style_sheet)
            v_layout.addWidget(background_widget)
            background_widget.edit_background.connect(self.open_edit_background)
            background_widget.remove_background.connect(self.on_removed_background)

        v_widget.setLayout(v_layout)
        self.ui.scrollArea.setWidget(v_widget)

    def add_pushButton_onClicked(self):
        self.add_background_dialog = AddBackground(self.all_env)
        self.add_background_dialog.add_new_background.connect(self.on_add_background)
        self.add_background_dialog.show()

    @Slot(str, str, str, str, str)
    def on_add_background(self, title, env, start, end, description):
        self.new_background.emit(title, env, start, end, description)

    def update_base_on_changes(self, backgrounds):
        self.all_backgrounds = backgrounds
        self.update_scroll_area()

    @Slot(str, str, dict, str, str, str)
    def open_edit_background(self, bg_id, title, env, description, start_time, end_time):
        print(f'Env: {env}')
        self.edit_background_dialog = EditBackground(bg_id, title, env, description, start_time, end_time, self.all_env)
        self.edit_background_dialog.save_changes.connect(self.on_saved_changes)
        self.edit_background_dialog.show()

    @Slot(str, str, str, str, str, str)
    def on_saved_changes(self, bg_id, title, env, start_time, end_time, description):
        self.save_background_change.emit(bg_id, title, env, start_time, end_time, description)

    @Slot(str)
    def on_removed_background(self, bg_id):
        self.remove_background.emit(bg_id)
