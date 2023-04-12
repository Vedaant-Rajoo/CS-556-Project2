from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from AuthGraph import AuthGraph, AuthGraphError
from apputils import load_kv
from scripts.connect import addLog, getPolicies, getJSONGraph, isOwner, allAccessToJson
from scripts.groperations import *

load_kv(__name__)

app = MDApp.get_running_app()


class AdminPanel(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.conn = None
        self.obj = ''
        self.policy = []
        self.ag = None

    def on_enter(self, *args):
        app.title = 'CS556 Project - Admin Panel'
        self.ids.admin_appbar.title = f"Admin Panel - {app.state['obj']}"
        self.obj = app.state['obj']
        self.conn = connect(app.state['username'], app.state['username'])
        self.policy = getPolicies(self.obj)
        self.ag = AuthGraph(self.policy)
        data = getJSONGraph(self.obj)
        if data:
            self.ag.load_graph(data[0])
            if not self.ag.has_node(app.state['username']):
                if isOwner(app.state['username'], self.obj):
                    self.ag.add_user(app.state['username'], 'owner')
                else:
                    self.ag.add_user(app.state['username'], 'curator')

    def logout(self):
        app.title = 'CS556 Project - Login'
        json_data = self.ag.save_graph()
        allAccessToJson(app.state['username'])
        saveJson(self.conn, self.obj, json_data)
        self.manager.get_screen('login').ids.username.text = ''
        self.manager.get_screen('login').ids.password.text = ''
        app.state['username'] = ''
        self.manager.get_screen('login').ids.username.focus = True
        self.manager.current = 'login'
        self.manager.transition.direction = 'right'

    def gohome(self):
        app.title = 'CS556 Project - Home'
        self.manager.current = 'home'
        self.manager.transition.direction = 'right'

    def f_execute(self):
        try:
            self.execute()
        except Exception as e:
            self.ids.com.helper_text = str(e)
            self.ids.com.text = ''

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
                self.grant(app.state['username'], user, privileges_str)
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
                self.revoke(app.state['username'], user, privileges_str)
            else:
                self.ids.com.helper_text = 'Invalid Privilege'
                self.ids.com.text = ''
        elif words[0] == 'delegate':
            user = words[1]
            addLog(command, app.state['username'])
            self.ids.com.helper_text = 'Delegation successful'
            self.ids.com.text = ''
            self.delegate(app.state['username'], user)
        elif words[0] == 'transfer':
            user = words[1]
            addLog(command, app.state['username'])
            self.ids.com.helper_text = 'Transfer successful'
            self.ids.com.text = ''
            self.transfer(app.state['username'], user)

        elif words[0] == 'revoke_admin':
            user = words[1]
            addLog(command, app.state['username'])
            self.ids.com.helper_text = 'Admin privileges revoked'
            self.ids.com.text = ''
            self.revoke_admin(app.state['username'], user)

        else:
            self.ids.com.helper_text = 'Invalid Command'
            self.ids.com.text = ''

    @staticmethod
    def checkpriv(priv_list):
        for priv in priv_list:
            if priv not in ['select', 'insert', 'update', 'delete', 'create', 'drop', 'all']:
                return False
        return True

    def grant(self, grantor, grantee, privileges):
        if self.ag.has_edge(grantor, grantee):
            grant_u(self.conn, grantor, grantee, self.obj, privileges)

    def delegate(self, grantor, grantee):
        self.ag.delegate(grantor, grantee)
        delegate(self.conn, self.obj, grantee, grantor)

    def transfer(self, grantor, grantee):
        self.ag.transfer(grantor, grantee)

    def revoke(self, grantor, grantee, privileges):
        if self.ag.has_edge(grantor, grantee):
            revoke(self.conn, grantor, grantee, privileges)

    def revoke_admin(self, grantor, grantee):
        pass
