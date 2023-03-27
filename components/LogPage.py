from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

data = [
    ['John', 'Doe'],
    ['Jane', 'Doe'],
    ['Bob', 'Smith'],
    ['Alice', 'Jones'],
    ['Peter', 'Pan']
]
class LogsPage(QWidget):
    def __init__(self):
        super().__init__()
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
        
        