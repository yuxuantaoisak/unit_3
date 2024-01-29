## Solution ##

```.py

from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen


class MysteryPageA(MDScreen):
    def change_page(self):
        self.parent.current = "MysteryPageB"


class MysteryPageB(MDScreen):
    def change_page(self):
        self.parent.current = "MysteryPageA"


class quiz_042(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        Window.size = (900, 900)

    def change_page(self):
        print("test")


test = quiz_042()
test.run()


```



```.kv

ScreenManager:
    id: screens

    MysteryPageA:
        name: "MysteryPageA"

    MysteryPageB:
        name: "MysteryPageB"


<MysteryPageA>:
    MDRaisedButton:
        pos: dp(250), dp(250)
        text: "This is mystery page A you pressed the button"
        on_press:
            root.change_page()
            app.change_page()


<MysteryPageB>:
    MDRaisedButton:
        pos: dp(250), dp(250)
        text: "This is mystery page B you pressed the button"
        on_press:
            root.change_page()
            app.change_page()


```



## Proof of work ##



https://github.com/yuxuantaoisak/unit_3/assets/144768397/1322d510-41df-4d1a-832b-60deb8aab91d


