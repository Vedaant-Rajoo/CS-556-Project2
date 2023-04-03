from kivy.config import Config

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'minimum_width', '600')
Config.set('graphics', 'minimum_height', '400')

from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.theming import ThemeManager


class GruvboxTheme(ThemeManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_style = 'Dark'
        self.primary_palette = 'Teal'


class ScreenManager(MDScreenManager):
    def get_classes(self):
        return {screen.__class__.__name__: screen.__class__.__module__ for screen in self.screens}


class MainApp(MDApp):
    DEBUG = True
    sm = None
    state = {}

    def build_app(self, first=False):
        self.title = 'CS556 Project'
        self.theme_cls = GruvboxTheme()
        if self.sm is None:
            self.state = {'current': 'login',
                          'username': '',
                          'obj': ''
                          }
        else:
            self.state = {
                'current': self.sm.current,
                'username': '',
                'obj': ''
            }

        self.sm = ScreenManager()
        CLASSES = self.sm.get_classes()

        return self.sm

    def apply_state(self, state):
        self.sm.current = state['current']

    def clear_mdlist(self):
        mdlist = self.sm.get_screen('home').ids.home_list
        for child in mdlist.children[:]:
            mdlist.remove_widget(child)


if __name__ == '__main__':
    app = MainApp()
    app.run()
