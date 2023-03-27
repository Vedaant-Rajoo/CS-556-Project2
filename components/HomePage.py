from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from scripts.connect import *

def load_stylesheet():
    with open('styles/homeStyles.qss', 'r') as f:
        return f.read()
class HomePage(QWidget):
    show_login_page_signal = pyqtSignal()
    show_logs_page_signal = pyqtSignal()
    show_policyDb_page_signal = pyqtSignal()
    def __init__(self,window,username):
        super().__init__()
        self.window = window
        self.username = username
        self.logs = QAction(QIcon("images/logs.png"),'Logs', self)
        self.logs.triggered.connect(
            lambda: self.show_logs_page_signal.emit()
        )
        # Ctrl on Mac is Command
        self.logs.setShortcut('Ctrl+L')
        self.logoutAction = QAction(QIcon("images/logout.png"),'Logout', self)
        self.logoutAction.triggered.connect(self.show_login_page)
        self.logoutAction.setShortcut('Ctrl+O')
        self.window.actionsMenu = self.window.menubar.addMenu('&Actions')
        self.window.actionsMenu.addAction(self.logs)
        self.window.actionsMenu.addAction(self.logoutAction)
        self.window.setCentralWidget(self)
        self.setStyleSheet(load_stylesheet())
        self.window.setWindowTitle("Home")
        layout = QVBoxLayout()
        self.welcome_label = QLabel(f'Welcome, {username}!')
        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.welcome_label)
        self.setLayout(layout)
        if isDBA(self.username):
            self.welcome_label.setText(self.welcome_label.text() + ' You are a DBA.')
            policyDbButton = QPushButton('Access Policy Database')
            policyDbButton.clicked.connect(
                lambda: self.show_policyDb_page_signal.emit()
            )
            layout.addWidget(policyDbButton)
        if isowner(self.username):
            self.welcome_label.setText(self.welcome_label.text() + ' You are an owner.')

            objectsowned = getObjectsAdmin(username)
        print (objectsowned)
        if objectsowned:
            dropwidget = QComboBox()
            dropwidget.addItems(objectsowned)
    def show_login_page(self):
        self.username = None
        self.actionsMenu.clear()
        self.show_login_page_signal.emit()
        
        

