from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from components.HomePage import HomePage
from scripts.login import login

def load_stylesheet():
    with open("styles/styles.qss", "r") as stylesheet:
        return stylesheet.read()

class LoginPage(QWidget):
    login_success = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        

        # create the widgets
        self.username_label = QLabel("Username:", self)
        self.username_label.move(50, 50)
        self.username_edit = QLineEdit(self)
        self.username_edit.move(150, 50)

        self.password_label = QLabel("Password:", self)
        self.password_label.move(50, 100)
        self.password_edit = QLineEdit(self)
        self.password_edit.move(150, 100)
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login", self)
        self.login_button.move(150, 150)
        self.login_button.clicked.connect(self.login)

        # create a grid layout for the widgets
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.username_label, 0, 0)
        grid_layout.addWidget(self.username_edit, 0, 1)
        grid_layout.addWidget(self.password_label, 1, 0)
        grid_layout.addWidget(self.password_edit, 1, 1)
        grid_layout.addWidget(self.login_button, 2, 1)

        # set the layout for the window
        self.setLayout(grid_layout)
        self.setStyleSheet(load_stylesheet())

    

    def login(self):
        # implement your login logic here
        username = self.username_edit.text()
        password = self.password_edit.text()
        if login(username, password):
            self.login_success.emit(username)
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password")
        