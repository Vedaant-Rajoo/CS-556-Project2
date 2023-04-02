from kivymd.uix.screen import MDScreen

from kivymd.app import MDApp
from apputils import load_kv
from scripts.connect import *

load_kv(__name__)

app = MDApp.get_running_app()


class HomeScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.username = None

    def on_enter(self, *args):
        self.username = app.state['username']
        self.ids.home_appbar.title = f"{self.username}"
        if isowner(self.username) and isDBA(self.username) and len(self.ids.home_appbar.right_action_items) <= 1:
            self.ids.home_appbar.right_action_items.insert(0, ['shield-check', lambda x: self.goToPolicyEditor(),
                                                               'Open Policy Editor'])
            self.ids.home_appbar.right_action_items.insert(0, ['account-supervisor', lambda x: self.admin(),
                                                               'Open Admin Panel'])
            self.ids.home_appbar.right_action_items.insert(0, ['history',
                                                               lambda x: self.goLogs(),
                                                               'Open Logs'])
            self.ids.home_label.text = f"Welcome to the Home Screen!\n You are a DBA and an owner/curator in the database."
        elif isowner(self.username) and not isDBA(self.username) and len(self.ids.home_appbar.right_action_items) <= 1:
            self.ids.home_appbar.right_action_items.insert(0, ['account-supervisor', lambda x: self.admin(),
                                                               'Open Admin Panel'])
            self.ids.home_appbar.right_action_items.insert(0, ['file-document-box-multiple-outline',
                                                               lambda x: self.goLogs(),
                                                               'Open Logs'])
            self.ids.home_label.text = f"Welcome to the Home Screen!\n You are an owner/curator in the database."
        else:
            self.ids.home_label.text = f"Welcome to the Home Screen {self.username}!"

    def logout(self):
        self.manager.get_screen('login').ids.username.text = ''
        self.manager.get_screen('login').ids.password.text = ''
        app.state['username'] = ''

        self.manager.current = 'login'
        self.manager.transition.direction = 'right'

    def admin(self):
        pass

    def goToPolicyEditor(self):
        app.title = 'CS556 Project - Policy Editor'
        self.manager.current = 'policy_editor'
        self.manager.transition.direction = 'left'

    def goLogs(self):
        app.title = 'CS556 Project - Logs'
        self.manager.current = 'logs'
        self.manager.transition.direction = 'left'
