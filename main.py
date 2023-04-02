from kivy.config import Config

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'minimum_width', '600')
Config.set('graphics', 'minimum_height', '400')

from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.theming import ThemeManager
from kivymd.color_definitions import colors


class GruvboxTheme(ThemeManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_style = 'Dark'
        self.primary_palette = 'Teal'
        self.gruvbox_dark = (
            colors["gruvbox-dark"][x]
            for x in (
            "bg0", "bg1", "bg2", "bg3", "bg4",
            "red", "green", "yellow",
            "blue", "purple", "aqua", "gray"
        )
        )


class ScreenManager(MDScreenManager):
    def get_classes(self):
        return {screen.__class__.__name__: screen.__class__.__module__ for screen in self.screens}


class MainApp(MDApp):
    DEBUG = True
    sm = None
    state = {}

    def build_app(self, first=False):
        self.theme_cls = GruvboxTheme()
        self.title = 'CS556 Project'
        if self.sm is None:
            self.state = {'current': 'login',
                          'username': ''
                          }
        else:
            self.state = {
                'current': self.sm.current,
                'username': ''
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
