from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from components.HomePage import HomePage
from components.LogPage import LogsPage
from components.LoginPage import LoginPage
from components.policyDb import PolicyDbPage
      
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menubar = self.menuBar()
        self.login_page = LoginPage(self)
        self.setCentralWidget(self.login_page)
        self.login_page.login_success.connect(self.show_home_page)
        
    def show_home_page(self, username):
        self.home_page = HomePage(self, username)
        self.home_page.show_login_page_signal.connect(self.show_login_page)
        self.home_page.show_policyDb_page_signal.connect(self.show_policyDb_page)
        self.home_page.show_logs_page_signal.connect(self.show_logs_page)

    def show_login_page(self):
        self.login_page = LoginPage(self)
        self.setCentralWidget(self.login_page)
        self.login_page.login_success.connect(self.show_home_page)
    
    def show_policyDb_page(self):
        self.policyDb_page = PolicyDbPage(self)
        self.policyDb_page.show_login_page_signal.connect(self.show_login_page)
        self.policyDb_page.show_logs_page_signal.connect(self.show_logs_page)

    def show_logs_page(self):
        self.logs_page = LogsPage(self)
        self.logs_page.show_login_page_signal.connect(self.show_login_page)
        self.logs_page.show_home_page_signal.connect(self.show_home_page)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()