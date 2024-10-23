import os

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.utils import platform
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText

# from satround.apt import decode

__version__ = '0.1.0'
Window.size = (360, 640)
screen = ScreenManager()


class InitScreen(Screen):
    def add_decode_button(self):
        self.add_widget(DecodeButton())


screen.add_widget(InitScreen(name='init'))


class DecodeButton(Screen): ...


class SatroundApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.selected_path,
            sort_by='date',
        )

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.title = 'Satround'
        return Builder.load_file('main.kv')

    def open_file_manager(self):
        start_path = (
            '/storage/emulated/0/' if platform == 'android' else os.getcwd()
        )
        self.file_manager.show(start_path)

    def selected_path(self, path: str):
        """
        It will be called when you click on the file name
        or the catalog selection button.
        """

        self.exit_manager()
        MDSnackbar(
            MDSnackbarText(
                text='Selected file.',
            ),
            y=dp(24),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            size_hint_x=0.8,
            radius=[dp(10), dp(10), dp(10), dp(10)],
        ).open()
        self.selected_path = path

    def exit_manager(self, *args):
        """Called when the user reaches the root of the directory tree."""

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        """Called when buttons are pressed on the mobile device."""

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    @staticmethod
    def decode_audio():
        try:
            # decode(self.selected_path)
            MDSnackbar(
                MDSnackbarText(
                    text='Saved image!',
                ),
                y=dp(24),
                pos_hint={'center_x': 0.5, 'center_y': 0.1},
                size_hint_x=0.8,
                radius=[dp(10), dp(10), dp(10), dp(10)],
            ).open()
        except Exception:
            print('There was an ERROR trying to decode.')
            MDSnackbar(
                MDSnackbarText(
                    text='There was an ERROR trying to decode.',
                ),
                y=dp(24),
                pos_hint={'center_x': 0.5, 'center_y': 0.1},
                size_hint_x=0.8,
                radius=[dp(10), dp(10), dp(10), dp(10)],
            ).open()


if __name__ == '__main__':
    SatroundApp().run()
