from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class HomePage(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle('Home Page')
        layout = QVBoxLayout()
        welcome_label = QLabel(f'Welcome, {username}!')
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(welcome_label)
        self.setLayout(layout)

