from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from scripts.connect import *
from apputils import load_kv
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineListItem

load_kv(__name__)

app = MDApp.get_running_app()


class PolicyEditor(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.data = None
        self.objs = getObjects()
        self.pts = ['object-owner', 'DBA', 'object-curator']
        self.dlgs = ['delegation', 'no-delegation', 'nil']
        self.trns = ['transfer', 'no-transfer', 'nil']
        self.acpts = ['acceptance', 'no-acceptance', 'nil']
        self.rvks = ['revoke', 'grantor-transfer', 'nil']

        obj_items = [{
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": f"{obj[0]}",
            "on_release": lambda x=f"{obj[0]}": self.set_item(x),
        } for obj in self.objs]

        pt_items = [{
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": f"{pt}",
            "on_release": lambda x=f"{pt}": self.set_pt_item(x),
        } for pt in self.pts]

        dlg_items = [{
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": f"{dlg}",
            "on_release": lambda x=f"{dlg}": self.set_dlg_item(x),
        } for dlg in self.dlgs]

        trn_items = [{
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": f"{trn}",
            "on_release": lambda x=f"{trn}": self.set_trn_item(x),
        } for trn in self.trns]

        acpt_items = [{
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": f"{acpt}",
            "on_release": lambda x=f"{acpt}": self.set_acpt_item(x),
        } for acpt in self.acpts]

        rvk_items = [{
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": f"{rvk}",
            "on_release": lambda x=f"{rvk}": self.set_rvk_item(x),
        } for rvk in self.rvks]

        self.obj_menu = MDDropdownMenu(
            caller=self.ids.object_name,
            items=obj_items,
            position="bottom",
            width_mult=4,
        )

        self.pt_menu = MDDropdownMenu(
            caller=self.ids.policy_type,
            items=pt_items,
            position="top",
            width_mult=4,
        )

        self.dlg_menu = MDDropdownMenu(
            caller=self.ids.delegation,
            items=dlg_items,
            position="bottom",
            width_mult=4,
        )

        self.trn_menu = MDDropdownMenu(
            caller=self.ids.transfer,
            items=trn_items,
            position="top",
            width_mult=4,
        )

        self.acpt_menu = MDDropdownMenu(
            caller=self.ids.acceptance,
            items=acpt_items,
            position="bottom",
            width_mult=4,
        )

        self.rvk_menu = MDDropdownMenu(
            caller=self.ids.revocation,
            items=rvk_items,
            position="top",
            width_mult=4,
        )

    def set_item(self, text_item):
        self.ids.object_name.text = text_item
        self.obj_menu.dismiss()

    def set_pt_item(self, text_item):
        self.ids.policy_type.text = text_item
        self.pt_menu.dismiss()

    def set_dlg_item(self, text_item):
        self.ids.delegation.text = text_item
        self.dlg_menu.dismiss()

    def set_trn_item(self, text_item):
        self.ids.transfer.text = text_item
        self.trn_menu.dismiss()

    def set_acpt_item(self, text_item):
        self.ids.acceptance.text = text_item
        self.acpt_menu.dismiss()

    def set_rvk_item(self, text_item):
        self.ids.revocation.text = text_item
        self.rvk_menu.dismiss()

    def on_enter(self, *args):
        self.data = getPolicies()
        for policy in self.data:
            self.ids.table_screen.add_row(policy)

    def logout(self):
        self.manager.get_screen('login').ids.username.text = ''
        self.manager.get_screen('login').ids.password.text = ''
        app.state['username'] = ''

        self.manager.current = 'login'
        self.manager.transition.direction = 'right'

    def gohome(self):
        self.manager.current = 'home'
        self.manager.transition.direction = 'right'

    def add_policy(self):
        obj = self.ids.object_name.text
        pt = self.ids.policy_type.text
        dlg = self.ids.delegation.text
        trn = self.ids.transfer.text
        acpt = self.ids.acceptance.text
        rvk = self.ids.revocation.text
        if obj == '' or pt == '' or dlg == '' or trn == '' or acpt == '' or rvk == '':
            self.ids.object_name.error = True
        else:
            add_Policy(obj, pt, dlg, trn, acpt, rvk)
            self.ids.table_screen.add_row((obj, pt, dlg, trn, acpt, rvk))
            self.ids.object_name.error = False
            # self.ids.table_screen.add_row((obj, pt, dlg, trn, acpt, rvk))
            self.ids.object_name.text = ''
            self.ids.policy_type.text = ''
            self.ids.delegation.text = ''
            self.ids.transfer.text = ''
            self.ids.acceptance.text = ''
            self.ids.revocation.text = ''
