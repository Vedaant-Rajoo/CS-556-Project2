from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class TableScreen(MDScreen):
    def __init__(self, **kwargs):
        super(TableScreen, self).__init__(**kwargs)
        self.table = MDDataTable(
            background_color_header="#65275d",
            background_color_cell="#451938",
            size_hint=(0.95, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            rows_num=3,
            column_data=[
                ("Object", dp(25)),
                ("Policy Type", dp(20)),
                ("Delegation", dp(25)),
                ("Transfer", dp(25)),
                ("Acceptance", dp(25)),
                ("Revocation", dp(25)),
            ],
            row_data=[],

        )
        self.add_widget(self.table)

    def add_row(self, row_data):
        self.table.row_data.append(row_data)
        self.table.rows_num += 1
