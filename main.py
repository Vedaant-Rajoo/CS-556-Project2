from kivy.config import Config

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'minimum_width', '600')
Config.set('graphics', 'minimum_height', '400')

from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager


class ScreenManager(MDScreenManager):
    def get_classes(self):
        return {screen.__class__.__name__: screen.__class__.__module__ for screen in self.screens}


# class LoginScreen(MDScreen):
#     username = ObjectProperty(None)
# 
#     @staticmethod
#     def login(self, username, password):
#         if login(username, password):
#             self.manager.current = 'home'
#             self.manager.transition.direction = 'left'
#         else:
#             self.ids.password.error = True
#             self.ids.username.text = ''
#             self.ids.password.text = ''
#             self.ids.username.focus = True
# 
#     def on_pre_leave(self, *args):
#         self.ids.username.focus = True
#         global g_username
#         g_username = self.ids.username.text
# 

# class HomeScreen(MDScreen):
# 
#     def on_enter(self, *args):
#         self.ids.home_label.text = f'Welcome {g_username}'
#         print(self.manager.current)
# 
#     def logout(self):
#         self.manager.current = 'login'
#         self.manager.transition.direction = 'right'

class MainApp(MDApp):
    DEBUG = True
    sm = None
    state = {}

    def build_app(self, first=False):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        if self.sm is None:
            self.state = {'current': 'login'
                          }
        else:
            self.state = {
                'current': self.sm.current,
            }
        KV_FILES = []
        self.sm = ScreenManager()
        CLASSES = self.sm.get_classes()

        return self.sm

    def apply_state(self, state):
        self.sm.current = state['current']


if __name__ == '__main__':
    app = MainApp()
    app.run()
