from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen


class SecondScreen(MDScreen):
    pass


class MainScreen(MDScreen):
    def change_to_page_2(self):
        print("Changing to page 2")
        self.parent.current = "SecondScreen"


class Screens(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        Window.size = (400, 900)

    def change_to_page_2(self):
        print("I can also change here to page 2")


test = Screens()
test.run()
