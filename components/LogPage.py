from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
data = [
    ['John', 'Doe'],
    ['Jane', 'Doe'],
    ['Bob', 'Smith'],
    ['Alice', 'Jones'],
    ['Peter', 'Pan']
]
class LogsPage(QWidget):
    show_login_page_signal = pyqtSignal()
    show_home_page_signal = pyqtSignal()
    def __init__(self,window):
        super().__init__()
        self.window = window
        self.window.setCentralWidget(self)
        self.window.setWindowTitle("Logs")
        self.homePage = QAction(QIcon("images/home.png"),'Home', self)
        self.homePage.triggered.connect(
            lambda: self.show_home_page_signal.emit()
        )
        self.homePage.setShortcut('Ctrl+P')
        self.logoutAction = QAction(QIcon("images/logout.png"),'Logout', self)
        self.logoutAction.triggered.connect(self.show_login_page)
        self.logoutAction.setShortcut('Ctrl+O')
        self.window.actionsMenu.addAction(self.homePage)
        self.window.actionsMenu.addAction(self.logoutAction)
        layout = QVBoxLayout()
        table_logs = QTableWidget()
        table_logs.setRowCount(len(data))
        table_logs.setColumnCount(2)
        table_logs.setHorizontalHeaderLabels(['First Name', 'Last Name'])
        for row in range(len(data)):
            for column in range(2):
                table_logs.setItem(row, column, QTableWidgetItem(data[row][column]))
        layout.addWidget(table_logs)
        self.setLayout(layout)
    def show_login_page(self):
        self.username = None
        self.window.actionsMenu.clear()
        self.show_login_page_signal.emit()    

        