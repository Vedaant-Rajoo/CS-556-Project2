from kivymd.uix.screen import MDScreen

from kivymd.app import MDApp
from apputils import load_kv
from scripts.connect import *

load_kv(__name__)

app = MDApp.get_running_app()


class AdminPanel(MDScreen):
    pass
