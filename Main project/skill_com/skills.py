from ui_skills import Ui_Skills
from PySide6.QtGui import QFont
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from editSkills import EditSkills
import sys

# ('SKILL_NAME', 'SKILL_ID', SKILL_ENDORSEMENTS_NUMBER)
skills_ex = [('pyqt', '2231423'), ('Qt', '121423')]
all_skills_ex = [
    ('pyqt', '2231423'),
    ('Qt', '121423'),
    ('python', '12423'),
    ('C++', '12314'),
    ('Unity', '11423')
]
label_style_sheet = \
    '''
    QLabel{
    border-radius:5px;
    margin:3px;
    padding-left:10px;
    background:
    qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
     stop:0 rgba(0, 138, 243, 86),
      stop:1 rgba(255, 255, 255, 255));
    Text-align:left;
    }
    '''


class Skills(QMainWindow):
    switch_to_profile = Signal(str)
    skill_edited = Signal(list, list)

    def __init__(self, user_id=None, firstname=None, lastname=None, skills=None, all_skills=None):
        super(Skills, self).__init__()
        self.ui = Ui_Skills()
        self.ui.setupUi(self)
        self.editSkillsDialog = None
        self.firstname = firstname
        self.lastname = lastname
        self.skills = skills
        self.all_skills = all_skills
        self.user_id = user_id

        self.ui.edit_pushButton.clicked.connect(self.edit_pushButton_onClicked)
        self.ui.back_pushButton.clicked.connect(self.back_pushButton_onClicked)

    def setup(self, user_id, own_user, firstname, lastname, skills, all_skills):
        self.firstname = firstname
        self.lastname = lastname
        self.skills = skills
        self.all_skills = all_skills
        self.user_id = user_id
        self.ui.edit_pushButton.setVisible(own_user)

        self.update_skill_box()
        # widget = QWidget()
        # v_layout = QVBoxLayout()
        # v_layout.setAlignment(Qt.AlignTop)
        #
        # counter = 0
        # h_widget = QWidget()
        # h_layout = QHBoxLayout()
        # h_widget.setLayout(h_layout)
        #
        # for skill in skills:
        #
        #     counter = counter + 1
        #     button = QPushButton()
        #     button.setText(skill)
        #     button.setStyleSheet(button_style_sheet)
        #     button.setCursor(Qt.PointingHandCursor)
        #     h_layout.addWidget(button)
        #
        #     if counter % 3 == 0:
        #         v_layout.addWidget(h_widget)
        #
        #         h_widget = QWidget()
        #         h_layout = QHBoxLayout()
        #         # h_layout.setStretch()
        #         h_widget.setLayout(h_layout)
        #
        # widget.setLayout(v_layout)
        # self.ui.scrollArea.setWidget(widget)



        # QWidget * central = new
        # QWidget
        # QScrollArea * scroll = new
        # QScrollArea;
        # QVBoxLayout * layout = new
        # QVBoxLayout(central);
        # scroll->setWidget(central);
        # scroll->setWidgetResizable(true);

    def edit_pushButton_onClicked(self):
        self.editSkillsDialog = EditSkills(self.firstname, self.lastname, self.skills, self.all_skills)
        self.editSkillsDialog.saved_changes.connect(self.save_skill_edit)
        self.editSkillsDialog.show()

    def back_pushButton_onClicked(self):
        self.switch_to_profile.emit(self.user_id)

    def update_skill_box(self):
        v_widget = QWidget()
        v_layout = QVBoxLayout()
        v_layout.setAlignment(Qt.AlignTop)

        font = QFont()
        font.setPointSize(16)

        for skill in skills_ex:
            label = QLabel()
            label.setCursor(Qt.PointingHandCursor)
            label.setFont(font)
            label.setText(skill[0])
            label.setStyleSheet(label_style_sheet)
            label.setMinimumHeight(60)
            label.setObjectName(skill[1])
            v_layout.addWidget(label)

        v_widget.setLayout(v_layout)
        self.ui.scrollArea.setWidget(v_widget)

    @Slot(list, list)
    def save_skill_edit(self, added_list, removed_list):
        for skill in self.skills:
            if skill[1] in removed_list:
                del skill

        for skill in self.all_skills:
            if (skill[1] in added_list) and (skill not in self.skills):
                self.skills.append(skill)

        self.update_skill_box()
        self.skill_edited.emit(added_list, removed_list)

if __name__ == "__main__":
    app = QApplication([])
    window = Skills('mersad', 'khalafi', skills_ex, all_skills_ex)
    window.show()
    sys.exit(app.exec())
