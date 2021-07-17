import sys
from PySide2.QtWidgets import QApplication , QDialog
from ui_post import Ui_post


class post(QDialog):
    def __init__(self):
        super(post, self).__init__()
        self.ui = Ui_post()
        self.ui.setupUi(self)
     



if __name__ == "__main__":
    app = QApplication([])
    window = post()
    window.show()
    sys.exit(app.exec_())

