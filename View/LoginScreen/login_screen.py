from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from apputils import load_kv
from scripts.login import login

load_kv(__name__)

app = MDApp.get_running_app()


class LoginScreen(MDScreen):

    def login(self, username, password):
        if login(username, password):
            self.manager.current = 'home'
            self.manager.transition.direction = 'left'
            app.state['username'] = username

        else:
            self.ids.password.error = True
            self.ids.username.text = ''
            self.ids.password.text = ''
            self.ids.username.focus = True

    def on_pre_leave(self, *args):
        self.ids.username.focus = True
