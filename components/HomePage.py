from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from scripts.connect import isDBA
from components.LogPage import LogsPage
def load_stylesheet():
    with open('styles/homeStyles.qss', 'r') as f:
        return f.read()
class HomePage(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle('Home Page')
        layout = QVBoxLayout()
        welcome_label = QLabel(f'Welcome, {username}!')
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(welcome_label)
        if isDBA(username):
            adminLabel = QLabel('You are an admin!')
            adminLabel.setStyleSheet('color: red')
            adminLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(adminLabel)

        self.setLayout(layout)
        self.setStyleSheet(load_stylesheet())

