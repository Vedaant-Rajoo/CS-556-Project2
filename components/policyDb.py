from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from scripts.connect import getPolicies

data = getPolicies()


class PolicyDbPage(QWidget):
    show_login_page_signal = pyqtSignal()
    show_logs_page_signal = pyqtSignal()
    def __init__(self,window):
        super().__init__()
        self.window = window
        self.window.setCentralWidget(self)
        self.window.setWindowTitle("Policy Database")
        self.logs = QAction(QIcon("images/logs.png"),'Logs', self)
        self.logs.triggered.connect(
            lambda: self.show_logs_page_signal.emit()
        )
        self.logs.setShortcut('Ctrl+L')
        self.logoutAction = QAction(QIcon("images/logout.png"),'Logout', self)
        self.logoutAction.triggered.connect(self.show_login_page)
        self.logoutAction.setShortcut('Ctrl+O')
        self.window.actionsMenu.addAction(self.logs)
        self.window.actionsMenu.addAction(self.logoutAction)
        layout = QVBoxLayout()
        table_logs = QTableWidget()
        table_logs.setRowCount(len(data))
        table_logs.setColumnCount(6)
        table_logs.setHorizontalHeaderLabels(['Object', 'Policy Types','Delegation','Transfer','Acceptance','Revoke Options'])
        for row in range(len(data)):
            for column in range(2):
                table_logs.setItem(row, column, QTableWidgetItem(data[row][column]))
        layout.addWidget(table_logs)
        self.setLayout(layout)
    def show_login_page(self):
        self.username = None
        self.window.actionsMenu.clear()
        self.show_login_page_signal.emit()
   