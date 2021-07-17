import sys
from PySide2.QtWidgets import QApplication , QDialog
from ui_login import Ui_login


class login(QDialog):
    def __init__(self):
        super(login, self).__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication([])
    window = login()
    window.show()
    sys.exit(app.exec_())

