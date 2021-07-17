import sys
from PySide2.QtWidgets import QApplication , QDialog
from ui_signup import Ui_signup


class signup(QDialog):
    def __init__(self):
        super(signup, self).__init__()
        self.ui = Ui_signup()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication([])
    window = signup()
    window.show()
    sys.exit(app.exec_())

