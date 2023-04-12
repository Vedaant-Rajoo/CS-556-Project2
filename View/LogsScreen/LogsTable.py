from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from scripts.connect import getLogs


class LogsTable(MDScreen):
    def __init__(self, **kwargs):
        super(LogsTable, self).__init__(**kwargs)
        self.table = MDDataTable(
            background_color_header="#3c3836",
            size_hint=(0.95, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            rows_num=len(getLogs()) + 1,
            column_data=[
                ('Time', dp(40)),
                ('Command', dp(80)),
                ('User', dp(20)),
            ],
            row_data=[],

        )
        self.add_widget(self.table)

    def add_row(self, row_data):
        self.table.row_data.append(row_data)
        self.table.rows_num += 1
