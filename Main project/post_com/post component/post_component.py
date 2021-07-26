import sys
from PySide2.QtWidgets import QApplication , QDialog
from ui_post_component import Ui_post_component


class post_component(QDialog):
    def __init__(self):
        super(post_component, self).__init__()
        self.ui = Ui_post_component()
        self.ui.setupUi(self)




if __name__ == "__main__":
    app = QApplication([])
    window = post_component()
    window.show()
    sys.exit(app.exec_())

