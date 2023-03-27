import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from components.HomePage import HomePage
from components.LogPage import LogsPage
from components.LoginPage import LoginPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_page = LoginPage()
        self.menubar = self.menuBar()
        # self.menubar.setNativeMenuBar(False)
        self.setWindowTitle("Login")
        self.setFixedSize(500, 500)
        self.setCentralWidget(self.login_page)
        self.login_page.login_success.connect(self.show_home_page)

    def show_home_page(self, username):
        self.username = username
        self.home_page = HomePage(username)
        self.logs = QAction('Logs', self)
        self.logs.triggered.connect(self.show_logs_page)
        # Ctrl on Mac is Command
        self.logs.setShortcut('Ctrl+L')
        self.logoutAction = QAction('Logout', self)
        self.logoutAction.triggered.connect(self.show_login_page)
        self.logoutAction.setShortcut('Ctrl+O')
        self.actionsMenu = self.menubar.addMenu('&Actions')
        self.actionsMenu.addAction(self.logs)
        self.actionsMenu.addAction(self.logoutAction)
        self.setWindowTitle("Home")
        self.setCentralWidget(self.home_page)
    
    def show_logs_page(self):
        self.logs_page = LogsPage()
        self.setWindowTitle("Logs")
        self.setCentralWidget(self.logs_page)
    
    def show_login_page(self):
        self.username = None
        self.actionsMenu.clear()
        self.login_page = LoginPage()
        self.setWindowTitle("Login")
        self.setCentralWidget(self.login_page)
        self.login_page.login_success.connect(self.show_home_page)
        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()