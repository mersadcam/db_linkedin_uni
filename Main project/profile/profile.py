from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from ui_profile import Ui_Profile
from about import About
import sys

data = {
    "about-content": '''
    Full-Stack Developer
    Interested in Cyber-security and Network
    '''
}


class Profile(QMainWindow):
    def __init__(self):
        super(Profile, self).__init__()
        self.ui = Ui_Profile()
        self.ui.setupUi(self)



        # self.ui.scrollArea.setWidget(fortest)

        # x = fortest.verticalLayout


if __name__ == "__main__":
    app = QApplication([])
    window = Profile()
    window.show()
    sys.exit(app.exec())
