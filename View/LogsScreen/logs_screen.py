from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from apputils import load_kv
from scripts.connect import getLogs

load_kv(__name__)

app = MDApp.get_running_app()


class LogsScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.data = None

    def logout(self):
        self.manager.get_screen('login').ids.username.text = ''
        self.manager.get_screen('login').ids.password.text = ''
        app.state['username'] = ''

        self.manager.current = 'login'
        self.manager.transition.direction = 'right'

    def gohome(self):
        app.title = 'CS556 Project - Home'
        self.manager.current = 'home'
        self.manager.transition.direction = 'right'

    def on_enter(self, *args):
        self.data = getLogs()
        for log in self.data:
            self.ids.logs_table.add_row(log)
