import sys
from PySide2.QtWidgets import QApplication , QDialog
from ui_comment import Ui_comment



class comment(QDialog):
    def __init__(self):
        super(comment, self).__init__()
        self.ui = Ui_comment()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication([])
    window = comment()
    window.show()
    sys.exit(app.exec_())

