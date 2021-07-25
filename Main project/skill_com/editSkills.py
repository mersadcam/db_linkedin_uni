from skill_com.ui_editSkills import Ui_EditSkillsDialog
from PySide6.QtWidgets import QMainWindow, QDialog, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtGui import Qt
from PySide6.QtCore import Signal, Slot

# skills_ex = [
#     ('Qt', '1231423')
# ]

button_style_sheet = \
    '''
    QPushButton{
    color:rgb(46, 52, 54);
    border:1px solid rgb(48, 162, 249);
    border-radius:5px;
    padding:5px;
    }

    QPushButton:hover
    {
        border:1px solid white;
        border-radius:5px;
        background:rgb(48, 162, 249);
        color:white;
    }
    '''


class EditSkills(QDialog):
    saved_changes = Signal(list, list)

    def __init__(self, firstname, lastname, skills, all_skills):
        super(EditSkills, self).__init__()
        self.ui = Ui_EditSkillsDialog()
        self.ui.setupUi(self)
        self.ui.firstname_label.setText(firstname)
        self.ui.lastname_label.setText(lastname)
        self.skills = skills
        self.all_skills = all_skills
        self.added_skills = []
        self.removed_skills = []

        self.update_skill_box()

        names = []
        for skill in all_skills:
            names.append(skill[0])

        self.ui.skills_comboBox.addItems(names)
        self.ui.add_pushButton.clicked.connect(self.add_new_skill)
        self.ui.save_pushButton.clicked.connect(self.save_pushButton_clicked)
        self.ui.cancel_pushButton.clicked.connect(self.cancel_pushButton_clicked)

    def get_id_by_name(self, name):
        for skill in self.all_skills:
            if skill[0] == name:
                return skill[1]

    def add_new_skill(self):
        skill_name = self.ui.skills_comboBox.currentText()
        skill_id = self.get_id_by_name(skill_name)
        if skill_id in self.removed_skills:
            self.removed_skills.remove(skill_id)
        elif (skill_name, skill_id) not in self.skills:
            self.added_skills.append(skill_id)
            self.skills.append((skill_name, skill_id))
        self.update_skill_box()

    def remove_skill(self):
        selected_skill = self.sender().objectName()
        if selected_skill in self.added_skills:
            self.added_skills.remove(selected_skill)
        elif selected_skill not in self.removed_skills:
            self.removed_skills.append(selected_skill)
        for skill in self.skills:
            if skill[1] == selected_skill:
                self.skills.remove(skill)
        self.update_skill_box()

    def update_skill_box(self):

        widget = QWidget()
        v_layout = QVBoxLayout()
        v_layout.setAlignment(Qt.AlignTop)

        counter = 0
        h_widget = QWidget()
        h_layout = QHBoxLayout()
        h_widget.setLayout(h_layout)

        for skill in self.skills:

            counter = counter + 1
            button = QPushButton()
            button.setText(skill[0])
            button.setStyleSheet(button_style_sheet)
            button.setCursor(Qt.PointingHandCursor)
            button.setObjectName(skill[1])
            button.clicked.connect(self.remove_skill)
            h_layout.addWidget(button)

            if counter % 3 == 0:
                v_layout.addWidget(h_widget)

                h_widget = QWidget()
                h_layout = QHBoxLayout()
                # h_layout.setStretch()
                h_widget.setLayout(h_layout)
        if counter % 3 != 0:
            v_layout.addWidget(h_widget)

        widget.setLayout(v_layout)
        self.ui.scrollArea.setWidget(widget)

    def save_pushButton_clicked(self):
        # emit removed list and add list
        self.saved_changes.emit(self.added_skills, self.removed_skills)
        self.added_skills = []
        self.removed_skills = []
        self.cancel_pushButton_clicked()

    def cancel_pushButton_clicked(self):
        self.close()
