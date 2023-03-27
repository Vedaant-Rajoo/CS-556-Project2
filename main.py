import sys
from PyQt6.QtWidgets import *
from components.HomePage import HomePage
from components.LoginPage import LoginPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_page = LoginPage()
        self.setWindowTitle("Login")
        self.setFixedSize(400, 250)
        self.setCentralWidget(self.login_page)
        self.login_page.login_success.connect(self.show_home_page)

    def show_home_page(self, username):
        self.home_page = HomePage(username)
        self.setWindowTitle("Home")
        self.setFixedSize(400, 250)
        self.setCentralWidget(self.home_page)
    

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()