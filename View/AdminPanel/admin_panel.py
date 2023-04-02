from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from apputils import load_kv
from scripts.connect import addLog

load_kv(__name__)

app = MDApp.get_running_app()


class AdminPanel(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

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

    def execute(self):
        command = self.ids.com.text
        words = command.split(' ')
        privileges = []
        if words[0] == 'grant':
            user, *privileges = words[1].split(',')
            if self.checkpriv(privileges):
                privileges_str = ','.join(privileges)
                addLog(command, app.state['username'])
                self.ids.com.helper_text = 'Privileges granted'
                self.ids.com.text = ''
            else:
                self.ids.com.helper_text = 'Invalid Privilege'
                self.ids.com.text = ''
        elif words[0] == 'revoke':
            user, *privileges = words[1].split(',')
            if self.checkpriv(privileges):
                privileges_str = ','.join(privileges)
                addLog(command, app.state['username'])
                self.ids.com.helper_text = 'Privileges revoked'
                self.ids.com.text = ''
            else:
                self.ids.com.helper_text = 'Invalid Privilege'
                self.ids.com.text = ''
        elif words[0] == 'delegate':
            user = words[1]
            addLog(command, app.state['username'])
            self.ids.com.helper_text = 'Delegation successful'
            self.ids.com.text = ''
        elif words[0] == 'transfer':
            user = words[1]
            addLog(command, app.state['username'])
            self.ids.com.helper_text = 'Transfer successful'
            self.ids.com.text = ''

        else:
            self.ids.com.helper_text = 'Invalid Command'
            self.ids.com.text = ''

    @staticmethod
    def checkpriv(priv_list):
        for priv in priv_list:
            if priv not in ['select', 'insert', 'update', 'delete', 'create', 'drop', 'all']:
                return False
        return True
